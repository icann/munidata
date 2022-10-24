#!/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from io import open

setup(
    name="munidata",
    version='2.2.0',
    description="Provides an API for accessing multiple instances of Unicode data",
    license="TBD",
    author='Viagenie and Wil Tan',
    author_email='support@viagenie.ca',
    install_requires=["picu"],
    packages=find_packages(),
    long_description=open('README.md', encoding='utf-8').read(),
    scripts=['tools/parse_idna_tables.py'],
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ]
)
