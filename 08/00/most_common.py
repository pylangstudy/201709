import collections

c = collections.Counter(cats=4, dogs=8)
print(c)
print(c.most_common())

c = collections.Counter('a b c d a a a c'.split())
print(c)
print(c.most_common())
