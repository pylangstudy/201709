import types

mt = types.ModuleType('mymod')
print(mt)
print(dir(mt))
mt.__doc__ = 'mymodのドキュメント。'
mt.__loader__ = None#https://docs.python.jp/3/glossary.html#term-loader
mt.__name__ = 'MyMod'
mt.__package__ = 'namespace.mypack'
print(mt)
print(dir(mt))
