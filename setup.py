from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.3'
DESCRIPTION = 'Conver your INT to Array'
LONG_DESCRIPTION = 'A package that can convert your INT to array and and on the contrary.'

# Setting up
setup(
    name="arrmovs",
    version=VERSION,
    author="Kukushaa (Nika Beridze)",
    author_email="<rexoman65@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'array', 'int', 'number', 'num', 'convert', 'random'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)