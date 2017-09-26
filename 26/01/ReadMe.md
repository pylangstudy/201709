# [9.2. math — 数学関数](https://docs.python.jp/3/library/math.html#module-math)

> このモジュールはいつでも利用できます。標準 C で定義されている数学関数にアクセスすることができます。

> これらの関数で複素数を使うことはできません。複素数に対応する必要があるならば、 cmath モジュールにある同じ名前の関数を使ってください。ほとんどのユーザーは複素数を理解するのに必要なだけの数学を勉強したくないので、複素数に対応した関数と対応していない関数の区別がされています。これらの関数では複素数が利用できないため、引数に複素数を渡されると、複素数の結果が返るのではなく例外が発生します。その結果、どういった理由で例外が送出されたかに早い段階で気づく事ができます。

ゆとり仕様で助かります。

> このモジュールでは次の関数を提供しています。明示的な注記のない限り、戻り値は全て浮動小数点数になります。

## [9.2.1. 数論および数表現の関数](https://docs.python.jp/3/library/math.html#number-theoretic-and-representation-functions)

メソッド|説明
--------|----
math.ceil(x)|x の「天井」 (x 以上の最小の整数) を返します。 x が浮動小数点数でなければ、内部的に x.__ceil__() が実行され、 Integral 値が返されます。
math.copysign(x, y)|x の大きさ (絶対値) で y と同じ符号の浮動小数点数を返します。符号付きのゼロをサポートしているプラットフォームでは、copysign(1.0, -0.0) は -1.0 を返します。
math.fabs(x)|x の絶対値を返します。
math.factorial(x)|x の階乗を返します。 x が整数値でなかったり負であったりするときは、 ValueError を送出します。
math.floor(x)|x の「床」 (x 以下の最大の整数) を返します。 x が浮動小数点数でなければ、内部的に x.__floor__() が実行され、 Integral 値が返されます。
math.frexp(x)|x の仮数と指数を (m, e) のペアとして返します。m はfloat型で、e は厳密に x == m * 2**e であるような整数型です。x がゼロの場合は、(0.0, 0) を返し、それ以外の場合は、0.5 <= abs(m) < 1 を返します。これは浮動小数点型の内部表現を可搬性を保ったまま “分解 (pick apart)” するためです。
math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)|値 a と b が互いに近い場合 True を、そうでない場合は False を返します。
math.isinf(x)|x が正ないし負の無限数ならば True を返します。それ以外の時には False を返します。
math.isnan(x)|x がNaN (not a number、非数) の時に True を返します。それ以外の場合には False を返します。
math.ldexp(x, i)|x * (2**i) を返します。これは本質的に frexp() の逆関数です。
math.modf(x)|x の小数部分と整数部分を返します。両方の結果は x の符号を受け継ぎます。整数部はfloat型で返されます。
math.trunc(x)|x の Integral 値 (たいてい整数) へ切り捨てられた Real 値を返します。 x.__trunc__() に処理を委譲します。

```python
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
```
```sh
$ python 0.py 
math.ceil
99
100
100
100
101
math.copysign
100.0
-100.0
-100.0
100.0
math.fabs
1.23
math.factorial
120
math.floor
99
99
99
100
100
100
math.fmod
2.0
2
math.frexp
(0.9765625, 10)
math.fsum
3.3000000000000003
math.gcd
7
math.isclose
True
False
False
True
math.isfinite
True
False
False
math.isinf
False
True
False
math.isnan
False
False
True
math.ldexp
1024.0
math.modf
(0.19999999999999996, 1.0)
math.trunc
1
```

## [9.2.2. 指数関数と対数関数](https://docs.python.jp/3/library/math.html#power-and-logarithmic-functions)

メソッド|説明
--------|----
math.exp(x)|e**x を返します。
math.expm1(x)|e**x - 1 を返します。小さな浮動小数点数 x について exp(x) - 1 を計算すると、引き算により 桁落ち する可能性がありますが、この expm1() 関数は、完全な精度でこの値を計算します:
math.log(x[, base])|引数が1つの場合、x の (e を底とする)自然対数を返します。
math.log1p(x)|1+x の自然対数(つまり底 e の対数)を返します。結果はゼロに近い x に対して正確になるような方法で計算されます。
math.log2(x)|2を底とする x の対数を返します。この関数は、一般に log(x, 2) よりも正確な値を返します。
math.log10(x)|x の10を底とした対数(常用対数)を返します。この関数は通常、log(x, 10) よりも高精度です。
math.pow(x, y)|x の y 乗を返します。例外的な場合については、 C99 標準の付録 ‘F’ に可能な限り従います。特に、 pow(1.0, x) と pow(x, 0.0) は、たとえ x が零や NaN でも、常に 1.0 を返します。もし x と y の両方が有限の値で、 x が負、 y が整数でない場合、 pow(x, y) は未定義で、 ValueError を送出します。
math.sqrt(x)|x の平方根を返します。

