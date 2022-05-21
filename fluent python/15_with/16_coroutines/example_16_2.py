# -*- coding: utf-8 -*-

def simple_coro2(a):
    print('-> started: a=',a)
    b = yield a
    print('-> Received:b=',b)
    c = yield a + b
    print('-> Received: c=',c)
