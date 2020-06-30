# -*- coding: utf-8 -*-

from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(name='prime',
      ext_modules=cythonize(Extension("prime", language='c', sources=['prime.pyx'])
      ))
# python setup.py build_ext --inplace
# cython -a prime.pyx
