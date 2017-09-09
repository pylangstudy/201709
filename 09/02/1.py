from collections import defaultdict
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print(s)

print('----- defaultdict() -----')
d = defaultdict(list)
for k, v in s: d[k].append(v)
print(sorted(d.items()))

print('----- setdefault() -----')
#s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = {}
for k, v in s: d.setdefault(k, []).append(v)
print(sorted(d.items()))
