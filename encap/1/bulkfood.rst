==============
BulkItem tests
==============

A line item for a bulk food order has description, weight and price fields::

	>>> from bulkfood import BulkItem
	>>> raisins = BulkItem('Golden raisins', 10, 36.95)
	>>> raisins.weight, raisins.description, raisins.price
	(10, 'Golden raisins', 36.95)
