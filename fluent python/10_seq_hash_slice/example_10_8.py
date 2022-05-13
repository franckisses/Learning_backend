# -*- coding: utf-8 -*-

# @Time: 2022-05-13
# @File: %
# @Author: Franckisses
# @Description: 

from array import array
import reprlib
import math
import numbers

class Vector:
    typecode = 'd'
    shortcut_names = 'xyzt'

    def __init__(self, components):
        self.__components = array(self.typecode, components)

    def __iter__(self):
        return iter(self.__components)

    def __repr__(self):
        components = reprlib.repr(self.__components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(slef.__components))

    def __eq__(self, other):
        return tuple(self)  == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(self, octets):
        typecode = str(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __len__(self):
        return len(self.__components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self.__components[index])
        if isinstance(index, numbers.Integral):
            return self.__components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self.__components):
                return self.__components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))



"""
>>> from example_10_8 import *
>>> a = Vector(range(10))
>>> a.x
0.0
>>> a.y
1.0
>>> a.t
3.0
>>> a.z
2.0
>>> a.x,a.y,a.z,a.t
(0.0, 1.0, 2.0, 3.0)
>>> a.x
0.0
>>> a.x = 10
>>> a.x
10
>>> a
Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
>>>
"""
