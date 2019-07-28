
from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name= 'pwHash',
    version = '0.1.0',
    packages = ['pwHash'],
    description = 'Simple Python Package for finding the hash of a string'
    long_description = readme()
    entry_points = {
        'console_scripts': [
            'pwHash = pwHash.main:hashThis'
        ]
    },
    install_requires = ['click']
)