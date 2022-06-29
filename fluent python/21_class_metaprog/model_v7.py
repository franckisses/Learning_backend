
class EntityMeta(type):
    """元类，用于创建带有验证字段的业务实体"""

    def __init__(cls, name, base, attr_dict):
        super().__init__(name, base, attr_dict)
        for key, attr in attr_dict.items():
            if isinstance(attr, Validated):
                type_name = type(attr).__name__
                attr.storage_name = '_{}#{}'.format(type_name, key)


class Entity(metaclass=EntityMeta):
    """带有验证字短的业务实体"""
