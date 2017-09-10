from collections import namedtuple
Point = namedtuple('Point', ['x','y'])
d = {'x': 11, 'y': 22}
p = Point(**d)
print(p)
