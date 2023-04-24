from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in fd_management/__init__.py
from fd_management import __version__ as version

setup(
	name="fd_management",
	version=version,
	description="fd management",
	author="finbyx",
	author_email="info@finbyz.tech",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
