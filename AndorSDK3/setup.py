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
            Extension('andor_sdk3', ["andor_sdk3.pyx", ],
                       libraries=["atcorem", ]),
        ]
    else:
        extensions = [
            Extension('andor_sdk3', ["andor_sdk3.pyx", ],
                       libraries=["atcore", ]),
        ]

    setup(
        ext_modules=cythonize(extensions, compiler_directives={'language_level': 3})
    )
else:
    extensions = [
        Extension("andor_sdk3", ["andor_sdk3.pyx", "atcore_fake_dev.cpp"],
                  include_dirs=["./", ]),
    ]
    setup(
        ext_modules=cythonize(extensions, compiler_directives={'language_level': 3})
    )
