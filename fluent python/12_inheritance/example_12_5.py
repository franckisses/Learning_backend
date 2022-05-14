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
        A.ping(self)
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)

"""
>>> from example_12_5 import *
>>> d = D()
>>> d.ping()
ping: <example_12_5.D object at 0x7fa8804c7cf8>
post-ping: <example_12_5.D object at 0x7fa8804c7cf8>
>>> d.pingpong()
ping: <example_12_5.D object at 0x7fa8804c7cf8>
post-ping: <example_12_5.D object at 0x7fa8804c7cf8>
pong: <example_12_5.D object at 0x7fa8804c7cf8>
PONG: <example_12_5.D object at 0x7fa8804c7cf8>
PONG: <example_12_5.D object at 0x7fa8804c7cf8>
PONG: <example_12_5.D object at 0x7fa8804c7cf8>
>>> bool.__mro__
(<class 'bool'>, <class 'int'>, <class 'object'>)
>>> def print_mro(cls):
...     print(','.join(c.__name__ for c in cls.__mro__))
>>> print_mro(bool)
bool,int,object
>>> import tkinter
>>> print_mro(tkinter.Text)
Text,Widget,BaseWidget,Misc,Pack,Place,Grid,XView,YView,object
"""
