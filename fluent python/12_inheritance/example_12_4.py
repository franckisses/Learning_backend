# -*- coding: utf-8 -*-

class A:
    def ping(self):
        print('ping:', self)


class B(A):
    def ping(self):
        print('pong:', self)

class C(A):
    def pong(self):
        print('PONG:', self)


class D(B, C):
    def ping(self):
        super().ping()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)

"""
>>> from example_12_4 import *
>>> d = D()
>>> d
<example_12_4.D object at 0x7f96525c7c50>
>>> d.pong()
PONG: <example_12_4.D object at 0x7f96525c7c50>
>>> C.pong(d)
PONG: <example_12_4.D object at 0x7f96525c7c50>
>>> D.__mro__
(<class 'example_12_4.D'>, <class 'example_12_4.B'>, <class 'example_12_4.C'>, <class 'example_12_4.A'>, <class 'object'>)
"""
