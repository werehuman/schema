import sys
from setuptools import setup

import schema


if sys.version_info.major == 3:
    long_description = open('README.rst', encoding='utf-8').read()
else:
    long_description = open('README.rst').read()


setup(
    name=schema.__name__,
    version=schema.__version__,
    author="Vladimir Keleshev",
    author_email="vladimir@keleshev.com",
    description="Simple data validation library",
    license="MIT",
    keywords="schema json validation",
    url="http://github.com/halst/schema",
    py_modules=['schema'],
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: MIT License",
    ],
)
