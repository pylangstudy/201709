import collections

c = collections.Counter()                           # a new, empty counter
print(c)
c = collections.Counter('gallahad')                 # a new counter from an iterable
print(c)
c = collections.Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
print(c)
c = collections.Counter(cats=4, dogs=8)             # a new counter from keyword args
print(c)
print(c['bacon'])#存在しないものは0が返る
print(c['cats'])
c['cats'] = 0#0を指定しても消えない
print(c)
del c['cats']#delでキーごと消える
print(c)

