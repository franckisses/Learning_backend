# -*- coding: utf-8 -*-
import model_v6 as model



@model.entity
class LineItem:
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

"""
>>> from bulkfood_v6  import LineItem
>>> raisins = LineItem('Golden raisins', 10, 6.95)
>>> dir(raisins)
['_NonBlank#description', '_Quantity#price', '_Quantity#weight', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'description', 'price', 'subtotal', 'weight']
>>> rais
raise    raisins
>>> raisins.description
'Golden raisins'
>>> getattr(raisins, '_NonBlank#description')
'Golden raisins'
>>>
"""
