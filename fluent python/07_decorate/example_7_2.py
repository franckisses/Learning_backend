
registery = []

def register(func):
    print('runing register(%s)' % func)
    registery.append(func)
    return func 


@register
def f1():
    print('runing f1()')


@register
def f2():
    print('runing f2()')

def f3():
    print('running f3()')

def main():
    print('running main()')
    print('registery -->', registery)
    f1()
    f2()
    f3()

if __name__ == '__main__':
    # main()
    pass 
