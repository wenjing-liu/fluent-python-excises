symbols = '$¢£¥€¤'

beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print('list generate: ', beyond_ascii)

beyond_ascii_filter_map = list(filter(lambda  c: c > 127, map(ord, symbols)))

print('filter map: ', beyond_ascii_filter_map)