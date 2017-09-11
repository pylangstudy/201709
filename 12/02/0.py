from collections import UserString

class HumanUS(UserString):
    def __init__(self, s):
        if isinstance(s, str): self.data = s

class HumanS(str):
    def __init__(self, s):
        if isinstance(l, str): self = s


l = 'this is string.'
hus = HumanUS(l)
hs = HumanS(l)
print(hus)
print(hs)
