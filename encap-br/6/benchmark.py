from timeit import timeit
n = 10**5
cmd = '''ItemPedido('gergelim', 250, 5.30)'''
setup = '''from granel import ItemPedido'''
t = timeit(cmd, setup, number=n)
print '%d instancias criadas em %.3fs' % (n, t)
print '%d instancias por segundo' % (n/t)
