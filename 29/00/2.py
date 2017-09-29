from decimal import *

c = getcontext()
c.traps[FloatOperation] = True
#print(Decimal(3.14))#decimal.FloatOperation: [<class 'decimal.FloatOperation'>]
#print(Decimal('3.5') < 3.7)#decimal.FloatOperation: [<class 'decimal.FloatOperation'>]
print(Decimal('3.5') == 3.5)
