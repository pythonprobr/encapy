
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

class BusinessEntity(object):
    def __new__(cls, *args, **kwargs):
        for key, attr in cls.__dict__.items():
            if isinstance(attr, Quantity):
                attr.set_name(cls.__name__, key)
        return super(BusinessEntity, cls).__new__(cls, *args, **kwargs)

class BulkItem(BusinessEntity):
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
