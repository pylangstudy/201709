import copy
class Human:
    def __init__(self, age=0):
        self.age = age

v = [Human()]
c = copy.copy(v)
d = copy.deepcopy(v)
print(v)
print(c)
print(d)

