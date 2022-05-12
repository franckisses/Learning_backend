
from array import array
import math


class Vector2d:
    typecode = 'd'  # <1>

    def __init__(self, x, y):
        self.__x = float(x)    # <2>
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))  # <3>

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)  # <4>

    def __str__(self):
        return str(tuple(self))  # <5>

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +  # <6>
                bytes(array(self.typecode, self)))  # <7>

    def __eq__(self, other):
        return tuple(self) == tuple(other)  # <8>

    def __abs__(self):
        return math.hypot(self.x, self.y)  # <9>

    def __bool__(self):
        return bool(abs(self))  # <10>

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def angle(self):
        return math.atan2(self.y, self.x)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

"""
>>> from example_9_9 import *
>>> v1 = Vector2d(3, 4)
>>> v2 = Vector2d(3.1, 4.2)
>>> v1
Vector2d(3.0, 4.0)
>>> v2
Vector2d(3.1, 4.2)
>>> hash(v1), hash(v2)
(7, 384307168202284039)
>>> set([v1,v2])
{Vector2d(3.1, 4.2), Vector2d(3.0, 4.0)}
"""
