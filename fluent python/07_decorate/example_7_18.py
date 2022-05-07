
from example_7_15 import *

@clock
def fibonacci(n):
    if n < 2:
        return n 
    return fibonacci(n-2) + fibonacci(n-1)


if __name__ == '__main__':
    print(fibonacci(6))

