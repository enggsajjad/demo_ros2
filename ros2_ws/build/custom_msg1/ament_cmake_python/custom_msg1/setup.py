from setuptools import find_packages
from setuptools import setup

setup(
    name='custom_msg1',
    version='0.0.0',
    packages=find_packages(
        include=('custom_msg1', 'custom_msg1.*')),
)
