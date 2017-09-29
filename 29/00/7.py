from decimal import *
print(Decimal('7.325').quantize(Decimal('.01'), rounding=ROUND_DOWN))
print(Decimal('7.325').quantize(Decimal('1.'), rounding=ROUND_UP))
