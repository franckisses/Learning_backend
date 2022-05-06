
def make_averager():
    series = []
   
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager
'''
>>> from example_7_9 import *
>>> avg = make_averager()
>>> avg(10)
10.0
>>> avg(11)
10.5
>>> avg(12)
11.0
>>> avg.__code__.co_varnames
('new_value', 'total')
>>> avg.__code__.co_freevars
('series',)
>>> avg.__closure__
(<cell at 0x7f84ad574fd8: list object at 0x7f84ad5ac048>,)
>>> avg.__closure__[0].cell_contents
[10, 11, 12]
'''