```python
import math
print(math.exp(10))
print(math.expm1(100))
print(math.log(256,2))#対数
print(math.log(1024,2))
print(math.log2(256))#対数
print(math.log2(1024))
print(math.log10(10))#対数
print(math.log10(1000))
print(math.log1p(10))#対数
print(math.log1p(100))
print(math.pow(2,10))
print(math.sqrt(2**2))
print(math.sqrt(3**2))
print(math.sqrt(4**2))
print(math.sqrt(5**2))
print(math.sqrt(2))
print(math.sqrt(3))
```
```sh
$ python 1.py 
22026.465794806718
2.6881171418161356e+43
8.0
10.0
8.0
10.0
1.0
3.0
2.3978952727983707
4.61512051684126
1024.0
2.0
3.0
4.0
5.0
1.4142135623730951
1.7320508075688772
```

## [9.2.3. 三角関数](https://docs.python.jp/3/library/math.html#trigonometric-functions)

メソッド|説明
--------|----
math.acos(x)|x の逆余弦を、ラジアンで返します。
math.asin(x)|x の逆正弦を、ラジアンで返します。
math.atan(x)|x の逆正接を、ラジアンで返します。
math.atan2(y, x)|atan(y / x) を、ラジアンで返します。戻り値は -pi から pi の間になります。この角度は、極座標平面において原点から (x, y) へのベクトルが X 軸の正の方向となす角です。 atan2() のポイントは、両方の入力の符号が既知であるために、位相角の正しい象限を計算できることにあります。例えば、 atan(1) と atan2(1, 1) はいずれも pi/4 ですが、 atan2(-1, -1) は -3*pi/4 になります。
math.cos(x)|x ラジアンの余弦を返します。
math.hypot(x, y)|ユークリッドノルム(sqrt(x*x + y*y))を返します。これは原点から点 (x, y) のベクトルの長さです。
math.sin(x)|x ラジアンの正弦を返します。
math.tan(x)|x ラジアンの正接を返します。

## []()
## []()
## []()
## []()
## []()
## []()
## []()
## []()
## []()
## []()
## []()



## [9.1.1. 数値塔](https://docs.python.jp/3/library/numbers.html#the-numeric-tower)

### class numbers.Complex

属性|説明
----|----
class numbers.Complex|この型のサブクラスは複素数を表し、組み込みの complex 型を受け付ける演算を含みます。それらは: complex および bool への変換、 real, imag, +, -, *, /, abs(), conjugate(), ==, != です。 - と != 以外の全てのものは抽象メソッドや抽象プロパティです。
real|抽象プロパティ。この数の実部を取り出します。
imag|抽象プロパティ。この数の虚部を取り出します。

### class numbers.Rational

属性|説明
----|----
class numbers.Rational|Real をサブタイプ化し numerator と denominator のプロパティを加えたものです。これらは既約分数のものでなければなりません。この他に float() のデフォルトも提供します。
numerator|抽象プロパティ。
denominator|抽象プロパティ。

### ほか

属性|説明
----|----
abstractmethod conjugate()|抽象プロパティ。複素共役を返します。たとえば、(1+3j).conjugate() == (1-3j) です。
class numbers.Real|Real は、Complex 上に、 実数に対して行える演算を加えます。簡潔に言うとそれらは: float への変換, math.trunc(), round(), math.floor(), math.ceil(), divmod(), //, %, <, <=, > および >= です。Real はまた complex(), real, imag および conjugate() のデフォルトを提供します。
class numbers.Integral|Rational をサブタイプ化し int への変換が加わります。 float(), numerator, denominator のデフォルトを提供します。 ** に対する抽象メソッドと、ビット列演算 <<, >>, &, ^, |, ~ を追加します。

## [9.1.2. 型実装者のための注意事項](https://docs.python.jp/3/library/numbers.html#notes-for-type-implementors)

> 実装する人は等しい数が等しく扱われるように同じハッシュを与えるように気を付けねばなりません。これは二つの異なった実数の拡張があるような場合にはややこしいことになるかもしれません。たとえば、 fractions.Fraction は hash() を以下のように実装しています:

```python
def __hash__(self):
    if self.denominator == 1:
        # Get integers right.
        return hash(self.numerator)
    # Expensive check, but definitely correct.
    if self == float(self):
        return hash(float(self))
    else:
        # Use tuple's hash to avoid a high collision rate on
        # simple fractions.
        return hash((self.numerator, self.denominator))
```

