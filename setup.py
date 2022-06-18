from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Conver your INT to Array'

# Setting up
setup(
    name="arrmovs",
    version=VERSION,
    author="Kukushaa (Nika Beridze)",
    author_email="<rexoman65@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'array', 'int', 'number', 'num', 'convert'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)