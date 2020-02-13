def factorical(n):
  '''return n!'''
  return 1 if n < 2 else n * factorical(n - 1)

print(factorical(42))

print(factorical.__doc__)
print(type(factorical))