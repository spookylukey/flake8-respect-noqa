Flake8 respect NOQA
===================

By default, flake8 (before 3.0) ignores ``# NOQA`` directives for some PEP8 errors.

See https://gitlab.com/pycqa/flake8/issues/21

This flake8 plugin makes it respect them.

If you are using flake8 3.0.0b1 or later, this plugin is not needed - see http://flake8.pycqa.org/en/3.0.0b1/user/ignoring-errors.html

Installation
------------

Simply::

  $ pip install flake8-respect-noqa


Usage
-----

It is enabled by default as soon as it is installed. Check that flake8 finds it::


  $ flake8 --version

  2.4.1 (pep8: 1.5.7, flake8-respect-noqa: 0.2, mccabe: 0.3.1, pyflakes: 0.8.1) CPython 2.7.6 on Linux

However, to get it to work, you currently need to run flake8 with ``--jobs=1`` or
put ``jobs = 1`` in your ``[flake8]`` configuration, otherwise flake8 uses its own 'reporter',
which trumps the customizations this extension attempts to make.

See https://gitlab.com/pycqa/flake8/issues/66
