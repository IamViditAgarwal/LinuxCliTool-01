# String Hashing CLI utility
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![HitCount](http://hits.dwyl.io/IamViditAgarwal/badges.svg)](http://hits.dwyl.io/IamViditAgarwal/badges.svg)


Small-n-simple command line utility for generating the hash's of a string.

Some of the supported formats are:
*   md5
*   sha224
*   sha256
*   sha512

## Folder Structure
*   `__init__.py`: The purpose of this file is to let `pip` know that this is a python package
*   `main.py`: Now, this file holds the code. In practical scenarios, there are multiple files that contains the code but for now, we can dump all the code in this file.
*   `setup.py`: This file let `pip` know the details of this package such as name, version and entrypoints.

## Installation
Follow the steps to install the package:
*   In the root level of the repo,
*   Run this: ```pip3 install -e .```
    *   `-e` let the pip to know that this package is in development mode.

## Demo Video
![demo](./demo/demo.svg)