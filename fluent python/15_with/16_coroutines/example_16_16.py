# -*- coding: utf-8 -*-

def chain(*iterable):
    for it in iterable:
        yield from it
