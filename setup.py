from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = ('1.3.1.0')
DESCRIPTION = 'Crud is a great module for python beginners its for edit folder or file like crud'
LONG_DESCRIPTION = 'A package that good for new folder with functions that already cool and good to go'

# Setting up
setup(
    name="Crud",
    version=VERSION,
    author="Raiz120 (Raiz Packagener Developer)",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires='time', 'pillow'],
    keywords=['python', 'Guide', 'for beginner', 'Crud', 'Good / Greate'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
