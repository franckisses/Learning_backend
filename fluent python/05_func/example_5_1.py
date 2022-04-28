

def factorial(n):
    '''return n!'''
    return 1 if n < 2 else n * factorial(n-1)



""">>> import example_5_1
>>> dir
<built-in function dir>
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'example_5_1']
>>> from example_5_1 import *
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'example_5_1', 'factorial']
>>> factorial(42)
1405006117752879898543142606244511569936384000000000
>>> factorial.__doc__
'return n!'
>>> type(factorial)
<class 'function'>
>>> help(factorial)
"""
