from collections import defaultdict
s = 'mississippi'
d = defaultdict(int)
for k in s: d[k] += 1
print(sorted(d.items()))

