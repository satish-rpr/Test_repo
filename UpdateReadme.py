import os
import subporcess

for root, dirs, files in os.walk("."):
    for file in files:
        print(f'file {os.path.join(root, file)}')

result = subprocess.run(['git', 'tag']).decode('utf-8')

print(result.splitlines())