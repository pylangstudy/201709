from decimal import *
setcontext(ExtendedContext)
print(Decimal(1) / Decimal(0))
print(Decimal('Infinity'))
getcontext().traps[DivisionByZero] = 1
print(Decimal(1) / Decimal(0))
