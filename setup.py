import os
from setuptools import setup,find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "PyLooper",
    version = "BETA",
    author = "K. H. Lo",
    author_email = "khl.lucien@gmail.com",
    description = ("A general framework to analyse dataset that cannot be fit into memory in one go"),
    license = "MIT",
    keywords = "numpy  cuda  matplotlib tensorflow  hep  parallel-computing gpu-computing",
    url = "https://github.com/lucien1011/PyCudaAnalyzer",
    packages = find_packages(exclude=['docs', 'images', 'tests']),
    entry_points={'console_scripts': [
        'loop = PyLooper.api.run:loop',
        'train = PyLooper.api.run:train',
        'sumup = PyLooper.api.run:sumup',
        ]
        },
    long_description=read('README'),
)
