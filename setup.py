from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in zh_chinese_language/__init__.py
from zh_chinese_language import __version__ as version

setup(
	name="zh_chinese_language",
	version=version,
	description="Chinese Language",
	author="Phipsoft",
	author_email="huzj@phipsoft.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
