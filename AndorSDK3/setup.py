import os
from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize
from Cython.Compiler import Options

Options.covert_range = True

__FAKE_DEV = False

if not __FAKE_DEV:
    if os.name == "nt":
        extensions = [
            Extension('andor_sdk3', 
                      ["andor_sdk3.pyx", ],
                      libraries=["atcorem", ],
                      library_dirs=['WIN/', ],
                      include_dirs=['WIN/', ],
            ),
        ]
    else:
        extensions = [
            Extension('andor_sdk3', 
                      ["andor_sdk3.pyx", ],
                      libraries=["atcore", ],
                      library_dirs=['LINUX/x86_64', ],
                      include_dirs=['LINUX/inc', ],
            ),
        ]

    setup(
        ext_modules=cythonize(extensions, compiler_directives={'language_level': 3})
    )
else:
    extensions = [
        Extension("andor_sdk3",
                  ["andor_sdk3.pyx", "atcore_fake_dev.cpp"],
                  include_dirs=["./LINUX/inc", ]),
    ]
    setup(
        ext_modules=cythonize(extensions, compiler_directives={'language_level': 3})
    )
