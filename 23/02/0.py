import pprint
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter()
print(pp.pformat(stuff))
pp.pprint(stuff)
print(pp.isreadable(stuff))
print(pp.isrecursive(stuff))
print(pp.format(stuff, locals(), 0, 0))
