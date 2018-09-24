"""setuptools-based setup module for drewtilities."""
from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, "README.rst")) as f:
    LONG_DESCRIPTION = f.read().strip()

with open(path.join(HERE, "VERSION")) as f:
    VERSION = f.read().strip()

URL = "https://github.com/alixnovosi/drewtilities"

INSTALL_REQUIRES = [
    "clint>=0.5.1, <0.6.0",
    "requests>=2.19.1, <3.0.0",
]

SETUP_REQUIRES = [
    "pytest-runner",
]

TEST_REQUIRES = [
    "coveralls>=1.2.0, <2.0.0",
    "pytest>=3.2.5, <4.0.0",
]

setup(author="Andrew Michaud",
      author_email="dev@mail.andrewmichaud.com",

      classifiers=[
          "Development Status :: 5 - Production/Stable",
           "Environment :: Console",
           "Intended Audience :: Developers",
           "License :: OSI Approved :: BSD License",
           "Natural Language :: English",
           "Operating System :: MacOS :: MacOS X",
           "Operating System :: POSIX :: Linux",
           "Programming Language :: Python :: 3.6",
           "Programming Language :: Python :: Implementation :: CPython",
           "Topic :: Software Development :: Libraries",
      ],

      name="drewtilities",
      description="Simple utilities for dev work.",
      download_url=f"{URL}/archive/v{VERSION}.tar.gz",
      url=f"{URL}",
      keywords=[],
      license="BSD3",

      entry_points={
          "console_scripts": ["drewtilities = drewtilities.__main__:main"]
      },

      package_data={
          ".": ["VERSION"],
      },

      python_requires=">=3.6",

      packages=find_packages(),
      long_description=LONG_DESCRIPTION,

      install_requires=INSTALL_REQUIRES,
      setup_requires=SETUP_REQUIRES,
      tests_require=TEST_REQUIRES,

      version=VERSION)
