# -*- coding: utf-8 -*-
class Quantity:
     __counter = 0
 
     def __init__(self, storage_name):
         cls = self.__class__
         prefix = cls.__name__
         index = cls.__counter
         self.storage_name = '{}#{}'.format(prefix, index)
         cls.__counter += 1
 
     def __get__(self, instance, owner):
         if instance is None:
             return self
         else:
             return getattr(instance,self.storage_name)
 
     def __set__(self, instance, value):
         if value > 0:
             setattr(instance, self.storage_name, value)
         else:
             raise ValueError('value must be >0')
