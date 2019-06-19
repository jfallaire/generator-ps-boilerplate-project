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

