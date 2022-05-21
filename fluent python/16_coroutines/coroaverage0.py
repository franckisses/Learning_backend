# -*- coding: utf-8 -*-

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
>>> from coroaverage0 import *
>>> coro_avg = averager()
>>> next(coro_avg)
>>> coro_avg.send(10)
10.0
>>> coro_avg.send(11)
10.5
>>> coro_avg.send(12)
11.0
"""
