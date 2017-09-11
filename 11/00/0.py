from collections import OrderedDict

#d = OrderedDict(['a','b','c','d'])#ValueError: need more than 1 value to unpack
#d = OrderedDict(*['a','b','c','d'])#TypeError: expected at most 1 arguments, got 4
d = OrderedDict([('a', 4),('b',3),('c',2),('d',1)])
print(d)
for k,v in d.items(): print(k,v)

for i in range(len(d)): print(d.popitem())
print(d)
d = OrderedDict([('a', 4),('b',3),('c',2),('d',1)])#TypeError: expected at most 1 arguments, got 4
for i in range(len(d)): print(d.popitem(last=False))
print(d)

d = OrderedDict([('a', 4),('b',3),('c',2),('d',1)])#TypeError: expected at most 1 arguments, got 4
d.move_to_end('a')
print(d)
d.move_to_end('a', last=False)
print(d)

for key in reversed(d): print(key)
