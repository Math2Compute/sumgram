#!/usr/bin/env python

from setuptools import setup, find_packages
from sumgram import __version__

long_description = open('README.md').read()
desc = """sumgram is a tool that summarizes a collection of text documents by generating the most frequent sumgrams (multiple ngrams)"""


setup(
    name='sumgram',
    version=__version__,
    description=desc,
    long_description=long_description,
    author='Alexander C. Nwala',
    author_email='anwala@cs.odu.edu',
    url='https://github.com/oduwsdl/sumgram/',
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        'numpy',
        'requests',
        'sklearn'
    ],
    entry_points={'console_scripts': ['sumgram = sumgram.sumgram:main']}
)