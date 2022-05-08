
registery = set()

def register(active=True):
    def decorate(func):
        print('running register(active=%s) -- decorate(%s)' % (active,func))
        if active:
            registery.add(func)
        else:
            registery.discard(func)
        return func
    return decorate

@register(active=False)
def f1():
    print('running f1()')


@register()
def f2():
    print('running f2()')

def f3():
    print('running f3()')


'''
>>> from example_7_23 import *
running register(active=False) -- decorate(<function f1 at 0x7fb5de5b5400>)
running register(active=True) -- decorate(<function f2 at 0x7fb5de5b5488>)
>>> registery
{<function f2 at 0x7fb5de5b5488>}
>>> register()(f3)
running register(active=True) -- decorate(<function f3 at 0x7fb5de5b5378>)
<function f3 at 0x7fb5de5b5378>
>>> registery
{<function f2 at 0x7fb5de5b5488>, <function f3 at 0x7fb5de5b5378>}
>>> register(active=False)(f2)
running register(active=False) -- decorate(<function f2 at 0x7fb5de5b5488>)
<function f2 at 0x7fb5de5b5488>
>>> registery
{<function f3 at 0x7fb5de5b5378>}
>>> 
'''
