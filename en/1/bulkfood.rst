==============
LineItem tests
==============

A line item for a bulk food order has description, weight and price fields::

	>>> from bulkfood import LineItem
	>>> raisins = LineItem('Golden raisins', 5, 2.48)
	>>> raisins.description, raisins.weight, raisins.price
	('Golden raisins', 5, 2.48)
	>>> raisins.subtotal()
	12.4
