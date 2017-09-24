from enum import Enum
class Color(Enum):
    RED = 100
    GREEN = 200
    BLUE = 300

print(Color(100))
print(Color(200))
print(Color(300))
print(Color['RED'])
print(Color['GREEN'])
print(Color['BLUE'])
print(Color.RED.name)
print(Color.RED.value)
