
registery = []

def register(func):
    print('running register(%s)' % func)
    registery.append(func)
    return func

@register
def f1():
    print('running f1()')


print('running main')
print('register ->', registery)
f1()
