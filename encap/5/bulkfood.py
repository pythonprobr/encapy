
class Quantity(object):

    def set_name(self, prefix, key):
        self.attr_name = '__%s_%s' % (prefix, key)

    def __get__(self, instance, owner):
        return getattr(instance, self.attr_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.attr_name, value)
        else:
            raise ValueError('value must be > 0')

class BusinessEntityMeta(type):
    def __init__(self, class_name, bases, attr_dict):
        for key, attr in attr_dict.items():
            if isinstance(attr, Quantity):
                attr.set_name(class_name, key)

class BusinessEntity(object):
    __metaclass__ = BusinessEntityMeta

class BulkItem(BusinessEntity):
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
