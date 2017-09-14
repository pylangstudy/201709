import bisect
import random
random.seed(1)
l = []
for i in range(1, 10):
    r = random.randint(1, 100)
    position = bisect.bisect(l, r)
    bisect.insort(l, r)
    print('%2d %2d' % (r, position), l)

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect.bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect.bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect.bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

#l = [9, 16, 18, 33, 58, 64, 73, 98, 98]
print(index(l, 18))#値18の位置
print(find_lt(l, 18))#値18より小さい最近値
print(find_le(l, 18))#値18以下の最近値
print(find_gt(l, 18))#値18より大きい最近値
print(find_ge(l, 18))#値18以上の最近値
