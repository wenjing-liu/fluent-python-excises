import array

symbols = '$¢£¥€¤'
single_param = tuple(ord(symbol) for symbol in symbols)
print(single_param)

multiple_params = array.array('I', (ord(symbol) for symbol in symbols))
print(multiple_params)