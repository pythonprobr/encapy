==========
Benchmarks
==========

The metaclass version is much faster than the __new__ implementation when a large quantity of BultItem instances is built.

Py version => __new__ / metaclass = speedup factor

CPython 2.7 => 8.1243929863 / 1.63555312157 = 4.967367234456582
PyPy 1.7.0 => 0.638398885727 / 0.0146901607513 = 43.45758338080168

