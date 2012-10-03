==============
BulkItem tests
==============

A line item for a bulk food order has description, weight and price fields::

	>>> from bulkfood import BulkItem
	>>> raisins = BulkItem('Golden raisins', 10, 36.95)
	>>> raisins.weight, raisins.description, raisins.price
	(10, 'Golden raisins', 36.95)

The ``weight`` of a ``BulkItem`` must be > 0::

	>>> raisins.weight = 0
	Traceback (most recent call last):
		...
	ValueError: value must be > 0

The same rule applies to ``price``::

	>>> raisins.price = 0
	Traceback (most recent call last):
		...
	ValueError: value must be > 0

The values of ``price`` and ``weight`` are stored in ``BulkRegister`` instance
attributes with names synthesized by the descriptor class. These attributes
look like ``Quantity_10b7c72a0`` -- they are unique but not user friendly::

	>>> [name for name in dir(raisins) if name[-1] != '_'] #doctest: +ELLIPSIS
	['Quantity_...', 'Quantity_...', 'description', 'price', 'weight']



