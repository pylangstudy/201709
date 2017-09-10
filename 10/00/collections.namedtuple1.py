from collections import namedtuple

# Basic example
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)     # instantiate with positional or keyword arguments
print(p)
print(p[0] + p[1])             # indexable like the plain tuple (11, 22)
x, y = p                # unpack like a regular tuple
print(x, y)
print(p.x + p.y)               # fields also accessible by name
print(p)                       # readable __repr__ with a name=value style
Point(x=11, y=22)
