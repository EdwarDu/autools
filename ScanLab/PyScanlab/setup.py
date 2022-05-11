from setuptools import setup
from setuptools.extension import Extension
import Cython
from Cython.Build import cythonize
from Cython.Compiler import Options

Options.covert_range = True

__FAKE_DEV = True

if not __FAKE_DEV:
    ext_modules = [
        Extension('pyscanlab.rtc6_sdk', 
                  ["cython/rtc6_sdk.pyx", ],
                  language = "c++",
                  libraries=["RTC6DLLx64", ],
                  library_dirs=['python3/pyscanlab/lib/',],
                  include_dirs=['python3/pyscanlab/inc/',]
                  ),
    ]
    pack_files = ['lib/*.dll', 'data/*']
else:
    ext_modules = [
        Extension('pyscanlab.rtc6_sdk',
                  ["cython/rtc6_sdk.pyx", "cython/rtc6_fake_dev.cpp"],
                  language = "c++",
                  libraries=[],
                  library_dirs=['python3/pyscanlab/lib/',],
                  include_dirs=['python3/pyscanlab/inc/',]
                  ),
    ]
    pack_files = ['lib/*.dll', 'data/*']

for e in ext_modules:
    e.cython_directives = {'language_level': "3"}

setup(
    name='pyscanlab',
    version='0.0.1',
    cmdclass={'build_ext': Cython.Build.build_ext},
    ext_modules=ext_modules,
    packages=['pyscanlab',],
    package_dir={'pyscanlab': 'python3/pyscanlab'},
    package_data={'pyscanlab': pack_files},
    include_package_data = True,
)
