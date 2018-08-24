#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

__version__ = '1.0.2'
__author__ = 'Agus Makmun (Summon Agus)'
__author_email__ = 'summon.agus@gmail.com'

setup(
    name="changewords",
    packages=['changewords'],
    version=__version__,
    platforms=['Linux'],
    url='https://github.com/agusmakmun/changewords/',
    download_url='https://github.com/agusmakmun/changewords/tarball/v%s' % __version__,
    description="Python tool to change or replace the text string in the files.",
    long_description=open("README.rst").read(),
    license='MIT',
    author=__author__,
    author_email=__author_email__,
    keywords=['change words', 'word replacer', 'python tool'],
    entry_points={
        'console_scripts': ['changewords=changewords.changewords:main', ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Software Development'
    ]
)
