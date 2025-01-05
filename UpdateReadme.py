import os
import subprocess

for root, dirs, files in os.walk("."):
    for file in files:
        print(f'file {os.path.join(root, file)}')

result = subprocess.run(['git', 'tag'], shell=True, capture_output=True, text=True).stdout

print(result)