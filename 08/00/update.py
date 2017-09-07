import collections

c = collections.Counter(a=4)
print(c)
c.update(a=1)
print(c)
c.update(b=10)
print(c)
c.update(c=1)
print(c)

