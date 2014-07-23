from operator import itemgetter

class Quantidade(object):

    _qt_instancias = 0

    def __init__(self):
        cls = self.__class__
        self.set_nome(cls.__name__, id(self))
        self.ordem = cls._qt_instancias
        cls._qt_instancias += 1

    def set_nome(self, prefix, key):
        self.nome_alvo = '%s_%s' % (prefix, key)

    def __get__(self, instance, owner):
        return getattr(instance, self.nome_alvo)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.nome_alvo, value)
        else:
            raise ValueError('valor deve ser > 0')

def entidade(cls):
    nome = cls.__name__
    for chave, atr in cls.__dict__.items():
        if hasattr(atr, 'set_nome'):
            atr.set_nome('__' + nome, chave)
    return cls


class Modelo(object):

    @classmethod
    def listar_campos(cls):
        campos = [(nome, atr.ordem) for nome, atr in cls.__dict__.items()
                if hasattr(atr, 'ordem')]
        campos.sort(key=itemgetter(1))
        return [nome for nome, ordem in campos]
