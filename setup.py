#!/bin/env python2
# -*- coding: utf-8 -*-
# Copyright (c) 2015, Viagenie inc.
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, is not permitted.

# This software is provided ``as is'' and any
# Express or implied warranties, including, but not limited to, the implied
# Warranties of merchantability and fitness for a particular purpose are
# Disclaimed. In no event shall the regents and contributors be liable for any
# Direct, indirect, incidental, special, exemplary, or consequential damages
# (including, but not limited to, procurement of substitute goods or services;
# Loss of use, data, or profits; or business interruption) however caused and on
# Any theory of liability, whether in contract, strict liability, or tort
# (including negligence or otherwise) arising in any way out of the use of this
# Software, even if advised of the possibility of such damage.
from setuptools import setup, find_packages

setup(
    name="munidata",
    version='1.2',
    description="Provides an API for accessing multiple instances of Unicode data",
    license="TBD",
    author='Viagenie and Wil Tan',
    author_email='support@viagenie.ca',
    install_requires=["picu"],
    packages=find_packages(),
    long_description=open('README.md').read(),
    scripts=['tools/parse_idna_tables.py'],
    classifiers=[
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Programming Language :: Python :: 2.7',
                'Topic :: Software Development :: Libraries'
    ]
)
