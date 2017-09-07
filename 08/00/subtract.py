import collections

c = collections.Counter(a=4, b=2, c=0, d=-2)
d = collections.Counter(a=1, b=2, c=3, d=4)
print(c)
print(d)
c.subtract(d)
print(c)

c = collections.Counter(cats=4, dogs=8)
print(c)
c.subtract(collections.Counter(cats=3, dogs=1))
print(c)

c = collections.Counter('a b c d a a a c'.split())
print(c)
c.subtract(collections.Counter(a=3))
print(c)

