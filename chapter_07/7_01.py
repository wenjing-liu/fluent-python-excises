def deco(func):
  func()
  def inner():
    print('running inner()')
  return inner

@deco
def target():
  print('running target()')

print(target())
print(target)