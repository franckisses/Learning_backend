# -*- coding: utf-8 -*-

class DemoException(Exception):
    """为这次演示定义的异常"""

def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handling, Continuing...')
        else:
            print('-> coroutine received:{!r}'.format(x))
    raise RuntimeError('this line should never run.')

"""

>>> from coro_exc_demo import *
>>> exc_coro = demo_exc_handling()
>>> next(exc_coro)
-> coroutine started
>>> exc_coro.send(11)
-> coroutine received:11
>>> exc_coro.send(22)
-> coroutine received:22
>>> exc_coro.send(33)
-> coroutine received:33
>>> exc_coro.close()
>>> from inspect import getgeneratorstate
>>> getgeneratorstate(exc_coro)
'GEN_CLOSED'
>>> exc_coro1 = demo_exc_handling()
>>> next(exc_coro1)
-> coroutine started
>>> exc_coro1.send(11)
-> coroutine received:11
>>> exc_coro1.throw(DemoException)
*** DemoException handling, Continuing...
# 传入可以处理的异常之后，协程不会终止
>>> getgeneratorstate(exc_coro1)
'GEN_SUSPENDED'
>>> exc_coro1.throw(ZeroDivisionError)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/gongyan/Project/liangpi/fluent python/15_with/16_coroutines/coro_exc_demo.py", line 10, in demo_exc_handling
    x = yield
ZeroDivisionError
# 如果传入的异常没有处理，协程就会终止
>>> getgeneratorstate(exc_coro1)
'GEN_CLOSED'
>>>
"""
