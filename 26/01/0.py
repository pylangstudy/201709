import math
#偶数側に丸めていると思われる
print('math.ceil')
print(math.ceil(99.0))
print(math.ceil(99.1))
print(math.ceil(99.9))
print(math.ceil(100.0))
print(math.ceil(100.1))

#不要。-1を掛ければいい
print('math.copysign')
print(math.copysign(100, 1))
print(math.copysign(-100, -1))
print(math.copysign(100, -1))
print(math.copysign(-100, 1))

print('math.fabs')
print(math.fabs(-1.23))
print('math.factorial')
print(math.factorial(5))#5!=5*4*3*2*1=120
print('math.floor')
print(math.floor(99.0))
print(math.floor(99.1))
print(math.floor(99.9))
print(math.floor(100.0))
print(math.floor(100.1))
print(math.floor(100.9))
print('math.fmod')
print(math.fmod(2, 3))#浮動小数点のとき x % y を使うと計算が狂うことがあるので fmod を使うべきらしい
print(2 % 3)

print('math.frexp')
print(math.frexp(1000))
print('math.fsum')
print(math.fsum([1.1, 2.2]))
print('math.gcd')
print(math.gcd(35,49))
print('math.isclose')
print(math.isclose(5,105,abs_tol=100))#差が100以内か否か
print(math.isclose(5,106,abs_tol=100))
print(math.isclose(89,100,rel_tol=0.1))#差が最大値の10%以内か否か
print(math.isclose(90,100,rel_tol=0.1))

print('math.isfinite')
print(math.isfinite(0))#無限でも NaNでもない場合に True
print(math.isfinite(float("inf")))
print(math.isfinite(float("NaN")))
print('math.isinf')
print(math.isinf(0))#無限でも NaNでもない場合に True
print(math.isinf(float("inf")))
print(math.isinf(float("NaN")))
print('math.isnan')
print(math.isnan(0))#無限でも NaNでもない場合に True
print(math.isnan(float("inf")))
print(math.isnan(float("NaN")))
print('math.ldexp')
print(math.ldexp(1,10))#x * (2**i)    frexp() の逆関数
print('math.modf')
print(math.modf(1.2))
print('math.trunc')
print(math.trunc(1.2))


