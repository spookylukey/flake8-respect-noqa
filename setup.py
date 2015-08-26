#!/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import with_statement
from setuptools import setup


def get_version(fname='flake8_respect_noqa.py'):
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


def get_long_description():
    descr = []
    for fname in ('README.rst',):
        with open(fname) as f:
            descr.append(f.read())
    return '\n\n'.join(descr)


setup(
    name='flake8-respect-noqa',
    version=get_version(),
    description='Always ignore #noqa lines with flake8.',
    long_description=get_long_description(),
    keywords='flake8 noqa pep8',
    author='Luke Plant',
    author_email='L.Plant.98@cantab.net',
    url='https://github.com/spookylukey/flake8-respect-noqa',
    install_requires=[
        'flake8>=2.4.1',
    ],
    license='MIT',
    py_modules=['flake8_respect_noqa'],
    zip_safe=False,
    entry_points={
        'flake8.extension': [
            'flake8_respect_noqa = flake8_respect_noqa:RespectNoqa',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)
