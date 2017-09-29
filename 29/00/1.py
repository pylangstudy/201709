from decimal import *
getcontext()
Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
        capitals=1, clamp=0, flags=[], traps=[Overflow, DivisionByZero,
        InvalidOperation])
getcontext().prec = 7       # Set a new precision

getcontext().prec = 28
print(Decimal(10))
print(Decimal('10'))
print(Decimal('3.14'))
print(Decimal('3.14'))
print(Decimal(3.14))

print(Decimal((0, (3, 1, 4), -2)))
print(Decimal(str(2.0 ** 0.5)))
print(Decimal(2) ** Decimal('0.5'))
print(Decimal('NaN'))
print(Decimal('-Infinity'))
