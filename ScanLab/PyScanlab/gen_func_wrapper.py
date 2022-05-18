#!/usr/bin/env python3

import os
import sys
import re

rtc6_func_re = re.compile(r"RTC6_API (?P<return_type>[\w\d]+) __stdcall (?P<func_name>[\w\d]+)\((?P<arg_list>.*)\);")
arg_re = re.compile(r"(?P<arg_type>[\w\*& \d]+)\s+(?P<arg_name>[\w\d]+)")

if os.path.exists(sys.argv[2]):
    print(f"{sys.argv[2]} exists, will not override", file=sys.stderr)
    exit(1)

with open(sys.argv[1], 'r') as f_header, open(sys.argv[2], 'w') as f_wrapper, open(sys.argv[2]+".pxd", 'w') as f_pxd:
    print(f'#include <{os.path.basename(sys.argv[1])}>', file=f_wrapper)

    print("""#define UNUSED(x) /*Empty*/""", file=f_wrapper)

    func_map = {}

    for line in f_header:
        func_match = rtc6_func_re.match(line.strip())
        if func_match is not None:
            arg_list = func_match.group('arg_list')
            func_ret_type = func_match.group('return_type')
            func_name=func_match.group('func_name')
            func_map[func_name]=(func_ret_type, arg_list)

    for func_name in [x for x in func_map.keys() if not x.startswith("n_")]:
        arg_list = func_map[func_name][1].strip()
        ret_type = func_map[func_name][0]
        if ("n_" + func_name) in func_map.keys():
            print(f"inline {ret_type} _{func_name} "
                  f"(int cardno {','+arg_list if arg_list != '' and arg_list != 'void' else ''}) {{", file=f_wrapper)
            print(f"  if (cardno == -1) {{ return {func_name}(", end= '', file=f_wrapper)
            if arg_list != "" and arg_list != "void":
                i = 0
                for arg in [x.strip() for x in re.split(",", arg_list)]:
                    arg_match = arg_re.match(arg)
                    arg_type = arg_match.group('arg_type')
                    arg_name = arg_match.group('arg_name')
                    if i == 0:
                        print(f"{arg_name}", end='', file=f_wrapper)
                    else:
                        print(f",{arg_name}", end='', file=f_wrapper)
                    i += 1
            print(f");}}", file=f_wrapper)
            print(f"  else {{ return n_{func_name} (static_cast<UINT>(cardno)", end= '', file=f_wrapper)
            if arg_list.strip() != "" and arg_list.strip() != "void":
                for arg in [x.strip() for x in re.split(",", arg_list)]:
                    arg_match = arg_re.match(arg)
                    arg_type = arg_match.group('arg_type')
                    arg_name = arg_match.group('arg_name')
                    print(f",{arg_name}", end='', file=f_wrapper)
            print(f");}}", file=f_wrapper)
            print(f"}}", file=f_wrapper)
        else:
            print(f"inline {ret_type} _{func_name} "
                  f"(int UNUSED(cardno) {','+arg_list if arg_list != '' and arg_list != 'void' else ''}) {{", file=f_wrapper)
            print(f" return {func_name} (", end= '', file=f_wrapper)
            if arg_list != "" and arg_list != "void":
                i = 0
                for arg in [x.strip() for x in re.split(",", arg_list)]:
                    arg_match = arg_re.match(arg)
                    arg_type = arg_match.group('arg_type')
                    arg_name = arg_match.group('arg_name')
                    if i == 0:
                        print(f"{arg_name}", end='', file=f_wrapper)
                    else:
                        print(f",{arg_name}", end='', file=f_wrapper)
                    i += 1
            print(f");", file=f_wrapper)
            print(f"}}", file=f_wrapper)

        print(f"cdef extern {ret_type} __stdcall _{func_name} "
              f"(int cardno{', '+arg_list if arg_list != '' and arg_list != 'void' else ''})", file=f_pxd)

