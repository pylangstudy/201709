from enum import Flag, auto
class Color(Flag):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    MAGENTA = RED | BLUE
    YELLOW = RED | GREEN
    CYAN = GREEN | BLUE

print(Color.RED.value)#1
print(Color.GREEN.value)#2
print(Color.BLUE.value)#4
print(Color.MAGENTA.value)#5
print(Color.YELLOW.value)#3
print(Color.CYAN.value)#6

print(Color(3))
print(Color(7))
print(Color(7).value)
print((Color.CYAN|Color.MAGENTA|Color.BLUE|Color.YELLOW|Color.GREEN|Color.RED).value)#7(0b111)
print((Color.BLUE|Color.GREEN|Color.RED).value)#7(0b111)
print(Color(8).value)#ValueError: 8 is not a valid Color
