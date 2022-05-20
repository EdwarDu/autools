__all__ = ['RTC6Helper', "rtc6_sdk"]

import os
import re

if os.name == "nt":
    env_var_name = 'PATH'
    sub_path = 'lib'
else:
    env_var_name = 'LD_LIBRARY_PATH'
    sub_path = 'lib'

if env_var_name not in os.environ.keys():
    os.environ[env_var_name] = ""

_lst_path = re.split(os.pathsep, os.environ[env_var_name])
_dll_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), sub_path)
if _dll_path not in _lst_path:
    os.environ[env_var_name] = os.environ.get(env_var_name) + os.pathsep + _dll_path

__CFG_PATH__ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

# allow raw function call to rtc6 (too many functions to handle in the python3 with wrapper for now)
from pyscanlab import rtc6_sdk
from pyscanlab.rtc6_sdk import RTC6Helper
