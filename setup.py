"""htmlmeta_hub installation script.
"""
import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.md")).read()
README = README.split("\n\n", 1)[0] + "\n"

requires = []

setup(name="htmlmeta_hub",
      version="0.0.5",
      description="Lightweight support for managing metadata",
      long_description=README,
      classifiers=[
        "Intended Audience :: Developers",
        "Framework :: Pylons",
        "Framework :: Pyramid",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        ],
      keywords="web pylons",
      py_modules=['htmlmeta_hub'],
      author="Jonathan Vanasco",
      author_email="jonathan@findmeon.com",
      url="https://github.com/jvanasco/htmlmeta_hub",
      license="MIT",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      tests_require = requires,
      test_suite="tests",
      install_requires = requires,
      )

