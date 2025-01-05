import os
import sys
import subprocess

repo_workspace = os.environ['GITHUB_WORKSPACE']
repo_ref = os.environ['GITHUB_REF']

print(f"repo_workspace: {repo_workspace}")
print(f"repo_ref: {repo_ref}")