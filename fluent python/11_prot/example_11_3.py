# -*- coding: utf-8 -*-

class Foo:
    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]


"""
<Up>>>> from example_11_3 import *
>>> f = Foo()
>>> f
<example_11_3.Foo object at 0x7fa72ddc7c88>
>>> f[1]
10
>>> for i in f: print(i)
...
0
10
20
>>> 20 in  f
True
>>> 15 in f
False
"""
