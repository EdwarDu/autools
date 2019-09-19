from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup(
    ext_modules=cythonize([Extension("andor_sdk3", ["andor_sdk3.pyx"],
                                     libraries=["atcorem"])
                           ], compiler_directives={'language_level': 3})
)

# setup(
#     ext_modules=cythonize("andor_sdk3.pyx", compiler_directives={'language_level': 3})
# )
