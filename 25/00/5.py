from enum import Flag, auto
class Color(Flag):
    RED = auto()
    BLUE = auto()
    GREEN = auto()
    WHITE = RED | BLUE | GREEN

print(Color.RED.value)
print(Color.BLUE.value)
print(Color.GREEN.value)
print(Color.WHITE.value)
