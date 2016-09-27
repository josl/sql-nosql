#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of SQL_NOSQL.
# https://github.com/josl/SQL_NOSQL

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Jose L. Bellod Cisneros <bellod.cisneros@gmail.com>

from setuptools import setup, find_packages
from SQL_NOSQL import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='SQL_NOSQL',
    version=__version__,
    description='WEEK 05 of 02807 COMPUTATIONAL TOOLS FOR BIG DATA: SQL AND NOSQL',
    long_description='''
        WEEK 05 of 02807 COMPUTATIONAL TOOLS FOR BIG DATA: SQL AND NOSQL
    ''',
    keywords='sql, nosql, databases',
    author='Jose L. Bellod Cisneros',
    author_email='bellod.cisneros@gmail.com',
    url='https://github.com/josl/SQL_NOSQL',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        # add your dependencies here
        'pymongo>=3.1.1<3.2'
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'SQL&NOSQL=SQL&NOSQL.cli:main',
        ],
    },
)
