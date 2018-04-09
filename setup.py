#!/bin/env python2
# -*- coding: utf-8 -*-
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
