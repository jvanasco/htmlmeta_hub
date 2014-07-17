"""htmlmeta_hub installation script.
"""
import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.md")).read()
README = README.split("\n\n", 1)[0] + "\n"

requires = [
    "metadata_utils>=0.0.1",
]

setup(
    name="htmlmeta_hub",
    description="Lightweight support for managing metadata",
    version="0.0.9",
    url="https://github.com/jvanasco/htmlmeta_hub",
    author="Jonathan Vanasco",
    author_email="jonathan@findmeon.com",
    long_description=README,
    zip_safe=False,
    keywords="web pylons",
    test_suite="tests",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Framework :: Pylons",
        "Framework :: Pyramid",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
    ],
    license="MIT",
    install_requires = requires,
)
