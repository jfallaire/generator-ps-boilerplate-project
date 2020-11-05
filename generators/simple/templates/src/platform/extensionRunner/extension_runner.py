# coding=utf-8

"""
 Will run an Indexing Pipeline Extension script on a document
"""

import io
import uuid
import collections
import os
import json
import datetime


PERMISSION_IDENTITY_TYPE = {
    'user',
    'group',
    'virtual_group',
    'virtualgroup',
    'unknown'
}

UTF16_STREAMS = {'body_text'}
TEXT_STREAMS = {'body_text', 'body_html'}


class RejectedException(Exception):
    def __init__(self, *args):
        super(RejectedException, self).__init__(*args)
        
        
class SkippedException(Exception):
    def __init__(self, *args):
        super(SkippedException, self).__init__(*args)



class CaseInsensitiveDict(dict):
    @classmethod
    def _k(cls, key):
        return key.lower() if isinstance(key, str) else key

    def __init__(self, *args, **kwargs):
        super(CaseInsensitiveDict, self).__init__(*args, **kwargs)
        self._convert_keys()

    def __getitem__(self, key):
        return super(CaseInsensitiveDict, self).__getitem__(self.__class__._k(key))

    def __setitem__(self, key, value):
        super(CaseInsensitiveDict, self).__setitem__(self.__class__._k(key), value)

    def __delitem__(self, key):
        return super(CaseInsensitiveDict, self).__delitem__(self.__class__._k(key))

    def __contains__(self, key):
        return super(CaseInsensitiveDict, self).__contains__(self.__class__._k(key))

    def pop(self, key, *args, **kwargs):
        return super(CaseInsensitiveDict, self).pop(self.__class__._k(key), *args, **kwargs)

    def get(self, key, *args, **kwargs):
        return super(CaseInsensitiveDict, self).get(self.__class__._k(key), *args, **kwargs)

    def setdefault(self, key, *args, **kwargs):
        return super(CaseInsensitiveDict, self).setdefault(self.__class__._k(key), *args, **kwargs)

    def update(self, E=None, **F):
        super(CaseInsensitiveDict, self).update(self.__class__(E or {}))
        super(CaseInsensitiveDict, self).update(self.__class__(**F))

    def _convert_keys(self):
        for k in list(self.keys()):
            v = super(CaseInsensitiveDict, self).pop(k)
            self.__setitem__(k, v)


class DocumentApi(object):
    working_path = ''

    def __init__(self, document_state):
        """
        Wraps the various APIs on a document

        :param ApiV1.DocumentState document_state: the document state
        """
        self.v1 = ApiV1(document_state)
        self.legacy = ApiLegacy(self.v1)
        self.latest = self.v1


class ApiLegacy(object):
    def __init__(self, api_v1):
        """
        api used with old mapping script before we had the IPE
        """
        self._api_v1 = api_v1

    def log(self, id_, message, severity='normal'):
        self._api_v1.log(message, severity)

    def get_meta_data(self, id_):
        return self._api_v1.get_meta_data()

    def add_meta_data(self, id_, meta_data):
        self._api_v1.add_meta_data(meta_data)


