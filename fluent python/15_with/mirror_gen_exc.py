# -*- coding: utf-8 -*-
import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    origanl_write = sys.stdout.write

    def reverse_write(text):
        orignal_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero'
    finally:
        sys.stdout.write = origanl_write
        if msg:
            print(msg)
