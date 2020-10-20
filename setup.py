"""htmlmeta_hub installation script.
"""
import os
import re

from setuptools import setup
from setuptools import find_packages

long_description = (
    description
) = "Lightweight support for managing metadata on webpages."
try:
    here = os.path.abspath(os.path.dirname(__file__))
    long_description = open(os.path.join(here, "README.md")).read()
except:
    pass

# store version in the init.py
with open(
    os.path.join(os.path.dirname(__file__), "htmlmeta_hub", "__init__.py")
) as v_file:
    VERSION = re.compile(r'.*__VERSION__ = "(.*?)"', re.S).match(v_file.read()).group(1)

requires = ["metadata_utils>=0.0.2"]
tests_require = [
    "six",
    "pyramid",
    "pytest",
]
testing_extras = tests_require + []


setup(
    name="htmlmeta_hub",
    version=VERSION,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jvanasco/htmlmeta_hub",
    author="Jonathan Vanasco",
    author_email="jonathan@findmeon.com",
    zip_safe=False,
    keywords="metadata html web pyramid",
    test_suite="tests",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Framework :: Pyramid",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    license="MIT",
    install_requires=requires,
    tests_require=tests_require,
    extras_require={
        "testing": testing_extras,
    },
)
