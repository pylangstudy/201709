import types

mpt = types.MappingProxyType({'k1': 'v1'})
print(mpt)
print('k1' in mpt)
print(mpt['k1'])
print(iter(mpt))
print(len(mpt))
print(mpt.copy())
print(mpt.get('k1'))
print(mpt.items())
print(mpt.keys())
print(mpt.values())
