
t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])

print('=', t1 == t2)

print(id(t1[-1]))

t1[-1].append(99)


print('t1:', t1)
print('t2:', t2)

print(t1 == t2)
