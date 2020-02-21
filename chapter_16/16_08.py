from inspect import getgeneratorstate
class DemoException(Exception):
  """演示定义的异常类型"""

def demo_exc_handling():
    print('-> coroutine started')
    try:
      while True:
        try:
          x = yield
        except DemoException:
          print('*** DemoException handled. Contining...')
        else:
          print('-> coroutine received: {!r}'.format(x))
      raise RuntimeError('This line should never run.')
    finally:
      print('-> coroutine ending')

exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(11)
# exc_coro.send(22)
# exc_coro.close()
#exc_coro.throw(DemoException)
exc_coro.throw(ZeroDivisionError)
print(getgeneratorstate(exc_coro))