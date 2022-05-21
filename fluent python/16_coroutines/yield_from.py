# -*- coding: utf-8 -*-
>>> def gen():
...     for c in 'AB':
...         yield c
...     for i in range(1,3):
...         yield i
...
>>> list(gen)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'function' object is not iterable
>>> list(gen())
['A', 'B', 1, 2]
>>> def gen():
...     yield from 'AB'
...     yield from range(1,3)
...
>>> list(gen())
['A', 'B', 1, 2]
