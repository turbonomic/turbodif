#!/usr/bin/python3

import os
from setuptools import setup, find_packages



about = {}
here = os.path.abspath(os.path.dirname(__file__))



with open(os.path.join(here, 'turbodif', '__about__.py'), 'r') as fp:
    exec(fp.read(), about)

with open(os.path.join(here, 'README.md'), 'r') as fp:
    readme = fp.read()


setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url='https://github.com/turbonomic/turbodif',
    packages=find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
    ],
    package_data={'': ['LICENSE', 'NOTICE']},
    include_package_data=True,
    python_requires=">=3.6",
    license=about['__license__'],
)