from enum import Enum
class Shape(Enum):
    SQUARE = 2
    DIAMOND = 1
    CIRCLE = 3
    ALIAS_FOR_SQUARE = 2
print(list(Shape))

for name, member in Shape.__members__.items():
    print(name, member)

print([name for name, member in Shape.__members__.items() if member.name != name])
