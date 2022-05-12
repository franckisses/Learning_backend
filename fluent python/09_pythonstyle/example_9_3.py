# -*- coding: utf-8 -*-

# @Time: 2022-05-12
# @File: %
# @Author: dreamhomes
# @Description: 
from array import array
import math
class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{} ({!r}, {!r})'.format(class_name, *slef)

    def __str__(self):
        return str(tuple(self))

    def __bytes(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def  frombytes(cls, octets):
        typecode = chr(octets)
        memv = memoryview(octets[1:].cast(typecode))
        return cls(*memv)

