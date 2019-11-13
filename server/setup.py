# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='janus-quality-dashboard',
    version='0.1.0',
    description='Janus Quality Dashboard',
    long_description=readme,
    author='Jonathan Coombs',
    author_email='jonathan.coombs@cambiahealth.com',
    url='https://github.com/jcoombs-at-cambia/hackathon-2019',
    packages=find_packages(exclude=('tests', 'docs'))
)