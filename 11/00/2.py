from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):
    'Store items in the order the keys were last added'

    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        OrderedDict.__setitem__(self, key, value)

d = LastUpdatedOrderedDict([('a', 4),('b',3)])
print(d)
d['c'] = 2
print(d)
d['a'] = 5
print(d)

