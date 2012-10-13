class Quantity(object):

    def __init__(self):
        prefix = self.__class__.__name__
        key = id(self)
        self.attr_name = '%s_%s' % (prefix, key)

    def __get__(self, instance, owner):
        return getattr(instance, self.attr_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.attr_name, value)
        else:
            raise ValueError('value must be > 0')


class LineItem(object):
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
