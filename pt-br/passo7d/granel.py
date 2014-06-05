from modelo import Quantidade, entidade, Modelo

@entidade
class ItemPedido(Modelo):

    peso = Quantidade()
    preco = Quantidade()
    volumes = Quantidade()

    def __init__(self, descricao, peso, preco):
        self.descricao = descricao
        self.peso = peso
        self.preco = preco

    def subtotal(self):
        return self.peso * self.preco
