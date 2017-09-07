import collections

c = collections.Counter(a=100, b=90)

c = collections.Counter(a=3, b=1)
d = collections.Counter(a=1, b=2)
print(c)
print(d)
print('+', c + d)                       # add two counters together:  c[x] + d[x]
print('-', c - d)                       # subtract (keeping only positive counts)
print('&', c & d)                       # intersection:  min(c[x], d[x]) 
print('|', c | d)                       # union:  max(c[x], d[x])

# 代入では負数が消えないのに、演算だと負数は消える。使うメソッドごとに結果が異なるのはわかりづらいし使いづらい。
