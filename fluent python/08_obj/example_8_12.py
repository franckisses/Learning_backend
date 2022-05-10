
class HauntedBus:
    '''备受幽灵乘客折磨的校车'''
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


'''
>>> from example_8_12 import *
>>> bus1 = HauntedBus(['Alice', 'Bill'])
>>> bus1.passengers
['Alice', 'Bill']
>>> bus1.pick('Charlie')
>>> bus1
<example_8_12.HauntedBus object at 0x7fb6ddce4be0>
>>> bus1.passengers
['Alice', 'Bill', 'Charlie']
>>> bus2 = HauntedBus()
>>> bus2.pick('Carrie')
>>> bus2.passengers
['Carrie']
>>> bus3 = HauntedBus()
>>> bus3
<example_8_12.HauntedBus object at 0x7fb6dde964e0>
>>> bus3.passengers
['Carrie']
>>> bus3.pick('Dave')
>>> bus3.passengers
['Carrie', 'Dave']
>>> bus2.passengers in bus3.passengers
False
>>> bus2.passengers
['Carrie', 'Dave']
>>> bus
bus1  bus2  bus3
>>> bus3.passengers
['Carrie', 'Dave']
>>> bus2.passengers is bus3.passengers
True
>>> bus1.passengers
['Alice', 'Bill', 'Charlie']


'''
