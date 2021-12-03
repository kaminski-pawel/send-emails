import os
from setuptools import setup, find_packages

setup(name='sender', version=os.getenv('VERSION'), packages=find_packages())
