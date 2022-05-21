# -*- coding: utf-8 -*-
class DemoException(Exception):
    """为这次演示定义的异常类型"""

def demo_finally():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled.continuing...')
            else:
                print('-> coroutine received:{!r}'.format(x))
    finally:
        print('-->coroutine ending')
