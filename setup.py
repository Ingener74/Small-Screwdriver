#!/usr/bin/env python
# encoding: utf8
from setuptools import setup, find_packages

setup(
    name="SmallScrewdriver",
    version="1.0.1",
    packages=find_packages(),
    scripts=[],
    install_requires=['PySide>=1.2.1',
                      'SillyCrossbow>=1.0.8'],
    package_data={
        '': ['*.txt', '*.rst']
    },
    author="Shnaider Pavel",
    author_email="shnaiderpasha@gmail.com",
    description="SmallScrewdriver is python texture packer library",
    license="LGPL",
    keywords="texture",
    url="https://github.com/Ingener74/Small-Screwdriver"
)
