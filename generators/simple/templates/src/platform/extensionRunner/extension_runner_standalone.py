# coding=utf-8
"""
 standalone extension runner used to run and debug an extension
"""
import json
import argparse
import base64
import zlib
from urllib.parse import urlparse
import requests
import pathlib
from collections import defaultdict
from typing import List

from extension_runner_server import ExtensionRunner
from cdf.root.serializer import JidEncoder
from cdf.root.deserializer import deserialize
from cdf.document_processor_script import DocumentProcessorScriptParameters
from cdf.document_definition import MetaDataValue, LocalBlobEntry, DataStreamValue


def get_script_parameters(session, env, org_id, script_file, source_id):
    """ will get the parameters for a script on a given source"""

    try:
        organization_id, extension_id = pathlib.Path(script_file).stem.split('-')
    except Exception:
        extension_id = pathlib.Path(script_file).stem
        organization_id = org_id
    
    extension_id = '{}-{}'.format(organization_id, extension_id[:extension_id.find('_v3')] if '_v3' in extension_id else extension_id)

    parameters = DocumentProcessorScriptParameters(script_id=script_file, name=extension_id)

    # fetch the parameters for this extension
    resp = session.get(f'https://platform{env}.cloud.coveo.com/rest/organizations/{organization_id}/sources/{source_id}/raw')
    if resp.ok:
        def get_params(pipeline):
            for p in pipeline:
                if p['extensionId'] == extension_id:
                    return p['parameters']

        json_resp = resp.json()
        if 'MAPPING_EXTENSION' in script_file:
            parameters.values = {'mappings': json.dumps(json_resp['mappings'])}
        else:
            parameters.values = get_params(json_resp['preConversionExtensions']) or get_params(json_resp['postConversionExtensions'])

    return parameters


def get_document(session, env, organization_id, query, load_from_field_name, load_from_stream_name, query_pipeline, meta_from_file):
    """ will load the extension and document"""
    origin_to_consider = {'crawler', 'converter', 'mapping'}

    def figure_out_meta(meta):
        """ will figure out the format of the meta """
        try:
            return deserialize(meta.json(), List[MetaDataValue])
        except:
            # simple key/value (may include origin)
            meta_by_origin = defaultdict(defaultdict)
            for k, v in meta.items():
                origin = 'crawler'
                value = v
                if ':' in k:
                    name, origin = k.split(':')
                    if origin not in origin_to_consider:
                        continue
                else:
                    name = k

                meta_by_origin[origin][name] = v

            return list(reversed([MetaDataValue(origin=k, values=v) for k, v in meta_by_origin.items()]))

    # load the document from a query result
    resp = session.post(f'https://platform{env}.cloud.coveo.com/rest/search/v2?organizationId={organization_id}&pipeline={query_pipeline}', data=json.dumps({'q': query}))

    # fill meta from the query result or from the given field or stream
    if resp.ok:
        meta_data = None
        content = resp.json()['results']
        if content:
            unique_id = content[0]["uniqueId"]
            result_meta = resp.json()['results'][0]['raw']

            # get the source id according to its name
            resp = session.get(f'https://platform{env}.cloud.coveo.com/rest/organizations/{organization_id}/sources/')
            if resp.ok:
                source_id = next(s['id'] for s in resp.json() if s['name'] == content[0]['raw']['source'])
            else:
                raise Exception(f'cannot get source id: {resp.reason}')

            if load_from_stream_name:
                resp = session.get(f'https://platform{env}.cloud.coveo.com/rest/search/v2/datastream?uniqueId={unique_id}&organizationId={organization_id}&dataStream={load_from_stream_name}')
                if resp.ok:
                    try:
                        meta_data = figure_out_meta(resp.json())
                    except Exception:
                        pass

            if not meta_data:
                if load_from_field_name and load_from_field_name in result_meta:
                    try:
                        meta_data = figure_out_meta(json.loads(result_meta[load_from_field_name]))
                    except Exception:
                        pass

            if not meta_data:
                meta_data = [MetaDataValue(origin='Crawler',
                                           values={})]
                for k, v in result_meta.items():
                    if not k.startswith('sys'):
                        meta_data[0].values[k] = v if type(v) is list else [v]

        else:
            raise Exception('document not found in index')

    else:
        raise Exception(resp.reason)

    # replace with the meta we've loaded from the file
    if meta_from_file:
        def erase_meta_from_origin(origin_):
            for m in meta_data:
                if m.origin == origin_:
                    meta_data.remove(m)
                    break

        for m in meta_from_file:
            origin = m['Origin']
            if origin.lower() in origin_to_consider:
                erase_meta_from_origin(origin)
                meta_data.append(MetaDataValue(origin=origin, values=m['Values']))

    return unique_id, source_id, meta_data


