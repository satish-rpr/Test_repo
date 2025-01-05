import os
import subprocess

result = subprocess.run(['git tag'], shell=True, capture_output=True, text=True).stdout

print(result)