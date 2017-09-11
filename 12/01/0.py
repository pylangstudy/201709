from collections import UserList

class HumanUL(UserList):
    def __init__(self, l):
        self.data = []
        if isinstance(l, list):
            self.data += l

class HumanL(list):
    def __init__(self, l):
        if isinstance(l, list):
            self += l


l = [0,1,2]
hul = HumanUL(l)
hl = HumanL(l)
print(hul)
print(hl)
