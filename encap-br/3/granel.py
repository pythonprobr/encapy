class Quantidade(object):

    def __init__(self):
        prefixo = self.__class__.__name__
        chave = id(self)
        self.nome_atr = '%s_%s' % (prefixo, chave)

    def __get__(self, instance, owner):
        return getattr(instance, self.nome_atr)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.nome_atr, value)
        else:
            raise ValueError('valor deve ser > 0')

class ItemPedido(object):
    peso = Quantidade()
    preco = Quantidade()

    def __init__(self, descricao, peso, preco):
        self.descricao = descricao
        self.peso = peso
        self.preco = preco
