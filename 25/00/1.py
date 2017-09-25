from enum import Enum, IntEnum
class Shape(IntEnum):
    CIRCLE = 1
    SQUARE = 2
class Color(Enum):
    RED = 1
    GREEN = 2
print(Shape.CIRCLE == Color.RED)
