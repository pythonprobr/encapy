from __future__ import print_function

import sys
from timeit import timeit
from glob import glob

from imp import reload

REPEAT = 10**6
SETUP = '''from bulkfood import LineItem'''
CMD = '''LineItem('sesame seed', 250, 5.30).subtotal()'''

print('Creating %s instances in each step' % REPEAT)
print()
print('-----  -----  -----------')
print('step   time   inst/second')
print('-----  -----  -----------')
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
