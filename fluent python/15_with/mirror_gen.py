# -*- coding: utf-8 -*-

import contextlib


@contextlib.contextmanager
def looking_glass():
    import sys
    orignal_write = sys.stdout.write

    def reverse_write(text):
        orignal_write(text[::-1])

    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    sys.stdout.write = orignal_write
