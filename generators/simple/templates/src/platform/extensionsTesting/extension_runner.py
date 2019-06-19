# coding=utf-8

"""
 Will run an Indexing Pipeline Extension script on a document
"""

# make sure that your python version is newer than 2.7.9 otherwise you may have ssl error

# Uncomment those lines in order to attach the debugger
#import ctypes, sys, os
#ctypes.windll.user32.MessageBoxA(0, 'Attach debugger to process {}'.format(os.getpid()), 'Debug', 0)

import io
import uuid
import codecs
import collections
import os
import json

PERMISSION_IDENTITY_TYPE = {
    'user',
    'group',
    'virtualgroup',
    'unknown'
}

UTF16_STREAMS = {'body_text'}


def _get_encoder(name, stream):
    """
    will wrapped stream into an encoder/decoder when the stream is known to be in utf16

    :param str name: the name of the stream
    :param BytesIO stream: the stream
    :return:
    """
    if name.lower() in UTF16_STREAMS:
        return codecs.EncodedFile(stream, 'utf-8', 'utf-16le', 'replace')
    else:
        return stream


# noinspection PyPep8Naming,PyPep8
class CaseInsensitiveDict(dict):
    @classmethod
    def _k(cls, key):
        # noinspection PyUnresolvedReferences
        return key.lower() if isinstance(key, basestring) else key

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

    def has_key(self, key):
        return super(CaseInsensitiveDict, self).has_key(self.__class__._k(key))

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

    # noinspection PyUnusedLocal
    def log(self, id_, message, severity='normal'):
        self._api_v1.log(message, severity)

    # noinspection PyUnusedLocal
    def get_meta_data(self, id_):
        return self._api_v1.get_meta_data()

    # noinspection PyUnusedLocal
    def add_meta_data(self, id_, meta_data):
        self._api_v1.add_meta_data(meta_data)


class ApiV1(object):
    # noinspection PyProtectedMember
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
            self._document_state.log_entries.append((message, severity))

    def get_meta_data(self):
        """
        get the current meta data on the document

        :return: list[MetaDataValue]
        """
        return self._document_state.current_meta_data + [ApiV1.MetaDataValue(self._document_state.origin, {k: v}) for k, v in self._document_state.meta_data_to_add.iteritems()]

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

    def add_meta_data(self, meta_data):
        """
        add meta data to the document

        :param dict[str, str|list[str|Object]] meta_data: the meta data to add to the document
        """
        for k, v in meta_data.iteritems():
            if isinstance(v, collections.Iterable) and not isinstance(v, basestring):
                self._document_state.meta_data_to_add[k.lower()] = [val if val is not None else '' for val in v]
            else:
                self._document_state.meta_data_to_add[k.lower()] = [v if v is not None else '']

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
        if isinstance(permission_levels, collections.Iterable):
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

    def reject(self):
        """
        will set the document as rejected
        """
        self._document_state.reject_document = True

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
                'DataStream': self.get_data_streams(),
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
            super(ApiV1.JsonEncoder, self).__init__(kwargs)

        def default(self, o):
            """
            Will encode to json and object

            :param o: the object to encode
            :return: the json for that object
            """
            if isinstance(o, (ApiV1, ApiV1.MetaDataValue, ApiV1.PermissionLevel, ApiV1.PermissionSet,
                              ApiV1.Permission, ApiV1.ReadOnlyDataStream, ApiV1.DataStream)):
                return o._to_json()

            return super(ApiV1.JsonEncoder, self).default(o)

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
                                self.reject_document)

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
        def __init__(self, name, origin, blob_id, inline_blob):
            """
            A read-only data stream

            :param str name: stream name
            :param str origin: stream origin
            :param str blob_id: the id in the blobstore
            :param str inline_blob: the content of the blob when inline

            """
            super(ApiV1.ReadOnlyDataStream, self).__init__()
            self._name = name.lower()
            self._origin = origin.lower()
            self._filename = None

            if blob_id:
                self._filename = os.path.join(DocumentApi.working_path, blob_id)
                self._size = os.stat(self._filename).st_size
                self._buffer = io.FileIO(self._filename, 'r+b')
            else:
                # make the inline blob act as a file
                self._size = len(inline_blob)
                self._buffer = io.BytesIO(inline_blob)

            self._encoder = _get_encoder(self._name, self._buffer)

        def close(self):
            super(ApiV1.ReadOnlyDataStream, self).close()
            self._encoder.close()

        def readable(self):
            return True

        def read(self, n=-1):
            return self._encoder.read(n)

        def writable(self):
            return False

        def seekable(self):
            return True

        def seek(self, offset, whence=0):
            return self._encoder.seek(offset, whence)

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
        def __init__(self, name, use_file=True):
            """
            Data stream that we can write to

            :param str name: stream name
            :param bool use_file: whether to save the stream on disk or keep it in ram
            """
            super(ApiV1.DataStream, self).__init__()
            self._name = name.lower()
            self._filename = None
            self._origin = None

            # html must have an utf-8 bom
            self._write_bom = self._name == 'body_html'

            if use_file:
                self._filename = str(uuid.uuid4())
                self._buffer = io.FileIO(os.path.join(DocumentApi.working_path, self._filename), 'wb')
            else:
                self._buffer = io.BytesIO()

            self._encoder = _get_encoder(self._name, self._buffer)

        def close(self):
            super(ApiV1.DataStream, self).close()
            self._encoder.close()

        def readable(self):
            return True

        def read(self, n=-1):
            return self._buffer.read(n)

        def writable(self):
            return True

        def write(self, b):
            if self._write_bom:
                self._write_bom = False
                self._encoder.write('\xEF\xBB\xBF')
            
            return self._encoder.write(b.encode('utf-8') if type(b) is unicode else b)

        def flush(self):
            self._encoder.flush()

        def seekable(self):
            return True

        def seek(self, offset, whence=0):
            return self._encoder.seek(offset, whence)

        def clear(self):
            """
            Will clear the content of the stream
            """
            # set whether or not we'll have to write the bom on the next write operation
            self._write_bom = self._name == 'body_html'

            # resize the stream to 0 bytes
            self._encoder.truncate(0)
            self._encoder.flush()
            self._encoder.seek(0)

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
        def origin(self):
            return self._origin

        @origin.setter
        def origin(self, value):
            self._origin = value

        @property
        def inline(self):
            if not self._filename:
                self._buffer.seek(0)
                return self._buffer.read()

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
        def __init__(self, meta_data, permissions, streams, log_entries, rejected):
            """
            The result of the script execution

            :param meta_data:
            :param list[PermissionLevel] permissions: the new document permissions
            :param list|dict streams: the streams to add
            :param list[(str, str)] log_entries: the log entries to add to the log
            :param bool rejected: whether the document is rejected
            """
            self.meta_data = meta_data
            self.permissions = permissions
            self.streams = streams
            self.log_entries = log_entries
            self.rejected = rejected
