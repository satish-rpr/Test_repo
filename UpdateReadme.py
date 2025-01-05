import os

for root, dirs, files in os.walk("."):
    for file in files:
        print(f'file {os.path.join(root, file)}')