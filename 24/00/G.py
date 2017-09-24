from enum import Enum
Animal = Enum('Animal', 'ANT BEE CAT DOG')
print(Animal)
print(Animal.ANT)
print(Animal.ANT.value)
print(list(Animal))
