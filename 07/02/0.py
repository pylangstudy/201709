import collections
import builtins
pylookup = collections.ChainMap(locals(), globals(), vars(builtins))
print(pylookup)
