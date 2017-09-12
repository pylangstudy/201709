import collections.abc
myvar = [1,2,3]
if isinstance(myvar, collections.abc.Sized): print(f'size: {len(myvar)}')
else: print('not collections.abc.Sized.')
