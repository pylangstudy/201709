from decimal import *
getcontext().prec = 6
print(Decimal(1) / Decimal(7))
getcontext().prec = 28
print(Decimal(1) / Decimal(7))

