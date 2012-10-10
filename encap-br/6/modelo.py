class Quantidade(object):

    def __init__(self):
        self.set_nome(self.__class__.__name__, id(self))

    def set_nome(self, prefix, key):
        self.nome_atr = '%s_%s' % (prefix, key)

    def __get__(self, instance, owner):
        return getattr(instance, self.nome_atr)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.nome_atr, value)
        else:
            raise ValueError('valor deve ser > 0')

class ModeloMeta(type):

    def __init__(mcs, nome, bases, dic):
        super(ModeloMeta, mcs).__init__(nome, bases, dic)
        for chave, atr in dic.items():
            if hasattr(atr, 'set_nome'):
                atr.set_nome('__' + nome, chave)

class Modelo(object):
    __metaclass__ = ModeloMeta
