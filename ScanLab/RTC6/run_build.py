# This is the entry point to setup_j
import os
import platform
import sys
import subprocess
import shutil

project_root = os.path.dirname(os.path.realpath(__file__))
# Change working directory to project root
os.chdir(project_root)

# Git to update
ans = input("Launch `git pull` to sync? [y/N]")
if ans.lower().startswith("y"):
    os.system("git pull")

python3_path = sys.executable # shutil.which('python')

if os.path.exists(python3_path):
    ans = input(f"Found {python3_path}, use? [Y/n]")
    if ans.lower().startswith("n"):
        python3_path = None
else:
    python3_path = None

if python3_path is None:
    ans = ""
    while not os.path.exists(ans):
        ans = input(f"Input the python3.exe path to launch the setup_j app:")
    python3_path = ans

os.system(f"{python3_path} setup.py build_ext -i")

ans = input("If there is no error message, want to launch run.py to test the package? [y/N]")

if ans.lower().startswith("y"):
    os.system(f"{python3_path} run.py")


