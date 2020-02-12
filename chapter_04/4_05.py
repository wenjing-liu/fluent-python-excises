for codec in ['latin1', 'utf_8', 'utf_16']:
  print(codec, 'El Niño'.encode(codec), sep='\t')