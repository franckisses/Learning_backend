# -*- coding: utf-8 -*-
from collections import namedtuple

Result = namedtuple('Result', 'count average')

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)

"""
>>> from coroaverager2 import *
>>> coro_avg = averager()
>>> nex(coro_avg)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'nex' is not defined
>>> next(coro_avg)
>>> coro_avg.send(10)
>>> coro_avg.send(11)
>>> coro_avg.send(12)
>>> coro_avg.send(14)
>>> coro_avg.send(None)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration: Result(count=4, average=11.75)
>>> from inspect import getgeneratorstate
>>> getgeneratorstate(coro_avg)
'GEN_CLOSED'
>>> coro_avg2 = averager()
>>> nect(coro_avg2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'nect' is not defined
>>> next(coro_avg2)
>>> coro_avg2.send(10)
>>> coro_avg2.send(20)
>>> coro_avg2.send(40)
>>> coro_avg2.send(30)
>>> try:
...     coro_avg2.send(None)
... except StopIteration as exc:
...     result = exc.value
...
>>> result
Result(count=4, average=25.0)
"""
