==============
LineItem tests
==============

A line item for a bulk food order has description, weight and price fields::

	>>> from bulkfood import LineItem
	>>> raisins = LineItem('Golden raisins', 10, 36.95)
	>>> raisins.weight, raisins.description, raisins.price
	(10, 'Golden raisins', 36.95)

The ``weight`` of a ``LineItem`` must be > 0::

	>>> raisins.weight = 0
	Traceback (most recent call last):
		...
	ValueError: value must be > 0

The same rule applies to ``price``::

	>>> raisins.price = 0
	Traceback (most recent call last):
		...
	ValueError: value must be > 0

The values of ``price`` and ``weight`` are stored in ``LineItem`` instance
attributes with names synthesized by the descriptor class. These attributes
look like ``Quantity_10b7c72a0``. They are unique but not user friendly::

	>>> [name for name in dir(raisins) if name[-1] != '_'] #doctest: +ELLIPSIS
	['Quantity_...', 'Quantity_...', 'description', 'price', 'weight']



