from enum import Enum
class UserClass: pass
Animal = Enum(value='Animal', names='ANT BEE CAT DOG', module=__name__, qualname=UserClass.__qualname__+'.Animal', start=100)
print(Animal)
print(Animal.ANT)
print(Animal.ANT.value)
print(list(Animal))
print()

Animal2 = Enum(value='Animal', names='ANT BEE CAT DOG', type=UserClass)
print(Animal2)
print(Animal2.ANT)
print(Animal2.ANT.value)
print(list(Animal2))
