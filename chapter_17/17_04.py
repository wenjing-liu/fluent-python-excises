import os
import time
import sys
from concurrent import futures

import requests

POP20_CC = ('CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR CD FR').split()
BASE_URL = 'http://flupy.org/data/flags'
DEST_DIR = './'

MAX_WORKERS = 20

def save_flag(img, filename):
  path = os.path.join(DEST_DIR, filename)
  with open(path, 'wb') as fp:
    fp.write(img)

def get_flag(cc):
  url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
  resp = requests.get(url)
  return resp.content

def show(text):
  print(text, end=' ')
  sys.stdout.flush()

def download_one(cc):
  image = get_flag(cc)
  show(cc)
  save_flag(image, cc.lower() + '.gif')
  return cc

def download_many(cc_list):
  workers = min(MAX_WORKERS, len(cc_list))
  with futures.ThreadPoolExecutor(workers) as executor:
    to_do = []
    for cc in sorted(cc_list):
      future = executor.submit(download_one, cc)
      to_do.append(future)
      msg = 'Scheduled for {}: {}'
      print(msg.format(cc, future))
    
    results = []
    for future in futures.as_completed(to_do):
      res = future.result()
      msg = '{} result: {!r}'
      print(msg.format(future, res))
      results.append(res)

  return len(list(results))

def main(download_many):
  t0 = time.time()
  count = download_many(POP20_CC)
  elapsed = time.time() - t0
  msg = '\n{} flags downloaded in {:.2f}s'
  print(msg.format(count, elapsed))

if __name__ == '__main__':
  main(download_many)