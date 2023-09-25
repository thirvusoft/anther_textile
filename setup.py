from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in anther_textile/__init__.py
from anther_textile import __version__ as version

setup(
	name="anther_textile",
	version=version,
	description="Anther Barcode Textile",
	author="Thrivusoft Private Limited",
	author_email="thirvusoft@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
