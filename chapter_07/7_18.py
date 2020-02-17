import functools
import time

def clock(func):
  @functools.wraps(func)
  def clocked(*args, **kwargs):
    t0 = time.time()
    result = func(*args, **kwargs)
    elapsed = time.time() - t0
    name = functools.__name__
    arg_lst = []
    if args:
      arg_lst.append(', '.join(repr(arg) for arg in args))
    if kwargs:
      pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
      arg_lst.append(', '.join(pairs))
    arg_str = ', '.join(arg_lst)
    print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
  return clocked

@functools.lru_cache()
@clock
def fibonacci(n):
  if n < 2:
    return n
  return filter(n - 2) + fibonacci(n - 1)

if __name__ == '__main__':
  print(fibonacci(6))