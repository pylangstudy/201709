from enum import Enum
class Color(Enum):
    RED = 100
    GREEN = 200
    BLUE = 300

print(Color.RED)
print(repr(Color.RED))
print(type(Color.RED))
print(isinstance(Color.GREEN, Color))
print(Color.RED.name)
print(Color.RED.value)

for c in Color: print(c)

apples = {}
apples[Color.RED] = 'red delicious'
apples[Color.GREEN] = 'granny smith'
apples == {Color.RED: 'red delicious', Color.GREEN: 'granny smith'}
print(apples)
