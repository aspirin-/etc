#!/usr/bin/env python2.7

""" Snippet for creating 'constants' in python
    http://stackoverflow.com/a/2688086
"""


def constant(f):
    def fset(self, value):
        raise TypeError

    def fget(self):
        return f()
    return property(fget, fset)


class _Const(object):
    @constant
    def FOO():
        return 0xBAADFACE

    @constant
    def BAR():
        return 0xDEADBEEF

CONST = _Const()
