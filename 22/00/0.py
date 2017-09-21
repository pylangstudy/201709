import types

print(types.SimpleNamespace)
print(dir(types.SimpleNamespace))

Human = types.SimpleNamespace(**{'Name':'', 'Age':0})
print(Human)
print(dir(Human))
print(Human.Name)
print(Human.Age)
print(Human.__repr__())
print(Human.Name.__repr__())
print(Human.Age.__repr__())
#print(Human())#TypeError: 'types.SimpleNamespace' object is not callable
