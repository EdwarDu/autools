from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Compiler import Options

Options.covert_range = True

__FAKE_DEV = False

if not __FAKE_DEV:
    extensions = [
        Extension('rtc6_sdk', ["rtc6_sdk.pyx", ],
                  libraries=["RTC6DLLx64", ]),
    ]

    setup(
        ext_modules=cythonize(extensions, compiler_directives={'language_level': 3})
    )
else:
    extensions = [
        Extension("rtc6_sdk", ["rtc6_sdk.pyx", "rtc6_fake_dev.cpp"],
                  include_dirs=["./", ]),
    ]
    setup(
        ext_modules=cythonize(extensions, compiler_directives={'language_level': 3})
    )

