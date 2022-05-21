# -*- coding: utf-8 -*-

def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:', x)

"""
from example_16_1 import *
>>> my_coro = simple_coroutine()
>>> from inspect import *
>>> next(my_coro)
-> coroutine started
>>> getgeneratorstate(my_coro)
'GEN_SUSPENDED'
>>> my_coro.send(100)
-> coroutine received: 100
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
激活协程，需要调用next(my_coro) 或者用 my_coro.send(None)

"""
