
class Quantity(object):
    def __init__(self):
        # self.attr_key will look like Quantity_10b7c72a0
        self.attr_key = '%s_%x' % (self.__class__.__name__, id(self))

    def __get__(self, instance, owner):
        return getattr(instance, self.attr_key)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.attr_key, value)
        else:
            raise ValueError('value must be > 0')

class BulkItem(object):
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
