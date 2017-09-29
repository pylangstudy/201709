from decimal import *
setcontext(ExtendedContext)
getcontext().clear_flags()
print(Decimal(355) / Decimal(113))
getcontext()
Context(prec=9, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
        capitals=1, clamp=0, flags=[Inexact, Rounded], traps=[])

