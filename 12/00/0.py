from collections import UserDict

class HumanUD(UserDict):
    def __init__(self, d):
        self.data = {}
        if isinstance(d, dict):
            self.data.update(d)

class HumanD(dict):
    def __init__(self, d):
        if isinstance(d, dict):
            self.update(d)


d = {'name':'Yamada', 'age':100}
hud = HumanUD(d)
hd = HumanD(d)
print(hud)
print(hd)
