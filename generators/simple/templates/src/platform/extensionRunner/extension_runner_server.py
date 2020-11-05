# coding=utf-8

"""
 python 3 version of the extension runner hosted with flask
"""
import pathlib
import datetime
import marshal
import os
import base64
import sys
import site
import traceback
import subprocess
import uuid
import logging
import re
import shlex
import gc
from typing import Dict, List

from extension_runner import *

from cdf.document_definition import LocalBlobEntry, CompressionType, PermissionLevel, PermissionSet, Permission, MetaDataValue, DataStreamValue
from cdf.document_processor_script import ScriptExecutionResult, LogEntry, PythonScriptException, PythonPackageException, ScriptPackage, DocumentProcessorScriptParameters, RejectedFromScriptException, ScriptSkippedException
from cdf.logger import LogEntry, SeverityType

import json as native_json
try:
    import rapidjson as _json
except ImportError:
    import json as _json
    

LOG_SEVERITY = {
    'fatal': 'Fatal',
    'error': 'Error',
    'important': 'Important',
    'normal': 'Normal',
    'debug': 'Debug',
    'notification': 'Notification',
    'warning': 'Warning',
    'detail': 'Detail'
}

IDENTITY_TYPES = {
    'user': 'User',
    'group': 'Group',
    'virtual_group': 'VirtualGroup',
    'virtualgroup': 'VirtualGroup',
    'unknown': 'Unknown'
}


