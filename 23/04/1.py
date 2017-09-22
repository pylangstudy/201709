import reprlib
r = reprlib.Repr()
print(r)
print(r.maxdict)
print(r.maxlist)
print(r.maxtuple)
print(r.maxset)
print(r.maxfrozenset)
print(r.maxdeque)
print(r.maxarray)

print(r.maxlong)
print(r.maxstring)
print(r.maxother)
print(r.repr)
print(r.repr1)
print(r.repr_TYPE({}, 0))#AttributeError: 'Repr' object has no attribute 'repr_TYPE'
