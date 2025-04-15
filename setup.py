#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Installation of the pyfunc2 package.
"""

import os
from setuptools import setup, find_packages

# Long description from README.md
try:
    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md"), encoding="utf-8") as f:
        LONG_DESCRIPTION = '\n' + f.read()
except FileNotFoundError:
    LONG_DESCRIPTION = ''

# Configuration setup
setup(
    name="pyfunc2",
    version="0.1.24",
    description="libs for cameramonit, ocr, fin-officer, cfo, and other projects",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Tom Sapletta",
    author_email="tom@sapletta.com",
    maintainer="pyfunc developers",
    maintainer_email="info@softreck.dev",
    python_requires=">=3.7",
    url="https://www.pyfunc.com",
    project_urls={
        "Repository": "https://github.com/pyfunc/lib",
        "Changelog": "https://github.com/pyfunc/lib/releases",
        "Wiki": "https://github.com/pyfunc/lib/wiki",
        "Issue Tracker": "https://github.com/pyfunc/lib/issues/new",
    },
    packages=["pyfunc2", "pyfunc2.config", "pyfunc2.email", "pyfunc2.file"],
    package_dir={"": "src"},
    license="Apache-2.0",  # Use simple string format
    license_files=("LICENSE"),  # Empty tuple to explicitly prevent license files
    keywords=["python", "pyfunc", "pyfunc2", "pyfunc3", "pyfunc4", "pyfunc5", "pyfunc6",
              "pyfunc7", "pyfunc8", "pyfunc9", "pyfunc10", "pyfunc11", "pyfunc12",
              "pyfunc13", "pyfunc14", "pyfunc15", "pyfunc16", "pyfunc17", "pyfunc18",
              "pyfunc19", "pyfunc20", "pyfunc21", "pyfunc22", "pyfunc23", "pyfunc24",
              "pyfunc25", "pyfunc26", "pyfunc27", "pyfunc28", "pyfunc29", "pyfunc30",
              "pyfunc31", "pyfunc32", "pyfunc33", "pyfunc34", "pyfunc35", "pyfunc36",
              "pyfunc37", "pyfunc38", "pyfunc39", "pyfunc40", "pyfunc41", "pyfunc42",
              "pyfunc43", "pyfunc"],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    # Critical fix for the license-file issue:
    # This prevents setuptools from automatically adding a license-file entry
)