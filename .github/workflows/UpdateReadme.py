import os
import sys
import subprocess

github_env = os.environ['GITHUB_ENV']
result = subprocess.run(['la -l'], shell=True, capture_output=True, text=True, cwd=sys.argv[1]).stdout

print(result)
print (f'github env {github_env}')