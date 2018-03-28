#!/usr/bin/ python3
# -*- coding: utf-8 -*-

import os
from setuptools import find_packages, setup


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()


setup(name="tabular-print",
      version="1.0.6a1",
      description="Lightweight, tabular data, printing module for Python.",
      long_description=README,
      author="Michael Kitzan",
      author_email="mkitzan45@gmail.com",
      url="https://github.com/mkitzan/tabular-print",
      license="MIT",
      packages=find_packages(),
      keywords="tabular-data sqlite3 python data table",
      classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 3 - Alpha",
        "Topic :: Database",
        "Topic :: Scientific/Engineering :: Visualization",
        ],
     )


