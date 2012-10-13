# coding: utf-8

from __future__ import print_function

import sys
from timeit import timeit
from glob import glob

REPEAT = 10**5
CMD = '''LineItem('sesame seed', 250, 5.30)'''
SETUP = '''from bulkfood import LineItem'''

print('Criando %s instâncias em cada passo' % REPEAT)
print()
print('-----  -----  ------------')
print('passo  tempo  inst/segundo')
print('-----  -----  ------------')
for i, dir_name in enumerate(glob('?')):
    sys.path.append(dir_name)
    if i == 0:
        import bulkfood
    else:
        reload(bulkfood)
    t = timeit(CMD, SETUP, number=REPEAT)
    print('%3d    %.3f %11d' % (i, t, REPEAT/t))
    sys.path.pop()
print('-----  -----  ------------')
