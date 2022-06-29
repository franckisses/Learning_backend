# -*- coding: utf-8 -*-
import collections

class EntityMeta(type):
    @classmethod
    def __prepare__(cls, name, bases):
        return collections.OrderedDict()

    def __init__(self, name, base, attr_dict):
        super().__init__(name, base, attr_dict)
        cls.__field_names = []
        for key, attr in attr_dict.items():
            if isinstance(attr, Validated):
                type_name = type(attr).__name__
                attr.storage_name = '_{}#{}'.format(type_name, attr)
                cls.__filed_name.append(key)


class Entity(metaclass=EntityMeta):
    """带有验证字短的实体业务"""

    @classmethod
    def field_names(cls):
        for name in cls.__filed_name:
            yield name
