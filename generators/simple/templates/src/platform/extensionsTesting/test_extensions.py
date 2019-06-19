from util import run_extension
import unittest
import os

def run_set_locale(document):
    my_dir = os.path.dirname(__file__)
    return run_extension(document,
                     os.path.join(my_dir, '../extensions/set_locale.py'),
                     ('params', os.path.join(my_dir, '../extensions/parameters/empty.json')))

def run_reject_document(document):
    my_dir = os.path.dirname(__file__)
    return run_extension(document,
                    os.path.join(my_dir, '../extensions/reject_document.py'),
                    ('exclusion_rules', os.path.join(my_dir, '../extensions/parameters/exclusion_rules.json')))

class TestSetLocale(unittest.TestCase):
    
    def test_set_locale_for_support_community(self):
        # support community doc
        doc = {'Id': 'https://support.customer.com/s/self-service-request?language=es_MX'}

        new_result = run_set_locale(doc)
        # print('\nlog entries: {}'.format(new_result.log_entries))
        assert new_result.meta_data['locale.lang_code'] == ['es']
        assert new_result.meta_data['locale.country_code'] == ['mx']
        assert new_result.meta_data['locale.culture_code'] == ['es_mx']
        assert new_result.meta_data['locale.language'] == ['Spanish']
    
    def test_set_locale_for_kb(self):
        # kb doc
        kb_doc = {
            'Id': 'http://www.salesforce.com/org:organization/articletype:EXT_Issues/article:kA50x000000CbTUCA0/language:en_US',
            'Kav_Language': ['en_US']
        }
        new_result = run_set_locale(kb_doc)
        # print('\nlog entries: {}'.format(new_result.log_entries))
        assert new_result.meta_data['locale.lang_code'] == ['en']
        assert new_result.meta_data['locale.country_code'] == ['us']
        assert new_result.meta_data['locale.culture_code'] == ['en_us']
        assert new_result.meta_data['locale.language'] == ['English']

    def test_set_locale_for_youtube(self):
        # youtube doc
        yt_doc = {
            'Id': 'https://www.youtube.com/watch?v=cECgaMPdZOU',
            'coveo_tags': ['fr_CA']
        }
        new_result = run_set_locale(yt_doc)
        # print('\nlog entries: {}'.format(new_result.log_entries))
        assert new_result.meta_data['locale.lang_code'] == ['fr']
        assert new_result.meta_data['locale.country_code'] == ['ca']
        assert new_result.meta_data['locale.culture_code'] == ['fr_ca']
        assert new_result.meta_data['locale.language'] == ['French'] 
        
    def test_set_locale_for_dummy(self):
        # dummy doc 
        dummy_doc = {'Id': 'https://dummy.doc.com'}
        new_result = run_set_locale(dummy_doc)
        # print('\nlog entries: {}'.format(new_result.log_entries))
        assert 'locale.lang_code' not in new_result.meta_data
        assert 'locale.country_code' not in new_result.meta_data
        assert 'locale.culture_code' not in new_result.meta_data
        assert 'locale.language' not in new_result.meta_data

class TestRejectDocument(unittest.TestCase):

    def test_reject_document(self):
        # matching exclusion rules
        new_result = run_reject_document({'Id': 'https://support.customer.com/s/article/this-is-a-nice-article'})
        # print('log entries: {}\n'.format(new_result.log_entries))
        assert new_result.rejected == True

        new_result = run_reject_document({'Id': 'https://support.customer.com/s/article'})
        # print('log entries: {}\n'.format(new_result.log_entries))
        assert new_result.rejected == True

        new_result = run_reject_document({'Id': 'https://support.customer.com/s/LiveChat?language=en_US'})
        # print('log entries: {}\n'.format(new_result.log_entries))
        assert new_result.rejected == True

        new_result = run_reject_document({'Id': 'https://support.customer.com/s/contactsupport?language=en_US'})
        # print('log entries: {}\n'.format(new_result.log_entries))
        assert new_result.rejected == True

        # not matching exclusion rules
        new_result = run_reject_document({'Id': 'https://support.customer.com/s/something-else'})
        # print('log entries: {}\n'.format(new_result.log_entries))
        assert new_result.rejected == False

if __name__ == '__main__':
    unittest.main()

