# -*- coding: utf-8 -*-

def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split(',')[-1]

def display(obj):
    cls = type(obj)
    if cls is type:
        return '<class {}>'.format(obj.__name__)
    elif cls in [type[None], int]:
        return repr(obj)
    else:
        return '<{} object>'.format(cls_name(obj))

def print_args(name, *args):
    pseudo_arags = ', '.join(display(x) for x in args)
    print('-> {}._{}({})'.format(cls_name(args[0], name, pseudo_args)))


class Overriding:
    """也称数据描述符或者强制描述符"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

    def __set__(self, instance, value):
        print_args('set', self, instance, value)

class OverridingNoGet:
    """没有 ```__get__```方法覆盖型描述符"""
    def __set__(self, instance,value):
        print_args('set', self, instance, value)

class NonOverriding:
    """也称非数据描述符或遮盖型描述符"""
    def __get__(self, instance, owner):
        print('get', self, instance, owner)

class Managed:
    over = Overriding()
    over_no_get = OverridingNoGet()
    no_over = NonOverriding()

    def spam(self):
        print('-> Managed.spam({})'.format(display(self)))
