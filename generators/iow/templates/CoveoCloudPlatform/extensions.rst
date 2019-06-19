**********
Extensions
**********

This section contains information about Indexing Pipeline extensions as of April 2019.

.. contents:: Contents
    :local:
    :backlinks: entry

.. _reject_document:

reject_document
===============

.. admonition:: Goal

    * Reject document based on exclusion rules

.. code-block:: python

    import re
    import json

    def reject_document(uri, exclusion_rules):
        try:
            rejectFlag = False
            reg_lst = []
            for raw_regex in exclusion_rules:
                reg_lst.append(re.compile(raw_regex))
            if any(compiled_reg.match(uri) for compiled_reg in reg_lst):
                log('rejecting document: [' + uri + ']')
                rejectFlag = True
            return rejectFlag
        except Exception as e:
            log(str(e))
            return False

    if reject_document(document.uri, json.loads(parameters.get('exclusion_rules', '[]'))):
        document.reject()

.. _set_locale:

set_locale
==========

.. admonition:: Goal

    * This extension will add metadata value such as countryCode and langCode

.. code-block:: python

    import re

    langcode_to_language = {'en': 'English',
                            'fr': 'French',
                            'es': 'Spanish',
                            'de': 'German',
                            'it': 'Italian',
                            'ja': 'Japanese',
                            'zh': 'Chinese',
                            'ru': 'Russian',
                            'ko': 'Korean',
                            'pt': 'Portuguese'}


    def extract_locale_info(uri):
        locale_info_regex = r"(language|lang)?[=:]?([a-zA-Z]{2})_([a-zA-Z]{2})?"
        locale_info = {}
        log('input param >>> {}'.format(uri))
        if uri :
            m = re.search(locale_info_regex, uri)
            if m : 
                lang_code = (m.group(2) or '').lower()
                country_code = (m.group(3) or '').lower()
                locale_info = {
                    "locale.culture_code": '{}_{}'.format(lang_code, country_code),
                    "locale.lang_code": '{}'.format(lang_code),
                    "locale.country_code": '{}'.format(country_code),
                    "locale.language": langcode_to_language.get(lang_code, '')
                }
        log('locale_info >>> {}'.format(locale_info))
        return locale_info

    def get_safe_meta_data(meta_data_name):
        safe_meta = ''
        meta_data_value = document.get_meta_data_value(meta_data_name)
        if len(meta_data_value) > 0:
            safe_meta = meta_data_value[-1]
        return safe_meta

    try:
        locale_info = extract_locale_info(get_safe_meta_data('coveo_tags') or get_safe_meta_data('kav_language') or document.uri)
        document.add_meta_data(locale_info)

    except Exception as e:
        log(str(e))



.. _allmetadatavalues:

allmetadatavalues
=================

.. admonition:: Goal

    * Extraction of all metadata values on document

.. caution:: this extension should only be used for debugging purposes otherwise it might have an impact on indexing performances. Please avoid activating this in production.

.. code-block:: python

    import json
    values = dict()
    for m in document.get_meta_data():
        for metadata_name, metadata_value in m.values.iteritems():
            values[metadata_name] = metadata_value
    document.add_meta_data({"allmetadatavalues": json.dumps(values)})

