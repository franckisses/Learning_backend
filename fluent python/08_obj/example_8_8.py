import copy

class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)



bus1 = Bus(['alice', 'bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)

print('id bus1',id(bus1), 'id bus2', id(bus2), 'id bus3', id(bus3))

print(bus1.drop('bill'))

print('bus1', bus1.passengers)
print('bus2', bus2.passengers)
print('bus3', bus3.passengers)

print(id(bus1.passengers))
print(id(bus2.passengers))
print(id(bus3.passengers))

print(bus3.passengers)
