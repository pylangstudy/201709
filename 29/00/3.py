from decimal import *
getcontext().prec = 6
print(Decimal('3.0'))
print(Decimal('3.1415926535'))
print(Decimal('3.1415926535') + Decimal('2.7182818285'))
getcontext().rounding = ROUND_UP
print(Decimal('3.1415926535') + Decimal('2.7182818285'))
