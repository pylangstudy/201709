from enum import Flag, auto
class Color(Flag):
    BLACK = 0
    RED = auto()
    BLUE = auto()
    GREEN = auto()
    WHITE = RED | BLUE | GREEN

print(Color.BLACK)
print(bool(Color.BLACK))

print(Color.RED.value)
print(Color.BLUE.value)
print(Color.GREEN.value)
print(Color.WHITE.value)
