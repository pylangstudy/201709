import collections
dq = collections.deque(['A','B','C'])

# count(element)
print(dq.count('A'))
print(dq.count('X'))

# copy()
dq2 = dq.copy()
dq2.append('D')
print('dq :', dq)
print('dq2:', dq2)
dq2[0] = 'a'
print('dq :', dq)
print('dq2:', dq2)

# index(element)
print(dq.index('C'))
#print(dq.index('X'))#ValueError: 'X' is not in deque

# remove()
dq.remove('A')
print(dq)
#dq.remove('X')#ValueError: deque.remove(x): x not in deque
print(dq.maxlen)#制限なしならNone。例外や-1ではない点が統一性の無さを感じる。

print(len(dq))
import copy
dq3 = copy.copy(dq)
dq3.append('D')
print('dq :', dq)
print('dq3:', dq3)
dq3[0] = 'b'
print('dq :', dq)
print('dq3:', dq3)
dq4 = copy.deepcopy(dq)
dq4.append('E')
print('dq :', dq)
print('dq4:', dq4)
dq4[0] = 'b'
print('dq :', dq)
print('dq4:', dq4)

