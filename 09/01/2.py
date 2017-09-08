import collections

def delete_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)

d = collections.deque('abcdefg')
print(d)
delete_nth(d, 3)
print(d)
