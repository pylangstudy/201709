from enum import IntEnum
class Shape(IntEnum):
    CIRCLE = 1
    SQUARE = 2
class Request(IntEnum):
    POST = 1
    GET = 2
print(Shape == 1)
print(Shape.CIRCLE == 1)
print(Shape.CIRCLE == Request.POST)

print(int(Shape.CIRCLE))
print(['a', 'b', 'c'][Shape.CIRCLE])
print([i for i in range(Shape.SQUARE)])
