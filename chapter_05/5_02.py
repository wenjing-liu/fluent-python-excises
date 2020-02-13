def factorical(n):
  '''return n!'''
  return 1 if n < 2 else n * factorical(n - 1)


fact = factorical
print(fact)
print(fact(5))
print(map(factorical, range(11)))
print(list(map(fact, range(11))))