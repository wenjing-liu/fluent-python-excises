b = 6

# def f2(a):
#   print(a)
#   print(b)
#   b = 9
# f2(3)


def f3(a):
  global b
  print(a)
  print(b)
  b = 9

f3(3)