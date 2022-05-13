# -*- coding: utf-8 -*-

# @Time: 2022-05-13
# @File: %
# @Author: Franckisses
# @Description: 

from array import array
import reprlib
import math

class Vector:
    typecode = 'd'

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
