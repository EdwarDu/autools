#!/usr/bin/env python3

import os
import sys
import re

rtc6_func_re = re.compile(r"RTC6_API (?P<return_type>[\w\d]+) __stdcall (?P<func_name>[\w\d]+)\((?P<arg_list>.*)\);")
arg_re = re.compile(r"(?P<arg_type>[\w\*& \d]+)\s+(?P<arg_name>[\w\d]+)")

if os.path.exists(sys.argv[2]):
    print(f"{sys.argv[2]} exists, will not override", file=sys.stderr)
    exit(1)

with open(sys.argv[1], 'r') as f_header, open(sys.argv[2], 'w') as f_fake:
    print(f'#include "{sys.argv[1]}"', file=f_fake)
    print(f'#include <iostream>', file=f_fake)
    print(f'using namespace std;', file=f_fake)
    for line in f_header:
        func_match =  rtc6_func_re.match(line.strip())
        if func_match is not None:
            func_name=func_match.group('func_name')
            func_ret_type = func_match.group('return_type')
            print(f"Getting {func_name} ...", file=sys.stderr)
            print(line.replace(";", "{"), end='', file=f_fake)
            print("  // auto-gen dummy impl of function", file=f_fake)
            arg_list = func_match.group('arg_list')
            print('  cout << __FUNCTION__ << " called" << ', end='', file=f_fake)
            if arg_list.strip() != "" and arg_list.strip() != "void":
                for arg in [x.strip() for x in re.split(",", arg_list)]:
                    arg_match = arg_re.match(arg)
                    arg_type = arg_match.group('arg_type')
                    arg_name = arg_match.group('arg_name')
                    print(f"    {arg_name} ---> {arg_type}", file=sys.stderr)
                    print(f"\"{arg_name} = \" << {arg_name} << ", end='', file=f_fake)
            print('endl;', file=f_fake)
            if func_ret_type == 'void':
                print("  return;", file=f_fake)
            elif func_ret_type == 'long':
                print("  return 0L;", file=f_fake)
            elif func_ret_type == 'double':
                print("  return 0.0;", file=f_fake)
            elif func_ret_type == 'UINT':
                print("  return 0;", file=f_fake)
            else:
                raise NotImplemented(f"Unhandled return type {func_ret_type}")
            print("}", file=f_fake)
            print("", file=f_fake)

