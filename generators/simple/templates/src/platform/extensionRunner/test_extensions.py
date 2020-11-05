from extension_runner_standalone import run_extension
from util import get_html_content
from util import zlib_compress_str
import unittest
import os

def run_set_locale(document):
    my_dir = os.path.dirname(__file__)
    return run_extension(document,
                     os.path.join(my_dir, '../extensions/set_locale.py'),
                     ('params', os.path.join(my_dir, '../extensions/parameters/empty.json')))

def run_extract_product_info(document):
    my_dir = os.path.dirname(__file__)
    return run_extension(document,
                    os.path.join(my_dir, '../extensions/extract_product_info.py'),
                    ('params', os.path.join(my_dir, '../extensions/parameters/empty.json')))

def run_reject_document(document):
    my_dir = os.path.dirname(__file__)
    return run_extension(document,
                    os.path.join(my_dir, '../extensions/reject_document.py'),
                    ('exclusion_rules', os.path.join(my_dir, '../extensions/parameters/exclusion_rules.json')))

def generate_doc(url): 
    html_content = get_html_content(url)
    blob = zlib_compress_str(html_content)
    doc = {
        'Document': {
            'Id': url,
            'MetaData':[{
                'Value':{},
                'Origin':'Crawler'
            }],
            'DataStreams': {
                'DocumentData': [{
                    'Value': {
                        'InlineBlob': blob,
                        'Compression': 'ZLib'
                    },
                    'Origin': 'Crawler'
                }]
            }
        }
    }
    return doc

class TestExtractProductInfo(unittest.TestCase):

    def test_extract_product_info(self):
        url = 'https://www2.hm.com/en_ca/productpage.0763763001.html'
        url2 = 'https://www2.hm.com/en_ca/productpage.0821336001.html'

        # test no.1
        new_result = run_extract_product_info(generate_doc(url))
        print('log entries: {}\n'.format(new_result.log_entries))

        assert 'product_info' in new_result.meta_data

        # test no.2
        new_result = run_extract_product_info(generate_doc(url2))
        print('log entries: {}\n'.format(new_result.log_entries))

        assert 'product_info' in new_result.meta_data

if __name__ == '__main__':
    unittest.main()

