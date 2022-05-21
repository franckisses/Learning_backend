# -*- coding: utf-8 -*-
"""


"""

from coroutil import coroutine

@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count

"""
>>> from coroaverager1 import *
>>> coro_avg = averager()
>>> coro_avg.send(10)
10.0
>>> coro_avg.send(11)
10.5
>>> coro_avg.send(12)
11.0
>>> coro_avg.send(15)
12.0
>>> coro_avg.send('test')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/gongyan/Project/liangpi/fluent python/15_with/16_coroutines/coroaverager1.py", line 16, in averager
    total += term
TypeError: unsupported operand type(s) for +=: 'float' and 'str'
>>> coro_avg.send(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
"""
