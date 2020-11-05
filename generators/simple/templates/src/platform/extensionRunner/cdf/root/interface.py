"""CoveoInterface base."""

import json
import re
import socket
from functools import wraps
from pathlib import Path
from typing import Pattern, Any, ClassVar, Callable, Dict, cast
from urllib import parse
from urllib.parse import ParseResult

from inflection import camelize
from requests import Session, Request, Response
from requests.adapters import HTTPAdapter

from corepyutils.annotations import find_return_annotation
from corepyutils.casing import flexcase
from cdf.root.deserializer import deserialize
from cdf.root.serializer import JidEncoder

_IP_MATCH_REGEX: Pattern = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
_CLOUD_HEXIP_MATCH: Pattern = re.compile(r'\bip-[a-f0-9]{8}\b')


TIMEOUT_S = 70  # seconds

# this is the typing annotation used when multiple values are returned.
MultiOut = Dict[str, Any]


class CoveoInterface:
    """Base class for generated coveo interfaces."""
    __slots__ = ('base_url',)

    def __init__(self, base_url: str, certificate: Path = None) -> None:
        if certificate:
            api.set_certificate(certificate)

        # handle some special url cases
        check_url = parse.urlparse(base_url)
        host, port = check_url.hostname, check_url.port
        if _CLOUD_HEXIP_MATCH.match(host):
            # this is a ip-hex uri from the cloud, which only resolves inside AWS.
            # we'll use its ip instead, which should be reachable.
            hex_ip = host.split('-')[-1]
            ip = []
            for i in range(0, 8, 2):
                ip.append(str(int(hex_ip[i:i + 2], 16)))
            host = ".".join(ip)
        if 'cloud.coveo.com' not in host and not _IP_MATCH_REGEX.match(host):
            # we'll convert the hostname to its IP
            # this prevents retries in the http libs and speeds up calls tenfold.
            # the cloud.coveo.com check can be removed once certificates are supported
            host = socket.gethostbyname_ex(host)[-1][0]
        netloc = ':'.join((host, str(port))) if port else host

        self.base_url: ParseResult = cast(ParseResult, parse.urlunparse(
            (check_url.scheme,
             netloc,
             check_url.path if check_url.path.startswith('/api/') else '/api' + check_url.path,
             check_url.query,
             check_url.params,
             check_url.fragment)))


class CertificateSwitchException(Exception):
    """Certificates may be set only once."""


# noinspection PyPep8Naming
class api:
    """
    Decorator for rest api Methods. Usage:

    class IJobConsumer(CoveoInterface):
        @api('POST/v1/organizations/{OrganizationId}/providers/{InstanceId}/jobs/{JobId}/status', out=True)
        def report_status(self, *, OrganizationId: str, InstanceId: str, ...) -> JobInterrupt:
            '''Send the status of the job currently being executed'''

    All wrapped methods will also support some special argments:
        _timeout: (seconds) int that can be used to specfy a timeout value.
        _raw: bool that can be used to return the response as a dict (i.e. no wrappers)
    """
    __slots__ = 'verb', 'path', 'pep8_camel'

    session: ClassVar[Session] = Session()  # the session exists for the lifetime of the interpreter
    session.verify = False
    session.mount("https://", HTTPAdapter(pool_connections=30, pool_maxsize=1000))
    session.mount("http://", session.adapters['https://'])
    session.headers.update({'content-type': 'application/json', 'charset': 'utf8'})

    def __init__(self, verb_and_url: str, **pep8_to_camel: str) -> None:
        self.verb, self.path = verb_and_url.split('/', maxsplit=1)
        self.pep8_camel = pep8_to_camel

    def __call__(self, fn: Callable) -> Callable:
        """Replace the method by our implementation."""
        return_response_type = find_return_annotation(fn)

        @wraps(fn)
        def _api_wrapper(interface: CoveoInterface, *, _raw: bool = False, _timeout: int = None, **kwargs: Any) -> Any:
            """Note: the original `fn` is called as usual (before the REST request) but its return value is ignored."""
            __tracebackhide__ = True
            fn(interface, **kwargs)

            # sanitize input
            deserialized = deserialize(kwargs, hint=fn)

            response = self._rest_request(interface, deserialized) if _timeout is None \
                else self._rest_request(interface, deserialized, _timeout)

            hint = return_response_type

            if response.ok and (isinstance(hint, type(None)) or not response.content):
                return

            content = response.json(strict=False)
            if content is None:
                return None
            if _raw:  # this one shortcuts before the exception check
                return content

            # IP-519: this part needs improvement and works for some scenarios but not all.
            # the multi-out will work, but some single-out methods may have a different return key that may not be
            # picked up. need more meta to determine it.
            if hint is MultiOut:
                assert isinstance(content, dict)
                hint = Dict[str, Any]  # deserialize into a Dict
            elif isinstance(content, dict):
                for return_path in ('ReturnValue', getattr(return_response_type, '__name__', None)):
                    if return_path in content:
                        assert len(content) == 1
                        content = content[return_path]
                        break

            return_value = deserialize(content, hint=hint)

            if isinstance(return_value, Exception):
                raise return_value

            return return_value

        return flexcase(_api_wrapper, allowed_extras=['_raw', '_timeout'])

    # noinspection PyDefaultArgument
    def _rest_request(self, interface: CoveoInterface, body: Dict[str, Any] = {}, timeout: int = TIMEOUT_S) \
            -> Response:
        """Generic REST request."""
        camel_body = {self.pep8_camel.get(k, camelize(k)): v for k, v in body.items()}
        request = self.session.prepare_request(Request(
            self.verb,
            '/'.join((str(interface.base_url), self.path.format(**(body or {})))),
            data=json.dumps(camel_body, ensure_ascii=False, cls=JidEncoder).encode()))

        return cast(Response, self.session.send(request, timeout=timeout))

    @classmethod
    def set_certificate(cls, certificate: Path) -> None:
        """It's possible to set the certificate for the session, once."""
        if certificate:
            # You cannot change the certificate once it's set.
            if cls.session.cert and Path(cls.session.cert).read_text() != certificate.read_text():  # type: ignore
                raise CertificateSwitchException
            cls.session.cert = str(certificate)  # shame; request doesn't support pathlib yet.
