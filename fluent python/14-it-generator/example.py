# -*- coding: utf-8 -*-
>>> def vowel(c):
...     return c.lower() in 'aeiou'
...
>>> list(filter(vowel, 'Aardvark')
... )
['A', 'a', 'a']
>>> import itertools
>>> list(itertools.filterfalse(vowel, 'Aadvark'))
['d', 'v', 'r', 'k']
>>> list(itertools.dropwhile(vowel, 'Aadvark'))
['d', 'v', 'a', 'r', 'k']
>>> list(itertools.takewhile(vowel, 'Aardvark'))
['A', 'a']
>>> list(itertools.compress('Aardvark', (1,0,1,1,0,1))
... )
['A', 'r', 'd', 'a']
>>> list(itertools.islice('Aardvark',4))
['A', 'a', 'r', 'd']
>>> list(itertools.islice('Aardvark',4,7))
['v', 'a', 'r']
>>> list(itertools.islice('Aardvark',1,7,2))
['a', 'd', 'a']
>>> sample = [5,4,2,8,7,6,3,0,9,1]
>>> import itertools
>>> list(itertools.accumulate(sample))
[5, 9, 11, 19, 26, 32, 35, 35, 44, 45]
>>> list(itertools.accumulate(sample, min))
[5, 4, 2, 2, 2, 2, 2, 0, 0, 0]
>>> list(itertools.accumulate(sample, max))
[5, 5, 5, 8, 8, 8, 8, 8, 9, 9]
>>> list(itertools.accumulate(sample, operator.mul))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'operator' is not defined
>>> import operator
>>> list(itertools.accumulate(sample, operator.mul))
[5, 20, 40, 320, 2240, 13440, 40320, 0, 0, 0]
>>> list(itertools.accumulate(range(1,11), operator.mul)
... )
[1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
>>> list(enumerate('albatroz',1))
[(1, 'a'), (2, 'l'), (3, 'b'), (4, 'a'), (5, 't'), (6, 'r'), (7, 'o'), (8, 'z')]
>>> list(enumerate('albatroz',2))
[(2, 'a'), (3, 'l'), (4, 'b'), (5, 'a'), (6, 't'), (7, 'r'), (8, 'o'), (9, 'z')]
>>> list(enumerate('albatroz',4))
[(4, 'a'), (5, 'l'), (6, 'b'), (7, 'a'), (8, 't'), (9, 'r'), (10, 'o'), (11, 'z')]
>>> list(map(operator.mul, range(1,11), [2, 4, 8]))
[2, 8, 24]
>>> list(map(lambda a,b :(a,b), range(11), [2,4,8]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'itertools' has no attribute 'starmp'
>>> list(itertools.starmap(operator.mul, enumerate('albatroz',1)))
['a', 'll', 'bbb', 'aaaa', 'ttttt', 'rrrrrr', 'ooooooo', 'zzzzzzzz']
>>> list(itertools.starmap(lambda a,b: b/a, enumerate(itertools.accumulate(sample),1)))
[5.0, 4.5, 3.6666666666666665, 4.75, 5.2, 5.333333333333333, 5.0, 4.375, 4.888888888888889, 4.5]
>>> list(itertools.chain('ABC', range(2)))
['A', 'B', 'C', 0, 1]
>>> list(itertools.chain(enumerate('ABC'))
... )
[(0, 'A'), (1, 'B'), (2, 'C')]
>>> list(itertools.chain.from_iterable(enumerate('ABC')))
[0, 'A', 1, 'B', 2, 'C']
>>> list(zip('ABC', range(5)))
[('A', 0), ('B', 1), ('C', 2)]
>>> list(zip('ABC', range(5), [10,20,30,40]))
[('A', 0, 10), ('B', 1, 20), ('C', 2, 30)]
>>> list(itertools.zip_longest('ABC', range(5)))
[('A', 0), ('B', 1), ('C', 2), (None, 3), (None, 4)]
>>> list(itertools.zip_longest('ABC', range(5), fillvalue='?'))
[('A', 0), ('B', 1), ('C', 2), ('?', 3), ('?', 4)]
>>>
>>>
>>> list(itertools.product('ABC', range(2)))
[('A', 0), ('A', 1), ('B', 0), ('B', 1), ('C', 0), ('C', 1)]
>>> suits = 'spades hearts diamonds clubs'.split()
>>> suits
['spades', 'hearts', 'diamonds', 'clubs']
>>> list(itertools.product('ABC', suits))
[('A', 'spades'), ('A', 'hearts'), ('A', 'diamonds'), ('A', 'clubs'), ('B', 'spades'), ('B', 'hearts'), ('B', 'diamonds'), ('B', 'clubs'), ('C', 'spades'), ('C', 'hearts'), ('C', 'diamonds'), ('C', 'clubs')]
>>> list(itertools.product('ABC'))
[('A',), ('B',), ('C',)]
>>> list(itertools.product('ABC', repeat=2))
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
>>> list(itertools.product(range(2), repeat=3)
... )
[(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
>>> rows = itertools.product('AB', range(2), repeat=2)
>>> for row in rows:print(row)
...
('A', 0, 'A', 0)
('A', 0, 'A', 1)
('A', 0, 'B', 0)
('A', 0, 'B', 1)
('A', 1, 'A', 0)
('A', 1, 'A', 1)
('A', 1, 'B', 0)
('A', 1, 'B', 1)
('B', 0, 'A', 0)
('B', 0, 'A', 1)
('B', 0, 'B', 0)
('B', 0, 'B', 1)
('B', 1, 'A', 0)
('B', 1, 'A', 1)
('B', 1, 'B', 0)
('B', 1, 'B', 1)
>>> ct = itertools.count()
>>> ct
count(0)
>>> next(ct), next(ct), next(ct)
(0, 1, 2)
>>> list(itertools.islice(itertools.count(1,0.3),3))
[1, 1.3, 1.6]
>>> cy = itertools.cycle('ABC')
>>> cy
<itertools.cycle object at 0x7fc767667708>
>>> next(cy)
'A'
>>> next(cy)
'B'
>>> next(cy)
'C'
>>> next(cy)
'A'
>>> next(cy)
'B'
>>> next(cy)
'C'
>>> next(cy)
'A'
>>> next(cy)
'B'
>>> next(cy)
'C'
>>> next(cy)
'A'
>>> next(cy)
'B'
>>> next(cy)
'C'
>>> next(cy)
'A'
>>> list(itertools.islice(cy,7))
['B', 'C', 'A', 'B', 'C', 'A', 'B']
>>> rp = itertools.repeat(7)
>>> rp
repeat(7)
>>> next(rp), next(rp)
(7, 7)
>>> list(itertools.repeat(8,4))
[8, 8, 8, 8]
>>> list(map(operator.mul, range(11), itertools.repeat(5)))
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
>>> list(itertools.combinations('ABC', 2))
[('A', 'B'), ('A', 'C'), ('B', 'C')]
