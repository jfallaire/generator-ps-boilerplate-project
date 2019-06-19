# coding=utf-8

"""
 standalone extension runner used to debug a script
"""

from extension_runner import *
import json
import argparse
import base64
import zlib

# noinspection PyShadowingNames
def execute_script(document_file, script_file, params_file):
    """
    execute a script a on document

    :param str document_file: name of the file that contains the document
    :param str script_file: name of the file that contains the script
    :return: extension_runner.ApiV1.Result
    """
    # load the files
    with open(document_file, 'rt') as d:
        document_and_config = json.loads(d.read())

        # document may be from a AllMetadataValues script and not really one exported from the DPM
        if 'Document' in document_and_config:
            document = document_and_config['Document']

            # keep only meta/streams from crawler
            document['DataStreams'] = {k:v for k,v in document['DataStreams'].items() if v[0]['Origin'] == 'Crawler'}
            document['MetaData'] = [m for m in document['MetaData'] if m['Origin'] == 'Crawler']
        else:
            document = {'MetaData': [{'Values': {k.split(':')[0]:v for k,v in document_and_config.iteritems()}}]}
            document['Id'] = document_and_config.get('Id', 'Unknown')

    with open(script_file, 'rt') as s:
        script = s.read()

    parameters = {}
    if params_file:
        with open(params_file[1], 'rt') as p:
            parameters[params_file[0]] = p.read().replace('\\"', '\"')

    # compile the script
    compiled_code = compile(script, script_file, 'exec')

    # prepare the script environment
    current_streams = []
    for name, streams in document.get('DataStreams', {}).iteritems():
        for stream in streams:
            value = stream.get('Value')
            if value:
                if value.get('Compression') == 'ZLib' and 'InlineBlob' in value:
                    uncompressed_buffer = zlib.decompress(base64.b64decode(value.get('InlineBlob', '')))
                else:
                    uncompressed_buffer = str(value.get('InlineBlob', ''))

                current_streams.append(ApiV1.ReadOnlyDataStream(name, stream.get('Origin', ''),
                                                                value.get('Id', ''),
                                                                uncompressed_buffer))

    document_state = ApiV1.DocumentState(document.get('Id', 'unknown'),
                                         [ApiV1.MetaDataValue.from_json(meta) for meta in document.get('MetaData', [])],
                                         [ApiV1.PermissionLevel.from_json(level) for level in document.get('Permissions', [])],
                                         current_streams,
                                         'standalone')
    document_api = DocumentApi(document_state)
    script_locals = {'__name__': '__main__',
                     'document_api': document_api,
                     'document': document_api.v1,
                     'log': document_api.v1.log,
                     'parameters': parameters}

    # run it
    try:
        exec compiled_code in script_locals, script_locals
    finally:
        document_state.close_streams()

        # close DataStreams that were created but not added
        for s in script_locals.itervalues():
            if type(s) is ApiV1.DataStream and not s.closed:
                s.close()

    return document_state.result


if __name__ == '__main__':
    # setup the valid args
    parser = argparse.ArgumentParser(description='Standalone extension runner')
    parser.add_argument('-document', '-d', required=True, help='filename of the input document')
    parser.add_argument('-script', '-s', required=True, help='filename of the script to apply to the document')
    parser.add_argument('-params', '-p', required=True, help='filename of the paramters file')

    args = parser.parse_args()

    # run the script
    result = execute_script(args.document, args.script, args.params)

    # output the result
    print('\nnew meta: {}\n'.format(result.meta_data))
    print('new datastreams: {}\n'.format([(s.name, s.id if s.id else s.inline) for s in result.streams]))
    print('new allowed: {}\n'.format([(a.identity, a.security_provider) for l in result.permissions for s in l.permission_sets for a in s.allowed_permissions]))
    print('new denied: {}\n'.format([(d.identity, d.security_provider) for l in result.permissions for s in l.permission_sets for d in s.denied_permissions]))
    print('log entries: {}\n'.format(result.log_entries))

#
# In order to have type completion in PyCharm, add those two lines to your script
#
# document = document
# """:type: extension_runner.ApiV1"""
#
