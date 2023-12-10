from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='caplogger',
    version='1.0.0',
    packages=find_packages(),
    description='A custom logger for Capstone',
    install_requires=requirements,
)
