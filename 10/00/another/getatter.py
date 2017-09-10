from collections import namedtuple
Point = namedtuple('Point', ['x','y'])
p = Point(100,200)
print(getattr(p, 'x'))
