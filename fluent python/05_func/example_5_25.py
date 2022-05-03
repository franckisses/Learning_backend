
from operator import methodcaller

s = 'the time has come'
upcase = methodcaller('upper')
print(upcase(s))

hiphenate = methodcaller('replace', ' ', '_')

print(hiphenate(s))
