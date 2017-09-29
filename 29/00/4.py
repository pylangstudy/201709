from decimal import *
getcontext().prec = 6
print(Decimal("1e9999999999999999999"))#decimal.InvalidOperation: [<class 'decimal.InvalidOperation'>]
