import cmath
import math
j = complex(-1.0, 0.0)
print('cmath.phase')
print(cmath.phase(j))
print('math.atan2')
print(math.atan2(j.imag, j.real))
