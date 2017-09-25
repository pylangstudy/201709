from enum import IntFlag
class Perm(IntFlag):
    R = 4
    W = 2
    X = 1
print(Perm.R | Perm.W)
print(Perm.R + Perm.W)
RW = Perm.R | Perm.W
print(Perm.R in RW)
