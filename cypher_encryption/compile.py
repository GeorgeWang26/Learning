from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("wrapper", ["wrapper.py"])
]

for e in ext_modules:
    e.cython_directives = {'language_level': "3"} # all are Python-3

setup(
    name = 'test_encryption_with_compile',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
