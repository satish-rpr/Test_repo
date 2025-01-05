import os
import subprocess

result = subprocess.run(['ls -l'], shell=True, capture_output=True, text=True, cwd='../../').stdout

print(result)