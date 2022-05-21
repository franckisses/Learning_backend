# -*- coding: utf-8 -*-
import collections
import queue
import random
import argparse
import time

Event = collections.namedtuple('Event', 'time proc action')

DEFAULT_NUMBER_OF_TAXIS = 3
DEPARTURE_INTERVAL = 5
DEFAULT_END_TIME = 180
SEARCH_DURATION = 5
TRIP_DURATION = 20


"""
<BS>>>> from taxi_sim import *
>>> taxi = taxi_process(ident=13,trips=2,start_time=0)
>>> next(taxi)
Event(time=0, proc=13, action='level garage')
>>> taxi.send(_.time +7)
Event(time=7, proc=13, action='pick up passenger')
>>> taxi.send(_.time + 23)
Event(time=30, proc=13, action='drop off passenger')
>>> taxi.send(_.time + 5)
Event(time=35, proc=13, action='pick up passenger')
>>> taxi.send(_.time + 48)
Event(time=83, proc=13, action='drop off passenger')
>>> taxi.send(_.time + 1)
Event(time=84, proc=13, action='going home')
>>> taxi.send(_.time + 10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
"""


def taxi_process(ident, trips, start_time=0):
    """每次状态改变时创建事件，把控制权让给仿真器"""
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')
    yield Event(time, ident, 'going home')

class Simulator:
    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):
        """排定并显示事件，直到时间结束"""
        # 排定各辆出租车的第一个事件
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)

        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break

            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print('taxi:', proc_id, proc_id*' ',current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time: {} events pending'
            print(msg.format(self.events.qsize()))

def compute_duration(previous_action):
    """使用指数分布计算操作耗时"""
    if previous_action in ['leave garage', 'drop off passenger']:
        # 新状态四处徘徊
        interval = SEARCH_DURATION
    elif previous_action == 'pick up passenger':
        # 新状态是行程开始
        interval = TRIP_DURATION
    elif previous_action == 'going home':
        interval = 1
    else:
        raise ValueError('unknow previous_action: %s'% previous_action)
    return int(random.expovariate(1/interval)) +1

def main(end_time=DEFAULT_END_TIME, num_taxis=DEFAULT_NUMBER_OF_TAXIS,
        seed=None):
    """初始化随机生成器，构建过程，运行仿真程序"""
    if seed is not None:
        random.seed(seed) # 获得可复现的结果

    taxis = {i: taxi_process(i, (i + 1) * 2, i * DEPARTURE_INTERVAL)
        for i in range(num_taxis)}

    sim = Simulator(taxis)
    sim.run(end_time)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Taxi fleet simulator')

    parser.add_argument('-e', '--end-time', type=int,
        default=DEFAULT_END_TIME,help='simulation end time;default=%s'%
        DEFAULT_END_TIME)

    parser.add_argument('-t', '--taxis', type=int,
        default=DEFAULT_NUMBER_OF_TAXIS,
        help='number of taxis running;default=%s' % DEFAULT_NUMBER_OF_TAXIS)

    parser.add_argument('-s', '--seed', type=int, default=None, help='random\
        generator seed (for testing)')

    args = parser.parse_args()
    main(args.end_time, args.taxis, args.seed)

