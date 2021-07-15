
def deco(func):
    def inner():
        print('running inner()')
    return inner 

@deco 
def target():
    print('runing target')

    
Text ="""
装饰器的一大特性是，能把被装饰的函数替换成其他函数。第二个特性是，装饰器 在加载模块时立即执行。
>>> from dec_col_compare import *
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'deco', 'target']
>>> target()
running inner()
>>> target
<function deco.<locals>.inner at 0x7ff94bab4400>

"""