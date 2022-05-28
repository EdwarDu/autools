import os
import platform
import sys
import subprocess
import shutil

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
        ans = input(f"Input the python3.exe path:")
    python3_path = ans

os.chdir(os.path.join(os.popen("git rev-parse --show-toplevel").read().strip(), ".."))
os.system(f"{python3_path} -m autools.Cameras.AndorCameraMan")

