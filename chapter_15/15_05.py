import contextlib

@contextlib.contextmanager
def looking_glass:
  import sys
  self.original_write = sys.stdout.write
  sys.stdout.write = self.reverse_write

  def reverse_write(self, text):
    self.original_write(text[::-1])
  
  sys.stdout.write = reverse_write
  yield 'JABBERWOCKY'
  sys.stdout.write = self.original_write