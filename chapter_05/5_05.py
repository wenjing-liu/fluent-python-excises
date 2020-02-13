def factorical(n):
  '''return n!'''
  return 1 if n < 2 else n * factorical(n - 1)


fact = factorical

print(list(map(fact, range(6))))

print([fact(n) for n in range(6)])

print(list(map(factorical, filter(lambda n: n % 2, range(6)))))

print([factorical(n) for n in range(6) if n % 2])