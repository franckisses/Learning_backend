# -*- coding: utf-8 -*-

def aritprog_gen(begin, step, end):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index
