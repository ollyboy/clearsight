# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in clearsight/__init__.py
from clearsight import __version__ as version

setup(
	name='clearsight',
	version=version,
	description='Project Portfolio Management',
	author='steve mcd',
	author_email='mcd.steven@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
