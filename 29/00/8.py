from decimal import *
myothercontext = Context(prec=60, rounding=ROUND_HALF_DOWN)
setcontext(myothercontext)
print(Decimal(1) / Decimal(7))

ExtendedContext
setcontext(ExtendedContext)
print(Decimal(1) / Decimal(7))
print(Decimal(42) / Decimal(0))

setcontext(BasicContext)
print(Decimal(42) / Decimal(0))
