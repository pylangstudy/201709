from collections import namedtuple
Employee = namedtuple('Employee', 'name,age')
e = Employee('Yamada',10)
print(e._fields)            # view the field names

Point = namedtuple('Point', ['x','y'])
Color = namedtuple('Color', 'red green blue')
Pixel = namedtuple('Pixel', Point._fields + Color._fields)
print(Pixel(11, 22, 128, 255, 0))
