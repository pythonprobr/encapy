class ItemPedido(object):

    def __init__(self, descricao, peso, preco):
        self.descricao = descricao
        self.peso = peso
        self.preco = preco

    def total(self):
        return self.peso * self.preco
