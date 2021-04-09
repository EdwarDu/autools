# This is the entry point to setup_j
import os
import platform
import sys
import subprocess

project_root = os.path.dirname(os.path.realpath(__file__))
# Change working directory to project root
os.chdir(project_root)

# Git to update
ans = input("Launch `git pull` to sync? [y/N]")
if ans.lower().startswith("y"):
    os.system("git pull")

# Go up to parent folder
os.chdir("..")
if platform.system() == "Windows":
    python3_path = os.path.join(".", "env_j", "python.exe")
else:
    python3_path = subprocess.check_output(['which', 'python3']).decode('utf8').strip()

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

# Launch the app
os.system(f"{python3_path} -m autools.setup_j.setup_main_window")