## [9.1.2.1. さらに数のABCを追加する](https://docs.python.jp/3/library/numbers.html#adding-more-numeric-abcs)

> 数に対する ABC が他にも多く存在しうることは、言うまでもありません。それらの ABC を階層に追加する可能性が閉ざされるとしたら、その階層は貧相な階層でしかありません。たとえば、 MyFoo を Complex と Real の間に付け加えるには、次のようにします:

```python
class MyFoo(Complex): ...
MyFoo.register(Real)
```

## [9.1.2.2. 算術演算の実装](https://docs.python.jp/3/library/numbers.html#implementing-the-arithmetic-operations)

> 算術演算を実装する際には、型混合(mixed-mode)演算を行うと、作者が両方の引数の型について知っているような実装を呼び出すか、両方の引数をそれぞれ最も似ている組み込み型に変換してその型で演算を行うか、どちらになるのが望ましい実装です。つまり、 Integral のサブタイプに対しては __add__() と __radd__() を次のように定義するべきです:

```python
class MyIntegral(Integral):

    def __add__(self, other):
        if isinstance(other, MyIntegral):
            return do_my_adding_stuff(self, other)
        elif isinstance(other, OtherTypeIKnowAbout):
            return do_my_other_adding_stuff(self, other)
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, MyIntegral):
            return do_my_adding_stuff(other, self)
        elif isinstance(other, OtherTypeIKnowAbout):
            return do_my_other_adding_stuff(other, self)
        elif isinstance(other, Integral):
            return int(other) + int(self)
        elif isinstance(other, Real):
            return float(other) + float(self)
        elif isinstance(other, Complex):
            return complex(other) + complex(self)
        else:
            return NotImplemented
```

> ここには5つの異なる Complex のサブクラス間の混在型の演算があります。上のコードの中で MyIntegral と OtherTypeIKnowAbout に触れない部分を “ボイラープレート” と呼ぶことにしましょう。 a を Complex のサブタイプである A のインスタンス (a : A <: Complex)、同様に b : B <: Complex として、 a + b を考えます:

>         A が b を受け付ける __add__() を定義している場合、何も問題はありません。

>         A でボイラープレート部分に落ち込み、その結果 __add__() が値を返すならば、 B に良く考えられた __radd__() が定義されている可能性を見逃してしまいますので、ボイラープレートは __add__() から NotImplemented を返すのが良いでしょう。(若しくは、 A はまったく __add__() を実装すべきではなかったかもしれません。)

>         そうすると、 B の __radd__() にチャンスが巡ってきます。ここで a が受け付けられるならば、結果は上々です。

>         ここでボイラープレートに落ち込むならば、もう他に試すべきメソッドはありませんので、デフォルト実装の出番です。

>         もし B <: A ならば、Python は A.__add__ の前に B.__radd__ を試します。これで良い理由は、 A についての知識を持って実装しており、 Complex に委ねる前にこれらのインスタンスを扱えるはずだからです。

> もし A <: Complex かつ B <: Real で他に共有された知識が無いならば、適切な共通の演算は組み込みの complex を使ったものになり、どちらの __radd__() ともそこに着地するでしょうから、 a+b == b+a です。

> ほとんどの演算はどのような型についても非常に良く似ていますので、与えられた演算子について順結合(forward)および逆結合(reverse)のメソッドを生成する支援関数を定義することは役に立ちます。たとえば、 fractions.Fraction では次のようなものを利用しています:

```python
def _operator_fallbacks(monomorphic_operator, fallback_operator):
    def forward(a, b):
        if isinstance(b, (int, Fraction)):
            return monomorphic_operator(a, b)
        elif isinstance(b, float):
            return fallback_operator(float(a), b)
        elif isinstance(b, complex):
            return fallback_operator(complex(a), b)
        else:
            return NotImplemented
    forward.__name__ = '__' + fallback_operator.__name__ + '__'
    forward.__doc__ = monomorphic_operator.__doc__

    def reverse(b, a):
        if isinstance(a, Rational):
            # Includes ints.
            return monomorphic_operator(a, b)
        elif isinstance(a, numbers.Real):
            return fallback_operator(float(a), float(b))
        elif isinstance(a, numbers.Complex):
            return fallback_operator(complex(a), complex(b))
        else:
            return NotImplemented
    reverse.__name__ = '__r' + fallback_operator.__name__ + '__'
    reverse.__doc__ = monomorphic_operator.__doc__

    return forward, reverse

def _add(a, b):
    """a + b"""
    return Fraction(a.numerator * b.denominator +
                    b.numerator * a.denominator,
                    a.denominator * b.denominator)

__add__, __radd__ = _operator_fallbacks(_add, operator.add)

# ...
```


