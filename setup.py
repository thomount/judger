from os.path import dirname, join
from setuptools import setup, find_packages

# Define version information
NAME = 'judger'

# Define version information
with open(join(dirname(__file__), NAME + '/VERSION'), 'rb') as f:
    VERSION = f.read().decode('ascii').strip()

setup(
    name=NAME,
    version=VERSION,
    description="Judge codes with input and output files",
    author='Thomount',
    author_email='tjpby@163.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    #install_requires=[
    #],


)
