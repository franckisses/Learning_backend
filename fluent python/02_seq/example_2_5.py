
symbols = '$¢£¥€¤'
tuple_1 = tuple(ord(symbol) for symbol in symbols)
print(tuple_1)


import array 

nary = array.array('I', (ord(symbol) for symbol in symbols))
print(nary)