class ExtensionRunner(object):
    """
    Will delegate execution of a python script to user code
    """

    def __init__(self, debug=False):
        super().__init__()
        self._debug = debug
        self._package_re = re.compile('([\w-]+)(?:[=~<>]+)?(.*)')
        self._last_document_state = None

        # hook the logging to the node log file
        self._log = logging.getLogger('system')
        self._log.setLevel(logging.INFO)

    def init_blade(self, parameters: Dict[str, str]):
        """
        Called to pass init parameters
        """
        if 'DataPath' in parameters:
            DocumentApi.working_path = parameters['DataPath']

    def compile(self, script_id: str, code: str) -> bytes:
        """
        will compile the code
        """
        if self._debug:
            # Don't compile the script in debug since we'll save it to disk later in order to trace it
            return base64.b64encode(b'').decode()
        else:
            return base64.b64encode(marshal.dumps(self._compile(code, '${FILENAME}'))).decode()

    def prepare_packages(self, packages: List[str], working_path: str, merge: bool) -> List[ScriptPackage]:
        """
        will prepare the packages
        """
        try:
            installed_into = []
            if merge:
                # installed packages in the same folder
                installed_into.append(self._pip_install(packages, working_path))
            else:
                # install each package in its own folder
                for p in packages:
                    installed_into.append(self._pip_install([p], working_path))

            return installed_into

        except Exception as e:
            raise PythonPackageException(what=str(e))

    def _pip_install(self, packages: List[str], working_path: str) -> ScriptPackage:
        """
        will install one or more packages into a folder
        """
        PIP_INSTALL_COMMAND_LINE = 'pip install {packages} -b "{build}" --prefix "{install}" --cache-dir "{cache}" --ignore-installed --compile'
        PIP_FREEZE_COMMAND_LINE = 'pip freeze'

        # create our working sub-folders
        build_folder = os.path.join(working_path, str(uuid.uuid4()))
        install_folder = os.path.join(working_path, str(uuid.uuid4()))
        temp_folder = os.path.join(working_path, str(uuid.uuid4()))
        cache_path = os.path.join(working_path, str(uuid.uuid4()))
        os.makedirs(build_folder)
        os.makedirs(install_folder)
        os.makedirs(temp_folder)
        os.makedirs(cache_path)

        # some packages will access the temp path while installing
        env = os.environ
        env['TEMP'] = temp_folder
        env['TMP'] = temp_folder

        # spawn the installation
        pip_install = subprocess.Popen(shlex.split(PIP_INSTALL_COMMAND_LINE.format(packages=' '.join(packages), build=build_folder, install=install_folder, cache=cache_path)),
                                       shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
        out, err = pip_install.communicate()
        if pip_install.returncode != 0:
            raise PythonPackageException(what=err.decode())

        # figure out where the package has been installed
        site_package_path = ''
        try:
            site_package_path = next(d[0] for d in os.walk(install_folder) if d[0].endswith('site-packages'))
        except StopIteration:
            pass

        # figure out the version of the packages we've just installed with pip freeze
        env['PYTHONPATH'] = site_package_path
        pip_freeze = subprocess.Popen(shlex.split(PIP_FREEZE_COMMAND_LINE),
                                      shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
        out, err = pip_freeze.communicate()
        if pip_freeze.returncode != 0:
            raise PythonPackageException(what=err.decode())

        all_installed_packages = {self._get_package_name(p): self._get_package_version(p) for p in out.decode().split()}

        # package name will contain its version as well
        # package that are merged together will end up with a merged name
        package = ScriptPackage()
        package.location = site_package_path
        package.name = ','.join(['{}=={}'.format(*z) for z in zip([self._get_package_name(p) for p in packages], [all_installed_packages[self._get_package_name(p)] for p in packages])])

        return package

    def get_last_log_entries(self) -> List[LogEntry]:
        """
        will get the log entries for the last script execution
        """
        if self._last_document_state:
            return self._last_document_state.get_log_entries()
        else:
            return []

    def execute(self, parameters: DocumentProcessorScriptParameters, id_: str, meta_data: List[MetaDataValue], meta_data_file: str, permissions: List[PermissionLevel], data_streams: Dict[str, DataStreamValue], package_paths: List[str]):
        """
        will the execute the extension
        """

        # compile or use the already compiled code
        delete_temp_file = False
        compiled_code = None
        filename = parameters.script_id
        if parameters.compiled_code:
            compiled_code = marshal.loads(base64.b64decode(parameters.compiled_code))
        elif parameters.code:
            if self._debug:
                import tempfile
                delete_temp_file = True
                filename = tempfile.mktemp(suffix='.py')
                with open(filename, 'wt', encoding='utf-8') as tmp_file:
                    tmp_file.write(parameters.code)

            compiled_code = self._compile(parameters.code, filename if self._debug else '${FILENAME}')

        elif pathlib.Path(filename).exists():
            with open(filename, encoding='utf8') as source_file:
                compiled_code = self._compile(source_file.read(), filename if self._debug else '${FILENAME}')

        if not compiled_code:
            raise PythonScriptException(what='Either compiled_code or code need to be populated in parameters')

        system_log_entries = []

        # load the meta from disk if needed
        if meta_data_file:
            try:
                with open(os.path.join(DocumentApi.working_path, meta_data_file), 'r') as mf:
                    meta_data = [ApiV1.MetaDataValue(m.get('Origin', ''), m.get('Values', {})) for m in _json.load(mf)]

            except Exception as e:
                system_log_entries.append(LogEntry(comment=u'rapidjson: {}'.format(e),
                                                   date=int(datetime.datetime.now().timestamp()),
                                                   severity=SeverityType.Error))

                # rapidjson cannot load the file, will retry with the native json
                with open(os.path.join(DocumentApi.working_path, meta_data_file), 'r') as mf:
                    meta_data = [ApiV1.MetaDataValue(m.get('Origin', ''), m.get('Values', {})) for m in native_json.load(mf)]
        else:
            meta_data = [ApiV1.MetaDataValue(mm.origin, mm.values) for mm in meta_data]

        document_state = _DocumentState(id_,
                                        meta_data,
                                        permissions,
                                        data_streams,
                                        parameters.name)
        self._last_document_state = document_state

        document_api = DocumentApi(document_state)

        # inject package folders in path & site
        old_path = list(sys.path)
        for p in package_paths:
            # addsitedir will add the folder to the end of sys.path
            # but we need them at the beginning of the list but not a position 0 since it's the script name
            sys.path.insert(1, p)
            site.addsitedir(p)

        script_globals = {'__name__': '__main__',
                          'sys': sys,
                          'script': document_api.legacy,
                          'document_api': document_api,
                          'document': document_api.v1,
                          'log': document_api.v1.log,
                          'parameters': parameters.values or {}}

        try:
            exec(compiled_code, script_globals)

            result = document_state.result

            if result.rejected:
                # someone did "except Exception" silencing the RejectedException, re-throw it
                raise RejectedException(document_state.reject_reason)

            return ScriptExecutionResult(meta_data=result.meta_data,
                                         permissions=result.permissions,
                                         data_streams=result.streams,
                                         log_entries=result.log_entries,
                                         system_log_entries=system_log_entries)
        except RejectedException as e:
            raise RejectedFromScriptException(what=str(e))
        except SkippedException as e:
            raise ScriptSkippedException(what=str(e))
        except BaseException:
            raise PythonScriptException(what=self._get_traceback(filename))
        finally:
            if delete_temp_file:
                try:
                    os.remove(filename)
                except OSError:
                    pass

            sys.path = list(old_path)

            # clean up the data_streams
            document_state.close_streams()

            # close DataStreams that were created but not added
            for s in script_globals.values():
                if type(s) is ApiV1.DataStream and not s.closed:
                    s.close()

            # clean up local objects that were passed to the extension in order to avoid leaks since those objects are somehow still referenced from the exec() step
            to_delete = [k for k in script_globals.keys()]
            for d in to_delete:
                del script_globals[d]

            gc.collect()

    def _compile(self, code, filename):
        try:
            return compile(code, filename, 'exec')
        except Exception:
            raise PythonScriptException(what=self._get_traceback(filename))

    def _get_traceback(self, filename):
        body_frames = self._replace_filename(filename, traceback.format_list(traceback.extract_tb(sys.exc_info()[2])[1:]))
        exception_frames = traceback.format_exception_only(sys.exc_info()[0], sys.exc_info()[1])

        # Make sure we deal with SyntaxError correctly, it adds the filename in the first frame
        if len(exception_frames) > 1:
            exception_frames = self._replace_filename(filename, exception_frames[:1]) + exception_frames[1:]
            
        frames = ['Traceback (most recent call last):\n'] + \
            body_frames + \
            exception_frames
        return ''.join(frames)

    def _replace_filename(self, filename, frame_list):
        filename = filename or '<string>'
        return [frame.replace('${FILENAME}', filename) for frame in frame_list]

    def _get_package_name(self, package):
        """
        will get a package name without the version

        :param package: package name with optional version
        :return: the package name
        """
        # according to https://packaging.python.org/tutorials/installing-packages/#id17
        # 'SomeProject' 'SomeProject==1.4' 'SomeProject>=1,<2' 'SomeProject~=1.4.2'
        return self._package_re.search(package).group(1)

    def _get_package_version(self, package):
        """
        will get a package version

        :param package: package name with mandatory version
        :return: the package version
        """
        return self._package_re.search(package).group(2)


class _DocumentState(ApiV1.DocumentState):
    def __init__(self, document_id, meta_data, permissions, streams, origin):
        """
        convert the streams from the wrapped C++ to more manageable ones
        """
        current_streams = []
        for name, streams in streams.items():
            for s in streams:
                current_streams.append(ApiV1.ReadOnlyDataStream(name,
                                                                s.origin,
                                                                s.value.file_name,
                                                                base64.b64decode(s.value.inline_blob)))

        super(_DocumentState, self).__init__(document_id,
                                             meta_data,
                                             [ApiV1.PermissionLevel(l.name, [ApiV1.PermissionSet(s.name,
                                                                                                 s.allow_anonymous,
                                                                                                 [ApiV1.Permission(a.identity, a.identity_type.name, a.security_provider, {k: v for k, v in a.additional_info.items()} if a.additional_info else {}) for a in s.allowed_permissions] if s.allowed_permissions else [],
                                                                                                 [ApiV1.Permission(d.identity, d.identity_type.name, d.security_provider, {k: v for k, v in d.additional_info.items()} if d.additional_info else {}) for d in s.denied_permissions] if s.denied_permissions else []) for s in l.permission_sets]) for l in permissions],
                                             current_streams,
                                             origin)

    @property
    def result(self):
        """
        get the result of the script execution

        :return: ApiV1.Result
        """
        return ApiV1.Result(self.meta_data_to_add,
                            self._get_final_permissions(),
                            self._get_streams_to_add(),
                            self.get_log_entries(),
                            self.reject_document,
                            self.reject_reason)

    def _get_streams_to_add(self):
        to_add = {}
        for stream in self.streams_to_add:
            if stream.filename:
                # blob in a file
                to_add[stream.name] = LocalBlobEntry(file_name=stream.filename,
                                                     compression=CompressionType['Uncompressed'])
            else:
                # inline blob
                to_add[stream.name] = LocalBlobEntry(inline_blob=base64.b64encode(stream.inline),
                                                     compression=CompressionType['Uncompressed'])

        return to_add

    def get_log_entries(self):
        return [LogEntry(comment=log_entry[0],
                         date=int(datetime.datetime.now().timestamp()),
                         duration=0,
                         fields={},
                         severity=LOG_SEVERITY.get(log_entry[1].lower(), 'Normal')) for log_entry in self.log_entries]

    def _get_final_permissions(self):
        def convert_permission(permission):
            return Permission(
                identity=permission.identity,
                identity_type=IDENTITY_TYPES.get(permission.identity_type.lower(), 'Unknown'),
                security_provider=permission.security_provider,
                additional_info={k: v for k, v in permission.additional_info.items()}
            )

        # Convert back to Permissions

        final_permissions = []
        for level in self.final_permissions:
            # level
            final_level = PermissionLevel(
                name=level.name,
                permission_sets=[]
            )
            for permission_set in level.permission_sets:
                # set
                final_set = PermissionSet(
                    name=permission_set.name,
                    allow_anonymous=permission_set.allow_anonymous,
                    allowed_permissions=[convert_permission(a) for a in permission_set.allowed_permissions],
                    denied_permissions=[convert_permission(d) for d in permission_set.denied_permissions]
                )

                final_level.permission_sets.append(final_set)

            final_permissions.append(final_level)

        return final_permissions
