with open('test.py') as fp:
  src = fp.read(60)

print(len(src))
print(fp)
fp.read(60)