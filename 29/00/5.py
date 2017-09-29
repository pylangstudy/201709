from decimal import *
data = list(map(Decimal, '1.34 1.87 3.45 2.35 1.00 0.03 9.25'.split()))
print(max(data))
print(min(data))
print(sorted(data))
print(sum(data))
a,b,c = data[:3]
print(str(a))
print(float(a))
print(round(a, 1))
print(int(a))
print(a * 5)
print(a * b)
print(c % a)

