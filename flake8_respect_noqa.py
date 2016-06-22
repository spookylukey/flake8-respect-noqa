# -*- coding: utf-8 -*-
"""
Always ignore lines with '# noqa'
"""
__version__ = 0.2

try:
    from pep8 import StandardReport, noqa
except ImportError:
    # Try the new (as of 2016-June) pycodestyle package.
    from pycodestyle import StandardReport, noqa


class RespectNoqaReport(StandardReport):

    def error(self, line_number, offset, text, check):
        if len(self.lines) > line_number - 1 and noqa(self.lines[line_number - 1]):
            return
        else:
            return super(RespectNoqaReport, self).error(line_number, offset,
                                                        text, check)


class RespectNoqa(object):
    name = 'flake8-respect-noqa'
    version = __version__

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def parse_options(cls, options):
        # The following only works with (flake8 2.4.1) if you run like "flake8 -j 1",
        # or put "jobs = 1" in your [flake8] config.
        # Otherwise, flake8 replaces this reported with it's own.
        # See https://gitlab.com/pycqa/flake8/issues/66
        options.reporter = RespectNoqaReport
        options.report = RespectNoqaReport(options)
