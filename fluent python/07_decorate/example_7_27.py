
import time
from example_7_25 import clock

@clock('{name}{args} dt={elapsed:0.3f}s')
def snooze(second):
    time.sleep(second)


for i in range(3):
    snooze(0.123)
