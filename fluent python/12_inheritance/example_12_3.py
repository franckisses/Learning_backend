# -*- coding: utf-8 -*-

import collections

class DoppelDict(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)



"""
>>> from example_12_3 import *
>>> dd = DoppelDict(one=1)
>>> dd
{'one': [1, 1]}
>>> dd['two'] = 2
>>> dd
{'one': [1, 1], 'two': [2, 2]}
>>> dd.update(three=3)
>>> dd
{'one': [1, 1], 'two': [2, 2], 'three': [3, 3]}
>>> import collections
>>> class AnswerDict2(collections.UserDict):
...     def __getitem__(self, key):
...         return 42
>>> ad = AnswerDict2(a= 'foo')
>>> ad
{'a': 'foo'}
>>> ad['a']
42
>>> d = []
>>> d = {}
>>> d.update(ad)
>>> d
{'a': 42}
>>>
"""
