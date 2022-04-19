



from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')

tokyo = City('Tykyo', 'JP', 36.933, (35.689722, 139.691667))

print(tokyo)

print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])

print(tokyo._fields)
print('*'*20)

Latlong = namedtuple('Latlong','lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, Latlong(28.613889,77.208899))

delhi = City._make(delhi_data)

# _asdict() 可以将具名元组转为collections.Orderdict 
print(delhi._asdict())

for key, value in delhi._asdict().items():
    print(key + ':' , value)

