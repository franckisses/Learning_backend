# -*- coding: utf-8 -*-

class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


"""
>>> from example_12_1 import *
>>> dd = DoppelDict(one=1)
>>> dd['two'] = 2
>>> dd
{'one': 1, 'two': [2, 2]}
>>> dd['three'] = 3
>>> dd
{'one': 1, 'two': [2, 2], 'three': [3, 3]}
>>> dd.update(four=4)
>>> dd
{'one': 1, 'two': [2, 2], 'three': [3, 3], 'four': 4}
"""
