from enum import Enum
class Color(Enum):
    RED = 100
    GREEN = 200
    BLUE = 300

print(Color.RED is Color.RED)
print(Color.RED is Color.BLUE)
print(Color.RED is not Color.BLUE)
print(Color.RED == Color.RED)
print(Color.RED == Color.BLUE)
print(Color.RED != Color.BLUE)
#print(Color.RED < Color.BLUE)#TypeError: '<' not supported between instances of 'Color' and 'Color'
print(Color.RED == 100)#非列挙型の値との比較は常に不等となります(それを望むならIntEnumを使う)
print(Color.RED.value == 100)

