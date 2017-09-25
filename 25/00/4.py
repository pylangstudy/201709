from enum import Flag, auto
class Color(Flag):
    RED = auto()
    BLUE = auto()
    GREEN = auto()

print(Color.RED & Color.GREEN)
print(bool(Color.RED & Color.GREEN))
