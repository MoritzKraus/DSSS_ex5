from distutils.core import setup
from setuptools import find_packages

setup(
    name="snowflake",
    version="0.1",
    author="Moritz Kraus",
    author_email="moritz.mk.kraus@fau.de",
    packages=find_packages(),
    install_requires=["numpy", "turtles"],
)