class ApiV1(object):
    _json_valid_translation = {int, bool, float, None, str, datetime.datetime, datetime.date, bytes}

    def __init__(self, document_state):
        """
        First version of the document API

        :param DocumentState document_state: the document state
        """
        self._document_state = document_state

        # hook our own json encoder
        self._old_json_encoder = json.JSONEncoder
        self._old_default_json_encoder = json._default_encoder
        json.JSONEncoder = self.JsonEncoder
        json._default_encoder = self.JsonEncoder()

    def __del__(self):
        # set back the original json encoder
        json.JSONEncoder = self._old_json_encoder
        json._default_encoder = self._old_default_json_encoder

    def log(self, message, severity='normal'):
        """
        add a log entry

        :param str message: the message
        :param str severity: the severity
        """
        if message is not None:
            self._document_state.log_entries.append((str(message), str(severity)))

    def get_meta_data(self):
        """
        get the current meta data on the document

        :return: list[MetaDataValue]
        """
        return self._document_state.current_meta_data + [ApiV1.MetaDataValue(self._document_state.origin, {k: v}) for k, v in self._document_state.meta_data_to_add.items()]

    def get_meta_data_value(self, name, origin=None, reverse=True):
        """
        get the meta data values

        :param str name: name of the meta values to get
        :param str origin: origin
        :param bool reverse: whether or not to scan in reverse
        :return: list[str]
        """
        origin = origin.lower() if origin else None
        name = name.lower()
        meta = reversed(self.get_meta_data()) if reverse else self.get_meta_data()

        for m in meta:
            if (not origin or origin == m.origin) and name in m.values:
                return m.values[name]

        return []

    @staticmethod
    def _json_translation(obj):
        """ will force as a string when the obj cannot be converted to json natively """
        if type(obj) in ApiV1._json_valid_translation:
            return obj
        else:
            return str(obj)

    def add_meta_data(self, meta_data):
        """
        add meta data to the document

        :param dict[str, str|list[str|Object]] meta_data: the meta data to add to the document
        """
        for k, v in meta_data.items():
            if isinstance(v, collections.abc.Iterable) and not isinstance(v, str):
                self._document_state.meta_data_to_add[k.lower()] = [ApiV1._json_translation(val) if val is not None else '' for val in v]
            else:
                self._document_state.meta_data_to_add[k.lower()] = [ApiV1._json_translation(v) if v is not None else '']

    def get_permissions(self):
        """
        will get the current permissions on the document

        :return: list[PermissionLevel]
        """
        return self._document_state.final_permissions

    def clear_permissions(self):
        """
        will clear the final permissions on the document
        """
        self._document_state.final_permissions = []

    def set_permissions(self, permission_levels):
        """
        will set the final permissions on the document

        :param list[PermissionLevel] permission_levels: the final permissions
        """
        if isinstance(permission_levels, collections.abc.Iterable):
            self._document_state.final_permissions = permission_levels
        else:
            self._document_state.final_permissions = [permission_levels]

    def add_allowed(self, identity, identity_type, security_provider, additional_info=None):
        """
        Will add an allowed permission

        :param str identity: the identity
        :param str identity_type: the identity type
        :param str security_provider: the provider
        :param dict additional_info: additional info for the identity
        """
        self._document_state.force_one_level_and_set()
        self._document_state.final_permissions[0].permission_sets[0].allowed_permissions.append(ApiV1.Permission(identity, identity_type, security_provider, additional_info))

    def add_denied(self, identity, identity_type, security_provider, additional_info=None):
        """
        Will add a denied permission

        :param str identity: the identity
        :param str identity_type: the identity type
        :param str security_provider: the provider
        :param dict additional_info: additional info for the identity
        """
        self._document_state.force_one_level_and_set()
        self._document_state.final_permissions[0].permission_sets[0].denied_permissions.append(ApiV1.Permission(identity, identity_type, security_provider, additional_info))

    def get_data_streams(self):
        """
        will get the current datastreams for that document
        :return: list[ReadOnlyDataStream]
        """
        return self._document_state.current_streams + self._document_state.streams_to_add

    def get_data_stream(self, name, origin=None, reverse=True):
        """
        will a specific data stream for a given origin
        :param str name: the name of the stream
        :param str origin: the origin of the stream to get, when None we consider all origins
        :param bool reverse: whether to scan the stream in reverse order
        :return: BytesIO
        """
        origin = origin.lower() if origin else None
        name = name.lower()
        streams = reversed(self.get_data_streams()) if reverse else self.get_data_streams()

        for stream in streams:
            if (not origin or stream.origin == origin) and stream.name == name:
                stream.seek(0)
                return stream

    def add_data_stream(self, stream):
        """
        will add a data stream

        :param BytesIO stream: the stream to add
        """
        stream.flush()
        stream.origin = self._document_state.origin
        self._document_state.streams_to_add.append(stream)

    def reject(self, reason=''):
        """
        will reject the document
        """
        self._document_state.reject_document = True
        self._document_state.reject_reason = reason        
        raise RejectedException(reason)
        
    def skip(self, reason=''):
        """
        will skip the current script execution
        """
        raise SkippedException(reason)

    @property
    def uri(self):
        """
        Will get the document uri

        :return: str
        """
        return self._document_state.uri

    def _to_json(self):
        """
        The document as json

        :return: dict
        """
        return {'URI': self.uri,
                'MetaData': self.get_meta_data(),
                'DataStreams': self.get_data_streams(),
                'Permissions': self.get_permissions()}

    #
    # Object definitions for this api version
    #
    class JsonEncoder(json.JSONEncoder):
        def __init__(self, **kwargs):
            """
            Json encoder that support our API classes

            :param kwargs: the args
            """
            super(ApiV1.JsonEncoder, self).__init__(**kwargs)

        def default(self, obj):
            """
            Will encode to json and object

            :param obj: the object to encode
            :return: the json for that object
            """
            if isinstance(obj, (ApiV1, ApiV1.MetaDataValue, ApiV1.PermissionLevel, ApiV1.PermissionSet,
                                ApiV1.Permission, ApiV1.ReadOnlyDataStream, ApiV1.DataStream)):
                return obj._to_json()

            if isinstance(obj, datetime.datetime):
                return int((obj - datetime.datetime(1970, 1, 1, tzinfo=obj.tzinfo)).total_seconds())

            if isinstance(obj, datetime.date):
                return int((obj - datetime.date(1970, 1, 1)).total_seconds())

            try:
                return super(ApiV1.JsonEncoder, self).default(obj)
            except TypeError:
                if obj.__str__:
                    return obj.__str__()

    class DocumentState(object):
        def __init__(self, document_id, meta_data, permissions, streams, origin):
            """
            The state of a document before & after running the script

            :param str document_id: the document id
            :param list[MetaDataValue] meta_data: the current meta data
            :param list[PermissionLevel] permissions: the current permissions
            :param list[ReadOnlyDataStream|DataStream] streams : the requests streams
            :param str origin: origin of the new meta/stream
            """
            self.uri = document_id
            self.current_meta_data = meta_data
            self.current_streams = streams
            self.final_permissions = permissions
            self.origin = origin
            self.meta_data_to_add = {}
            self.streams_to_add = []
            self.log_entries = []
            self.reject_document = False
            self.reject_reason = ''

        @property
        def result(self):
            """
            the result of the script execution

            :return: ApiV1.Result
            """
            return ApiV1.Result(self.meta_data_to_add,
                                self.final_permissions,
                                self.streams_to_add,
                                self.log_entries,
                                self.reject_document,
                                self.reject_reason)

        def force_one_level_and_set(self):
            """
            Will make sure to have only 1 level with 1 set. Needed when using the simple permissions methods like add_allowed/denied
            """
            if not self.final_permissions or len(self.final_permissions) > 1:
                # force 1 level
                self.final_permissions = [ApiV1.PermissionLevel(permission_sets=[ApiV1.PermissionSet()])]
            elif not self.final_permissions[0].permission_sets or len(self.final_permissions[0].permission_sets) > 1:
                # force 1 set in that level
                self.final_permissions[0].permission_sets = [ApiV1.PermissionSet()]

        def close_streams(self):
            """
            Will close all opened streams

                self.streams_to_add are closed on add_data_stream
            """
            for s in self.current_streams:
                s.close()

            for s in self.streams_to_add:
                s.close()                

    class ReadOnlyDataStream(io.RawIOBase):
        def __init__(self, name, origin, file_name, inline_blob):
            """
            A read-only data stream

            :param str name: stream name
            :param str origin: stream origin
            :param str file_name: the name of the file on disk
            :param str inline_blob: the content of the blob when inline

            """
            super(ApiV1.ReadOnlyDataStream, self).__init__()
            self._name = name.lower()
            self._origin = origin.lower()
            self._filename = None

            is_text = name.lower() in TEXT_STREAMS
            encoding = 'utf-16le' if name.lower() in UTF16_STREAMS else 'utf-8-sig' if self._name == 'body_html' else 'utf8'

            if file_name:
                self._filename = os.path.join(DocumentApi.working_path, file_name)
                self._buffer = open(self._filename, 'rt', encoding=encoding) if is_text else io.FileIO(self._filename, 'rb')
                self._size = os.stat(self._filename).st_size
            else:
                # make the inline blob act as a file
                self._size = len(inline_blob)
                self._buffer = io.TextIOWrapper(io.BytesIO(inline_blob), encoding=encoding, errors='ignore') if is_text else io.BytesIO(inline_blob)

        def close(self):
            super(ApiV1.ReadOnlyDataStream, self).close()
            self._buffer.close()

        def readable(self):
            return True

        def read(self, n=-1):
            return self._buffer.read(n)

        def readlines(self, hint=-1):
            return self._buffer.readlines(hint)

        def readline(self, size=-1):
            return self._buffer.readline(size)

        def readinto(self, b):
            self._buffer.readinto(b)

        def writable(self):
            return False

        def seekable(self):
            return True

        def seek(self, offset, whence=0):
            return self._buffer.seek(offset, whence)

        @property
        def name(self):
            return self._name

        @property
        def origin(self):
            return self._origin

        @property
        def size(self):
            return self._size

        @property
        def filename(self):
            return self._filename

        def _to_json(self):
            """
            The ReadOnlyDataStream as json

            :return: dict
            """
            return {'Origin': self._origin,
                    'Name': self._name}

    class DataStream(io.RawIOBase):
        def __init__(self, name, binary=True, use_file=True):
            """
            Data stream that we can write to

            :param str name: stream name
            :param bool binary: whether to open the stream in binary mode
            :param bool use_file: whether to save the stream on disk or keep it in ram
            """
            super(ApiV1.DataStream, self).__init__()
            self._name = name.lower()
            self._filename = None
            self._origin = None
            self._is_text = name.lower() in TEXT_STREAMS or not binary

            encoding = 'utf-16le' if name.lower() in UTF16_STREAMS else 'utf-8-sig' if self._name == 'body_html' else 'utf8'

            if use_file:
                self._filename = str(uuid.uuid4())
                self._buffer = open(os.path.join(DocumentApi.working_path, self._filename), 'wt+', encoding=encoding, newline='\n') if self._is_text else io.FileIO(os.path.join(DocumentApi.working_path, self._filename), 'wb+')
            else:
                self._buffer = io.TextIOWrapper(io.BytesIO(), encoding=encoding, errors='ignore', newline='\n') if self._is_text else io.BytesIO()

        def close(self):
            super(ApiV1.DataStream, self).close()
            self._buffer.close()

        def readable(self):
            return True

        def read(self, n=-1):
            return self._buffer.read(n)

        def readlines(self, hint=-1):
            return self._buffer.readlines(hint)

        def readline(self, size=-1):
            return self._buffer.readline(size)

        def writable(self):
            return True

        def write(self, b):
            if self._is_text:
                return self._buffer.write(b.decode(errors='ignore') if type(b) is bytes else b)
            return self._buffer.write(b.encode('utf8') if type(b) is str else b)

        def writelines(self, lines):
            def convert_lines(lns):
                # make sure all written lines end with a \n
                for l in lns:
                    line = l.decode(errors='ignore') if self._is_text and type(l) is bytes else l
                    if self._is_text:
                        yield line if line.endswith('\n') else line + '\n'
                    else:
                        yield line if line.endswith(b'\n') else line + b'\n'

            self._buffer.writelines(convert_lines(lines))

        def flush(self):
            self._buffer.flush()

        def seekable(self):
            return True

        def seek(self, offset, whence=0):
            return self._buffer.seek(offset, whence)

        def clear(self):
            """
            Will clear the content of the stream
            """
            # resize the stream to 0 bytes
            self._buffer.truncate(0)
            self._buffer.flush()
            self._buffer.seek(0)

        def _to_json(self):
            """
            The DataStream as json

            :return: dict
            """
            return {'Origin': self._origin,
                    'Name': self._name}

        @property
        def name(self):
            return self._name

        @property
        def id(self):
            return self._filename

        @property
        def filename(self):
            return self._filename

        @property
        def origin(self):
            return self._origin

        @origin.setter
        def origin(self, value):
            self._origin = value

        @property
        def inline(self):
            if not self._filename:
                self._buffer.seek(0)
                # read from the buffer directly of the TextIOWrapper to have the binary representation when stream is inlined text
                return self._buffer.buffer.read() if type(self._buffer) is io.TextIOWrapper else self._buffer.read()

    class MetaDataValue(object):
        def __init__(self, origin, values):
            """
            A meta data and its values

            :param str origin: the origin of the meta data
            :param dict[str, list[str]] values: the meta data values
            """
            self._origin = origin.lower()
            self._values = CaseInsensitiveDict(values or {})

        @property
        def origin(self):
            """
            The origin of the meta: crawler, converter etc
            """
            return self._origin

        def _to_json(self):
            """
            The MetaDataValue as json

            :return: dict
            """
            return {'Origin': self._origin,
                    'Values': self._values}

        @property
        def values(self):
            """
            A dict of values: {'meta_name':['value1', 'value2']}
            """
            return self._values

        @classmethod
        def from_json(cls, json_):
            return cls(json_.get('Origin', ''),
                       json_.get('Values', None))

    class Permission(object):
        def __init__(self, identity, identity_type, security_provider, additional_info=None):
            """
            A single permission.

            :param str identity: the identity
            :param str identity_type: the identity type
            :param str security_provider: the security provider
            :param dict[str, str] additional_info: additional info
            """
            self.identity = identity
            self.identity_type = identity_type.lower() if identity_type.lower() in PERMISSION_IDENTITY_TYPE else 'unknown'
            self.security_provider = security_provider
            self.additional_info = additional_info or {}

        def _to_json(self):
            """
            The Permission as json

            :return: dict
            """
            return {'Identity': self.identity,
                    'IdentityType': self.identity_type,
                    'SecurityProvider': self.security_provider,
                    'AdditionalInfo': self.additional_info}

        @classmethod
        def from_json(cls, json_):
            return cls(json_.get('Identity', ''),
                       json_.get('IdentityType', ''),
                       json_.get('SecurityProvider', ''),
                       json_.get('AdditionalInfo', None))

    class PermissionSet(object):
        def __init__(self, name='', allow_anonymous=False, allowed_permissions=None, denied_permissions=None):
            """
            A collection of allowed and denied permissions.
            :param str name: the set name
            :param bool allow_anonymous: whether anonymous is allowed
            :param list[Permission] allowed_permissions: the allowed
            :param list[Permission] denied_permissions: the denied
            "
            """
            self.name = name
            self.allow_anonymous = allow_anonymous
            self.allowed_permissions = allowed_permissions or []
            self.denied_permissions = denied_permissions or []

        def _to_json(self):
            """
            The PermissionSet as json

            :return: dict
            """
            return {'Name': self.name,
                    'AllowAnonymous': self.allow_anonymous,
                    'AllowedPermissions': self.allowed_permissions,
                    'DeniedPermissions': self.denied_permissions}

        @classmethod
        def from_json(cls, json_):
            return cls(json_.get('Name', ''),
                       json_.get('AllowAnonymous', False),
                       [ApiV1.Permission.from_json(allowed) for allowed in json_.get('AllowedPermissions', [])],
                       [ApiV1.Permission.from_json(denied) for denied in json_.get('DeniedPermissions', [])])

    class PermissionLevel(object):
        def __init__(self, name='', permission_sets=None):
            """
            A level of permission where multiple permission sets can be specified.

            :param str name: the level name
            :param list[ApiV1.PermissionSet] permission_sets: the permissions set for this level
            """
            self.name = name
            self.permission_sets = permission_sets or []

        def _to_json(self):
            """
            The PermissionLevel as json

            :return: dict
            """
            return {'Name': self.name,
                    'PermissionSets': self.permission_sets}

        @classmethod
        def from_json(cls, json_):
            return cls(json_.get('Name', ''),
                       [ApiV1.PermissionSet.from_json(permission_set) for permission_set in json_.get('PermissionSets', [])])

    class Result(object):
        def __init__(self, meta_data, permissions, streams, log_entries, rejected, reject_reason):
            """
            The result of the script execution
            """
            self.meta_data = meta_data
            self.permissions = permissions
            self.streams = streams
            self.log_entries = log_entries
            self.rejected = rejected
            self.reject_reason = reject_reason

