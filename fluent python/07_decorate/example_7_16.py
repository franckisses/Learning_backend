
import time
from example_7_15 import clock


@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
   return 1 if n < 2 else n*factorial(n-1)


if __name__ == '__main__':
    print('*' * 40, 'calling snooze(0.123)')
    snooze(0.123)
    print('*' * 40, 'calling factorial(6)')
    print('6!',factorial(6))
