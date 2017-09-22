import pprint
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff)
pprint.pprint(stuff)

print(pprint.isreadable(stuff))
print(pprint.saferepr(stuff))
