

import random

class BingoCage:
    def __init__(self, items):
        self.__items = list(items)
        random.shuffle(self.__items)


    def pick(self):
        try: 
            return self.__items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()

In [1]: from example_5_8 import *                                                                                                 

In [3]: bingo = BingoCage(range(3))                                                                                               

In [4]: bingo.pick()                                                                                                              
Out[4]: 0

In [5]: bingo()                                                                                                                   
Out[5]: 1

In [6]: callable(bingo)                                                                                                           
Out[6]: True
