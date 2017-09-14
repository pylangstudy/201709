import bisect
import random
random.seed(1)
l = []
for i in range(1, 10):
    r = random.randint(1, 100)
    position = bisect.bisect(l, r)
    bisect.insort(l, r)
    print('%2d %2d' % (r, position), l)
