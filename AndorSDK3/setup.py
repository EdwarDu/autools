import os
import glob
from setuptools import setup
from setuptools.extension import Extension
import Cython
from Cython.Build import cythonize
from Cython.Compiler import Options

Options.covert_range = True

__FAKE_DEV = False

this_dir = os.path.dirname(os.path.abspath(__file__))

if not __FAKE_DEV:
    if os.name == "nt":
        ext_modules = [
            Extension('pyandor3.andor_sdk3', 
                      ["cython/andor_sdk3.pyx",],
                      libraries=["atcorem", ],
                      library_dirs=['python3/pyandor3/lib/WIN/', ],
                      include_dirs=['python3/pyandor3/inc/WIN/', ],
            ),
        ]
        lib_files =  ['lib/WIN/*.dll', ]
    else:
        ext_modules = [
            Extension('pyandor3.andor_sdk3', 
                      ["cython/andor_sdk3.pyx",],
                      libraries=["atcore", ],
                      library_dirs=['python3/pyandor3/lib/LINUX/x86_64', ],
                      include_dirs=['python3/pyandor3/inc/LINUX/', ],
            ),
        ]
        lib_files = ['lib/LINUX/x86_64/*', ]

else:
    ext_modules = [
        Extension("pyandor3.andor_sdk3",
                  ["cython/andor_sdk3.pyx", "cython/atcore_fake_dev.cpp"],
                  include_dirs=["python3/pyandor3/inc/LINUX/", ]),
    ]
    lib_files=["",]

for e in ext_modules:
    e.cython_directives = {'language_level': "3"}

setup(
    name='pyandor3',
    version="0.0.1",
    cmdclass={'build_ext': Cython.Build.build_ext},
    ext_modules=ext_modules,
    packages=['pyandor3',],
    package_dir={'pyandor3': 'python3/pyandor3'},
    package_data={'pyandor3': lib_files},
    include_package_data = True,
)

