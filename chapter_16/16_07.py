from functools import wraps

def coroutine(func):
  @wraps(func)
  def primer(*args, **kwargs):
    gen = func(*args, **kwargs)
    next(gen)
    return gen
  return primer

@coroutine
def averager():
  total = 0.0
  count = 0
  average = None
  while True:
    term = yield average
    total += term
    count += 1
    average = total/count

coro_avg = averager()
print(coro_avg.send(40))
print(coro_avg.send(50))
coro_avg.send('spam')
coro_avg.send(60)