def get_data_streams(session, env, unique_id, document_uri, script_file, streams_from_file):
    """ load the streams needed by the script """
    
    data_streams = {}
    
    with open(script_file, 'rt') as s:
        script_code_lower = s.read().lower()

    if 'body_text' in script_code_lower:
        if 'Body_Text' in streams_from_file and 'InlineBlob' in streams_from_file['Body_Text'][0]['Value']:
            data_streams['Body_Text'] = [DataStreamValue(origin='Crawler',
                                                         value=LocalBlobEntry(compression='Uncompressed',
                                                                              inline_blob=base64.b64encode(zlib.decompress(base64.b64decode(streams_from_file['Body_Text'][0]['Value']['InlineBlob'])))))]
        else:
            resp = session.get(f'https://platform{env}.cloud.coveo.com/rest/search/v2/text?uniqueId={unique_id}&organizationId={organization_id}')
            if resp.ok:
                data_streams['Body_Text'] = [DataStreamValue(origin='Crawler',
                                                             value=LocalBlobEntry(compression='Uncompressed',
                                                                                  inline_blob=base64.b64encode(resp.json()['content'].encode('utf-16le'))))]

    if 'body_html' in script_code_lower:
        if 'Body_HTML' in streams_from_file and 'InlineBlob' in streams_from_file['Body_HTML'][0]['Value']:
            data_streams['Body_HTML'] = [DataStreamValue(origin='Crawler',
                                                         value=LocalBlobEntry(compression='Uncompressed',
                                                                              inline_blob=base64.b64encode(zlib.decompress(base64.b64decode(streams_from_file['Body_HTML'][0]['Value']['InlineBlob'])))))]
        else:
            resp = session.get(f'https://platform{env}.cloud.coveo.com/rest/search/v2/html?uniqueId={unique_id}&organizationId={organization_id}')
            if resp.ok:
                data_streams['Body_HTML'] = [DataStreamValue(origin='Crawler',
                                                             value=LocalBlobEntry(compression='Uncompressed',
                                                                                  inline_blob=base64.b64encode(resp.content.decode().encode())))]

    if 'documentdata' in script_code_lower:
        if 'DocumentData' in streams_from_file and 'InlineBlob' in streams_from_file['DocumentData'][0]['Value']:
            data_streams['DocumentData'] = [DataStreamValue(origin='Crawler',
                                                         value=LocalBlobEntry(compression='Uncompressed',
                                                                              inline_blob=base64.b64encode(zlib.decompress(base64.b64decode(streams_from_file['DocumentData'][0]['Value']['InlineBlob'])))))]
        elif urlparse(document_uri).scheme == 'https':
            resp = requests.get(document_uri, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'})
            if resp.ok:
                data_streams['documentdata'] = [DataStreamValue(origin='Crawler',
                                                                value=LocalBlobEntry(compression='Uncompressed',
                                                                                     inline_blob=base64.b64encode(resp.content)))]
    return data_streams


def run_extension(document, extension_filename, parameters):
    """ will run an extension on a document """

    data_streams = {}
    streams_from_file = {}
    document = document['Document']
    streams_from_file = document.get('DataStreams', {})
    meta_from_file = document.get('MetaData', {})

    # setup the meta data
    meta_data = [MetaDataValue(origin='Crawler',
                               values={})]
    for k, v in meta_from_file[0]['Value'].items():
        meta_data[0].values[k] = v if type(v) is list else [v]

    if 'DocumentData' in streams_from_file and 'InlineBlob' in streams_from_file['DocumentData'][0]['Value']:
        data_streams['DocumentData'] = [DataStreamValue(origin='Crawler',
                                                        value=LocalBlobEntry(compression='Uncompressed',
                                                                             inline_blob=base64.b64encode(zlib.decompress(base64.b64decode(streams_from_file['DocumentData'][0]['Value']['InlineBlob'])))))]
    # get the document URI from the meta Id
    document_uri = ''
    if 'Id' in document:
        document_uri = document['Id']

    # setup the params
    script_parameters = DocumentProcessorScriptParameters(script_id=extension_filename, name=pathlib.Path(extension_filename).stem)
    if parameters:
        with open(parameters[1]) as param_file:
            script_parameters.values = {parameters[0]: param_file.read()}

    # run the extension
    extension_runner = ExtensionRunner(debug=True)
    return extension_runner.execute(script_parameters,
                                    document_uri,
                                    meta_data,
                                     '',
                                     [],
                                     data_streams,
                                     [])


if __name__ == '__main__':
    # setup the valid args
    parser = argparse.ArgumentParser(description='Standalone extension runner')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-uri', help='uri of the document to get from index')
    group.add_argument('-urihash', help='the uri hash of the document to get the extensions for')
    parser.add_argument('-script', required=True, nargs='+', help='filename of the script to apply to the document')
    parser.add_argument('-token', required=True, help='the authorization token to connect to the platform')
    parser.add_argument('-field', required=False, help='get the meta from that field, ex: allmetadatavalues')
    parser.add_argument('-stream', required=False, help='get the meta from that stream, ex: allmetadatavalues')
    parser.add_argument('-env', required=False, default='', help='dev, qa or empty for prod')
    parser.add_argument('-pipeline', dest='pipeline', required=False, default='default', help='the query pipeline')
    parser.add_argument('-json_file', required=False, default='', help='will load the document meta from a json file')
    parser.add_argument('-orgid', required=False, help='the org id')
    args = parser.parse_args()

    scripts = args.script if type(args.script) else [args.script]
    organization_id = args.orgid or pathlib.Path(scripts[0]).stem.split('-')[0]

    # load the document from the optional json file
    meta_from_file = []
    streams_from_file = {}
    if args.json_file:
        with open(args.json_file) as json_file:
            json_doc = json.load(json_file)
            if 'Document' in json_doc:
                meta_from_file = json_doc['Document'].get('MetaData', [])
                streams_from_file = json_doc['Document'].get('DataStreams', {})

    session = requests.session()
    session.headers.update({'content-type': 'application/json', 'Authorization': f'Bearer {args.token}'})

    query = f'@uri=={args.uri}' if args.uri else f'@urihash=={args.urihash}'
    unique_id, source_id, meta_data = get_document(session, args.env, organization_id, query, args.field, args.stream, args.pipeline, meta_from_file)

    document_uri = unique_id[unique_id.find('$') + 1:]
    extension_runner = ExtensionRunner(debug=True)

    for script in scripts:
        data_streams = get_data_streams(session, args.env, unique_id, document_uri, script, streams_from_file)
        script_parameters = get_script_parameters(session, args.env, organization_id, script, source_id)

        try:
            result = extension_runner.execute(script_parameters,
                                              document_uri,
                                              meta_data,
                                              '',
                                              [],
                                              data_streams,
                                              [])
            print(f'Success {script_parameters.name}: {json.dumps(result, cls=JidEncoder, indent=4)}')

            # update the document with new meta and streams
            meta_data.append(MetaDataValue(origin=script_parameters.name,
                                           values=result.meta_data))
            if result.data_streams:
                pass

        except Exception as e:
            print(f'Exception {script_parameters.name}: {json.dumps(e, cls=JidEncoder, indent=4,check_circular=False)}')
            print(f'Logs: {json.dumps(extension_runner.get_last_log_entries(), cls=JidEncoder, indent=4)}')





#
# In order to have type completion in PyCharm, add those two lines to your script
#
# document = document
# """:type: extension_runner_27.ApiV1"""
#
