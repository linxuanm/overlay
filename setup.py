'''Installer for the package.'''

import pathlib
from setuptools import find_packages, setup

PATH = pathlib.Path(__file__).parent

README = (PATH / "README.md").read_text()

setup(
	name = 'overlay',
	version = '1.1.0',
	description = 'A package that creates and manipulates screen overlays based on tkinter.',
	long_description = README,
	long_description_content_type = "text/markdown",
	url = 'https://github.com/davidmaamoaix/Overlay',
	author = 'David Ma',
	author_email = "davidma@davidma.cn",
	license = 'MIT',
	packages = find_packages(),
	include_package_data = True,
)