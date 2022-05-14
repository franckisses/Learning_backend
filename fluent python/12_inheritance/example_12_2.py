# -*- coding: utf-8 -*-

class AnswerDict(dict):
    def __getitem__(self, key):
        return 42

"""
>>> from example_12_2 import *
>>> ad = AnswerDict(a='foo')
>>> ad
{'a': 'foo'}
>>> ad['a']
42
>>> ad
{'a': 'foo'}
>>> d = {}
>>> d
{}
>>> d.update(ad)
>>> d
{'a': 'foo'}
"""
