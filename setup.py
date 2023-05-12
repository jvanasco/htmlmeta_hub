"""htmlmeta_hub installation script.
"""
import os
import re

from setuptools import setup
from setuptools import find_packages

HERE = os.path.abspath(os.path.dirname(__file__))
long_description = (
    description
) = "Lightweight support for managing metadata on webpages."
with open(os.path.join(HERE, "README.md")) as f:
    long_description = f.read()

# store version in the init.py
with open(os.path.join(HERE, "src", "htmlmeta_hub", "__init__.py")) as v_file:
    VERSION = re.compile(r'.*__VERSION__ = "(.*?)"', re.S).match(v_file.read()).group(1)

requires = ["metadata_utils>=0.0.2"]
tests_require = [
    "mypy",
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
    packages=find_packages(
        where="src",
    ),
    package_dir={"": "src"},
    package_data={"htmlmeta_hub": ["py.typed"]},
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Framework :: Pyramid",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
    license="MIT",
    install_requires=requires,
    tests_require=tests_require,
    extras_require={
        "testing": testing_extras,
    },
    test_suite="tests",
)
