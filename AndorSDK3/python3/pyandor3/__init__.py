__all__ = ['Andor3Man', ]

import os 
import re

if os.name == "nt":
    env_var_name = 'PATH'
    sub_path = os.path.join('lib', 'WIN')
else:
    env_var_name = 'LD_LIBRARY_PATH'
    sub_path = os.path.join('lib', 'LINUX/x86_64')

if env_var_name not in os.environ.keys():
    os.environ[env_var_name] = ""

_lst_path = re.split(os.pathsep, os.environ[env_var_name])
_dll_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), sub_path)
if _dll_path not in _lst_path:
    os.environ[env_var_name] = os.environ.get(env_var_name) + os.pathsep + _dll_path

from pyandor3.andor_sdk3 import Andor3Man
