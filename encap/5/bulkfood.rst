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

In order to store the ``Quantity`` values with better names in the
``BulkRegister`` instances, a new ``BusinessEntity`` class is introduced
to implement the attribute naming logic. The new attribute names include
the name of the actual class attribute to which each descriptor is bound,
``weight`` and ``price``::

	>>> [name for name in dir(raisins) if name[-1] != '_'] #doctest: +ELLIPSIS
	['__BulkItem_price', '__BulkItem_weight', ..., 'price', 'weight']



