from timeit import timeit
stmt = '''BulkItem('Golden raisins', 10, 36.95)'''
setup = '''from bulkfood import BulkItem'''
print(timeit(stmt, setup))
