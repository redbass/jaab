#!/usr/bin/env python

from distutils.core import setup

from setuptools import find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='jaab',
      version='1.0',
      description='Just Another Address Book',
      author='Luca Gallici',
      author_email='luca.gallici@gmail.com',
      packages=find_packages(),
      install_requirements=requirements)
