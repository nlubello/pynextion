import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pynextion",
    version = "0.0.2",
    author = "Raffaele Montella",
    author_email = "raffaele.montella@uniparthenope.it",
    description = ("Python librari to drive Nextion display "),
    license = "Apache 2.0",
    keywords = "nextion python",
    url = "http://packages.python.org/nl-pynextion",
    packages=['pynextion' ,'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache 2.0 License",
    ],
)
