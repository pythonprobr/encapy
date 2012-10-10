===================================
Alimentos a granel: itens de pedido
===================================

Um pedido de alimentos a granel é uma coleção de ``ItenPedido``.
Cada item possui campos para descrição, peso e preço::

	>>> from granel import ItemPedido
	>>> ervilha = ItemPedido('ervilha partida', 500, 3.95)
	>>> ervilha.descricao, ervilha.peso, ervilha.preco
	('ervilha partida', 500, 3.95)

O peso de um ``ItemPedido`` deve ser maior que zero::

	>>> ervilha.peso = 0
	Traceback (most recent call last):
		...
	ValueError: valor deve ser > 0

A mesma regra se aplica ao preço::

	>>> lentilha = ItemPedido('lentilha', 1000, 0.00)
	Traceback (most recent call last):
		...
	ValueError: valor deve ser > 0

Armazenagem dos valores
=======================

A classe descritora ``Quantidade`` armazena os dados de cada atributo controlado em um atributo em cada instância de ``ItemPedido``::

Os valores de ``preco`` e ``peso`` são armazenados em atributos das
instâncias de ``ItemPedido`` com nomes arbitrários definidos no método
``Quantidade.__init__``. Isso funciona porque os nomes são únicos, como
``Quantidade_4300501456``.porém não são mnemônicos, o que dificulda a
depuração::

	>>> dir(ervilha) # doctest: +ELLIPSIS
	['Quantidade_...', 'Quantidade_...', ...]
