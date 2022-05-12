
from array import array
import math


class Vector2d:
    typecode = 'd'  # <1>

    def __init__(self, x, y):
        self.x = float(x)    # <2>
        self.y = float(y)

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

"""
>>> from example_9_6 import *
>>> format(Vector2d(1,1),'p')
'<1.4142135623730951, 0.7853981633974483>'
>>> format(Vector2d(1,1), '.3ep')
'<1.414e+00, 7.854e-01>'
>>> format(Vector2d(1,1), '0.5ep')
'<1.41421e+00, 7.85398e-01>'
>>> format(Vector2d(1,1), '0.5fp')
'<1.41421, 0.78540>'
"""
