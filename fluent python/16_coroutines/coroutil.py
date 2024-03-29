# -*- coding: utf-8 -*-
from functools import wraps

def coroutine(func):
    """装饰器 向前执行到第一个`yield`表达式，预激`func`"""
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer
