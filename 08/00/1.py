import collections

c = collections.Counter(a=100, b=90)
print(sum(c.values()))                 # total of all counts
c.clear()                       # reset all counts
print(c)
c = collections.Counter(a=100, b=90)
print(list(c))                         # list unique elements
print(set(c))                          # convert to a set
print(dict(c))                         # convert to a regular dictionary
print(c.items())                       # convert to a list of (elem, cnt) pairs
c = collections.Counter(dict([('a',9),('b',6),('c',3),('d',0),('e',-30)]))    # convert from a list of (elem, cnt) pairs
print(c)
print(c.most_common()[1:3])       # n least common elements
print(+c)                              # remove zero and negative counts

#+cはわかりにくすぎる。
