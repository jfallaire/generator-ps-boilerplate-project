import os
import json
import tempfile

from extension_runner_standalone import execute_script

def run_extension(document, script_file, params_file):
    # create a temp file for the document
    try:
        document_file = tempfile.mkstemp()
        os.write(document_file[0], json.dumps(document))
        os.close(document_file[0])

        return execute_script(document_file[1], script_file, params_file)
    finally:
        os.remove(document_file[1])
