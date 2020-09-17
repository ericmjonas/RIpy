
from setuptools import setup,Extension
from Cython.Build import cythonize

sourcefiles = ['riwrapper.pyx', 'ritest.cc']

extensions = [Extension("riwrapper", sourcefiles,
                        include_dirs=['include', 'rilib'],
                        language="c++",
                        extra_compile_args=["-O3"])]


setup(
    ext_modules = cythonize(extensions)
)


