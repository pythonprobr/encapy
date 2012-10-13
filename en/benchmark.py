# coding: utf-8

import sys
from timeit import timeit

REPEAT = 10**5
CMD = '''ItemPedido('gergelim', 250, 5.30)'''
SETUP = '''from granel import ItemPedido'''

print 'Criando %s instâncias em cada passo' % REPEAT
print
print '-----  -----  ------------'
print 'passo  tempo  inst/segundo'
print '-----  -----  ------------'
for i in range(1, 7):
    sys.path.append(str(i))
    if i == 1:
        import granel
    else:
        reload(granel)
    t = timeit(CMD, SETUP, number=REPEAT)
    print '%3d    %.3f %11d' % (i, t, REPEAT/t)
    sys.path.pop()
print '-----  -----  ------------'
