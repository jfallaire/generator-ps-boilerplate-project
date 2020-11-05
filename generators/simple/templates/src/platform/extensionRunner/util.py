import os
import json
import tempfile
import zlib
import base64
import urllib.request

def zlib_compress_str(content):
    outdata = zlib.compress(content, zlib.Z_BEST_COMPRESSION)
    encodedData = base64.encodebytes(outdata)
    #print('zlib compressed >>> {}'.format(encodedData))
    return encodedData


def get_html_content(url):
    hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    req = urllib.request.Request(url, headers=hdr)

    try:
        with urllib.request.urlopen(req) as response:
            return response.read()

    except Exception as e:
        print(e)
        return ''
