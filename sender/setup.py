from dotenv import load_dotenv
import os
from setuptools import setup, find_packages

load_dotenv()
setup(name='sender', version=os.getenv('VERSION'), packages=find_packages())