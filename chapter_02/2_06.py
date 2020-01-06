colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for t_shirt in ('%s %s' % (c, s) for c in colors for s in sizes):
  print(t_shirt)
