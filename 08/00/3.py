import collections
c = collections.Counter(a=2, b=-4, c=0)
print(' c', c)
print('+c', +c)#Counter({'a': 2})
print('-c', -c)#Counter({'b': 4})
# 分かりにくすぎる。-cはどういうときに使うんだ？
