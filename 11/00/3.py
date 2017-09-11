from collections import OrderedDict
from collections import Counter

class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first encountered'

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)

d = OrderedCounter([('a', 4),('b',3)])
print(d)
d['c'] = 2
print(d)
d['a'] = 5
print(d)

