=======================
Encapsulation in Python
=======================

Evolving a simple class from public attributes to properties and descriptors
in five steps.

The last step includes a metaclass that provides better integration from of
the descriptors with their target instances.

See slides ``encap-draft.pdf`` for more context and UML diagrams.

Benchmarks
==========

The metaclass version in step 5 is much faster than the ``__new__``
implementation in step 4, at least when a large quantity of BultItem instances
is built.

Code used for timing::

    from timeit import timeit
    stmt = '''LineItem('Golden raisins', 10, 36.95)'''
    setup = '''from bulkfood import LineItem'''
    print(timeit(stmt, setup))


Benchmark results:

=========== ============ ============= ==================
interpreter __new__      metaclass     speedup factor
=========== ============ ============= ==================
CPython 2.7 8.1243929863 1.63555312157 4.97 times faster
PyPy 1.7.0  0.6383988857 0.01469016075 43.46 times faster
=========== ============ ============= ==================

Note: by default, ``timeit`` executes the timed statement 1,000,000 times.
