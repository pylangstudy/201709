from enum import IntFlag
class Perm(IntFlag):
    R   = 0b100
    W   = 0b010
    X   = 0b001
    RWX = 0b111
print(Perm.R | Perm.W)
print(Perm.R + Perm.W)
RW = Perm.R | Perm.W
print(Perm.R in RW)

print(Perm.RWX)
print(~Perm.RWX)

print(Perm.R & Perm.X)#定義に宣言がないと0になる！
print((Perm.R & Perm.X).value)
print(bool(Perm.R & Perm.X))#定義に宣言がないとFalseになる！

print(Perm.X | 8)
