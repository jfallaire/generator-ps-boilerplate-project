import os
import sys
import argparse

print(sys.argv)
dir_path = os.path.dirname(os.path.realpath(__file__))

if __name__ == '__main__':
  # setup the valid args
  parser = argparse.ArgumentParser(description='Run extension')
  parser.add_argument('-script', required=True, help='filename of the script to apply to the document')
  parser.add_argument('-urihash', required=True, help='the uri hash of the document to get the extensions for')
  args = parser.parse_args()

  cmd = f"python3 {dir_path}/extension_runner_standalone.py -script {args.script} -urihash {args.urihash} -orgid {os.environ['COVEO_ORG_ID']} -token {os.environ['COVEO_API_KEY']}"

  print(cmd)
  os.system(cmd)
