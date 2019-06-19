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