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
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return '<{} object>'.format(cls_name(obj))

def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print('-> {}._{}({})'.format(cls_name(args[0]), name, pseudo_args))


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

"""
# 覆盖型描述符
>>> from descriptionkinds import *
>>> obj = Managed()
>>> obj.over
-> Overriding._get(<Overriding object>, <Managed object>, <class Managed>)
>>> Managed.over
-> Overriding._get(<Overriding object>, None, <class Managed>)
>>> obj.over = 7
-> Overriding._set(<Overriding object>, <Managed object>, 7)
>>> obj.over
-> Overriding._get(<Overriding object>, <Managed object>, <class Managed>)
>>> obj.__dict__
{}
>>> obj.__dict__['over'] = 8
>>> vars(obj)
{'over': 8}
>>> obj.over
-> Overriding._get(<Overriding object>, <Managed object>, <class Managed>)
>>> obj
<descriptionkinds.Managed object at 0x7fcbc15c7d68>
>>> dir(obj)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'no_over', 'over', 'over_no_get', 'spam']
>>> obj.over
-> Overriding._get(<Overriding object>, <Managed object>, <class Managed>)

# 没有__get__方法的覆盖型描述符
>>> obj.over_no_get
<descriptionkinds.OverridingNoGet object at 0x7fcbc164c208>
>>> Managed.over_no_get
<descriptionkinds.OverridingNoGet object at 0x7fcbc164c208>
>>> obj.over_no_get = 7
-> OverridingNoGet._set(<OverridingNoGet object>, <Managed object>, 7)
>>> obj.over_no_get
<descriptionkinds.OverridingNoGet object at 0x7fcbc164c208>
>>> obj.__dict__['over_no_get'] = 9
>>> obj.over_no_get
9
>>> obj.over_no_get= 7
-> OverridingNoGet._set(<OverridingNoGet object>, <Managed object>, 7)
>>> obj.over_no_get
9
>>>
>>> obj.no_over
get <descriptionkinds.NonOverriding object at 0x7fcbc164c240> <descriptionkinds.Managed object at 0x7fcbc15c7d68> <class 'descriptionkinds.Managed'>
>>> obj.no_over
get <descriptionkinds.NonOverriding object at 0x7fcbc164c240> <descriptionkinds.Managed object at 0x7fcbc15c7d68> <class 'descriptionkinds.Managed'>
>>> obj.no_over = 7
>>> obj.no_over
7
>>> Managed.no_over
get <descriptionkinds.NonOverriding object at 0x7fcbc164c240> None <class 'descriptionkinds.Managed'>
>>> del obj.no_over
>>> obj.no_over
get <descriptionkinds.NonOverriding object at 0x7fcbc164c240> <descriptionkinds.Managed object at 0x7fcbc15c7d68> <class 'descriptionkinds.Managed'>
"""
