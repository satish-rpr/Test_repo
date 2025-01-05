import os
import sys
import subprocess


result = subprocess.run(['git tag'], shell=True, capture_output=True, text=True, cwd=sys.argv[1]).stdout

print(result)