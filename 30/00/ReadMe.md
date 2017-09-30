# [9.4. decimal — 十進固定及び浮動小数点数の算術演算](https://docs.python.jp/3/library/decimal.html#module-decimal)

< [9. 数値と数学モジュール](https://docs.python.jp/3/library/numeric.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/decimal.py](https://github.com/python/cpython/tree/3.6/Lib/decimal.py)

## [9.4.2. Decimal オブジェクト](https://docs.python.jp/3/library/decimal.html#decimal-objects)

属性|説明
----|----
class decimal.Decimal(value="0", context=None)|value に基づいて新たな Decimal オブジェクトを構築します。
adjusted()|仮数の先頭の一桁だけが残るように右側の数字を追い出す桁シフトを行い、その結果の指数部を返します: Decimal('321e+5').adjusted() は 7 を返します。最上桁の小数点からの相対位置を調べる際に使います。
as_integer_ratio()|与えられた Decimal インスタンスを、既約分数で分母が正数の分数として表現した整数のペア (n, d) を返します。
as_tuple()|数値を表現するための名前付きタプル(named tuple): DecimalTuple(sign, digittuple, exponent) を返します。
canonical()|引数の標準的(canonical)エンコーディングを返します。現在のところ、 Decimal インスタンスのエンコーディングは常に標準的なので、この操作は引数に手を加えずに返します。
compare(other, context=None)|二つの Decimal インスタンスの値を比較します。 compare() は Decimal インスタンスを返し、被演算子のどちらかが NaN ならば結果は NaN です:
compare_signal(other, context=None)|この演算は compare() とほとんど同じですが、全ての NaN がシグナルを送るところが異なります。すなわち、どちらの比較対象も発信 (signaling) NaN でないならば無言 (quiet) NaN である比較対象があたかも発信 NaN であるかのように扱われます。
compare_total(other, context=None)|二つの対象を数値によらず抽象表現によって比較します。 compare() に似ていますが、結果は Decimal に全順序を与えます。この順序づけによると、数値的に等しくても異なった表現を持つ二つの Decimal インスタンスの比較は等しくなりません:
compare_total_mag(other, context=None)|二つの対象を compare_total() のように数値によらず抽象表現によって比較しますが、両者の符号を無視します。 x.compare_total_mag(y) は x.copy_abs().compare_total(y.copy_abs()) と等価です。
conjugate()|self を返すだけです。このメソッドは十進演算仕様に適合するためだけのものです。
copy_abs()|引数の絶対値を返します。この演算はコンテキストに影響されず、静かです。すなわち、フラグは変更されず、丸めは行われません。
copy_negate()|引数の符号を変えて返します。この演算はコンテキストに影響されず、静かです。すなわち、フラグは変更されず、丸めは行われません。
copy_sign(other, context=None)|最初の演算対象のコピーに二つめと同じ符号を付けて返します。たとえば:
exp(context=None)|与えられた数での(自然)指数関数 e**x の値を返します。結果は ROUND_HALF_EVEN 丸めモードで正しく丸められます。
from_float(f)|浮動小数点数を正確に小数に変換するクラスメソッドです。
fma(other, third, context=None)|融合積和(fused multiply-add)です。self*other+third を途中結果の積 self*other で丸めを行わずに計算して返します。
is_canonical()|引数が標準的(canonical)ならば True を返し、そうでなければ False を返します。現在のところ、 Decimal のインスタンスは常に標準的なのでこのメソッドの結果はいつでも True です。
is_finite()|引数が有限の数値ならば True を、無限大か NaN ならば False を返します。
is_infinite()|引数が正または負の無限大ならば True を、そうでなければ False を返します。
is_nan()|引数が (無言か発信かは問わず) NaN であれば True を、そうでなければ False を返します。
is_normal(context=None)|引数が 正規(normal) の有限数値ならば True を返します。引数がゼロ、非正規(subnormal)、無限大または NaN であれば False を返します。
is_qnan()|引数が無言 NaN であれば True を、そうでなければ False を返します。
is_signed()|引数に負の符号がついていれば True を、そうでなければ False を返します。注意すべきはゼロや NaN なども符号を持ち得ることです。
is_snan()|引数が発信 NaN であれば True を、そうでなければ False を返します。
is_subnormal(context=None)|引数が非正規数(subnormal)であれば True を、そうでなければ False を返します。
is_zero()|引数が(正または負の)ゼロであれば True を、そうでなければ False を返します。
ln(context=None)|演算対象の自然対数(底 e の対数)を返します。結果は ROUND_HALF_EVEN 丸めモードで正しく丸められます。
log10(context=None)|演算対象の底 10 の対数を返します。結果は ROUND_HALF_EVEN 丸めモードで正しく丸められます。
logb(context=None)|非零の数値については、 Decimal インスタンスとして調整された指数を返します。演算対象がゼロだった場合、 Decimal('-Infinity') が返され DivisionByZero フラグが送出されます。演算対象が無限大だった場合、 Decimal('Infinity') が返されます。
logical_and(other, context=None)|logical_and() は二つの 論理引数 (論理引数 参照)を取る論理演算です。結果は二つの引数の数字ごとの and です。
logical_invert(context=None)|logical_invert() は論理演算です。結果は引数の数字ごとの反転です。
logical_or(other, context=None)|logical_or() は二つの 論理引数 (論理引数 参照)を取る論理演算です。結果は二つの引数の数字ごとの or です。
logical_xor(other, context=None)|logical_xor() は二つの 論理引数 (論理引数 参照)を取る論理演算です。結果は二つの引数の数字ごとの排他的論理和です。
max(other, context=None)|max(self, other) と同じですが、値を返す前に現在のコンテキストに即した丸め規則を適用します。また、 NaN に対して、(コンテキストの設定と、発信か無言どちらのタイプであるかに応じて) シグナルを発行するか無視します。
max_mag(other, context=None)|max() メソッドに似ていますが、比較は絶対値で行われます。
min(other, context=None)|min(self, other) と同じですが、値を返す前に現在のコンテキストに即した丸め規則を適用します。また、 NaN に対して、(コンテキストの設定と、発信か無言どちらのタイプであるかに応じて) シグナルを発行するか無視します。
min_mag(other, context=None)|min() メソッドに似ていますが、比較は絶対値で行われます。
next_minus(context=None)|与えられたコンテキスト(またはコンテキストが渡されなければ現スレッドのコンテキスト)において表現可能な、操作対象より小さい最大の数を返します。
next_plus(context=None)|与えられたコンテキスト(またはコンテキストが渡されなければ現スレッドのコンテキスト)において表現可能な、操作対象より大きい最小の数を返します。
next_toward(other, context=None)|二つの比較対象が等しくなければ、一つめの対象に最も近く二つめの対象へ近付く方向の数を返します。もし両者が数値的に等しければ、二つめの対象の符号を採った一つめの対象のコピーを返します。
normalize(context=None)|数値を正規化 (normalize) して、右端に連続しているゼロを除去し、 Decimal('0') と同じ結果はすべて Decimal('0e0') に変換します。等価クラスの属性から基準表現を生成する際に用います。たとえば、 Decimal('32.100') と Decimal('0.321000e+2') の正規化は、いずれも同じ値 Decimal('32.1') になります。
number_class(context=None)|操作対象の クラス を表す文字列を返します。
quantize(exp, rounding=None, context=None)|二つ目の操作対象と同じ指数を持つように丸めを行った、一つめの操作対象と等しい値を返します。
radix()|Decimal(10) つまり Decimal クラスがその全ての算術を実行する基数を返します。仕様との互換性のために取り入れられています。
remainder_near(other, context=None)|self を other で割った剰余を返します。これは self % other とは違って、剰余の絶対値を小さくするように符号が選ばれます。より詳しく言うと、n を self / other の正確な値に最も近い整数としたときの self - n * other が返り値になります。最も近い整数が2つある場合には偶数のものが選ばれます。
rotate(other, context=None)|一つ目の演算対象の数字を二つ目で指定された量だけ巡回(rotate)した結果を返します。二つめの演算対象は -precision から precision までの範囲の整数でなければなりません。この二つ目の演算対象の絶対値を何桁ずらすかを決めます。そしてもし正の数ならば巡回の方向は左に、そうでなければ右になります。一つ目の演算対象の仮数部は必要ならば精度いっぱいまでゼロで埋められます。符号と指数は変えられません。
same_quantum(other, context=None)|self と other が同じ指数を持っているか、あるいは双方とも NaN である場合に真を返します。
scaleb(other, context=None)|二つ目の演算対象で調整された指数の一つ目の演算対象を返します。同じことですが、一つめの演算対象を 10**other 倍したものを返します。二つ目の演算対象は整数でなければなりません。
shift(other, context=None)|一つ目の演算対象の数字を二つ目で指定された量だけシフトした結果を返します。二つ目の演算対象は -precision から precision までの範囲の整数でなければなりません。この二つ目の演算対象の絶対値が何桁ずらすかを決めます。そしてもし正の数ならばシフトの方向は左に、そうでなければ右になります。一つ目の演算対象の係数は必要ならば精度いっぱいまでゼロで埋められます。符号と指数は変えられません。
sqrt(context=None)|引数の平方根を最大精度で求めます。
to_eng_string(context=None)|文字列に変換します。指数が必要なら工学表記が使われます。
to_integral(rounding=None, context=None)|to_integral_value() メソッドと同じです。to_integral の名前は古いバージョンとの互換性のために残されています。
to_integral_exact(rounding=None, context=None)|最近傍の整数に値を丸め、丸めが起こった場合には Inexact または Rounded のシグナルを適切に出します。丸めモードは以下のように決められます。 rounding 引数が与えられていればそれが使われます。そうでなければ context 引数で決まります。どちらの引数も渡されなければ現在のスレッドのコンテキストの丸めモードが使われます。
to_integral_value(rounding=None, context=None)|Inexact や Rounded といったシグナルを出さずに最近傍の整数に値を丸めます。 rounding が指定されていれば適用されます; それ以外の場合、値丸めの方法は context の設定か現在のコンテキストの設定になります。

```python
from decimal import *
print((-7) % 4)
print(Decimal(-7) % Decimal(4))
print(-7 // 4)
print(Decimal(-7) // Decimal(4))
```
```sh
$ python 0.py 
1
-3
-2
-1
```

```python
from decimal import *
print(Decimal('321e+5').adjusted())
print(Decimal('-3.14').as_integer_ratio())
print(Decimal('-3.14').as_tuple())
print(Decimal('-3.14').canonical())
print(Decimal('-3.14').compare(Decimal('-3.14')))
print(Decimal('-3.14').compare(Decimal('3.14')))
print(Decimal('-3.14').compare(Decimal('-333.14')))
print(Decimal('-3.14').compare_signal(Decimal('-333.14')))
print(Decimal('12.0').compare_total(Decimal('12')))
print(Decimal('12.0').compare_total_mag(Decimal('12')))
print(Decimal('12.0').conjugate())
print(Decimal('12.0').copy_abs())
print(Decimal('12.0').copy_negate())
print(Decimal('2.3').copy_sign(Decimal('-1.5')))
print(Decimal('1').exp())
print(Decimal.from_float(0.1))
print(Decimal(2).fma(3, 5))
print(Decimal('1').is_canonical())
print(Decimal('1').is_finite())
print(Decimal('1').is_infinite())
print(Decimal('1').is_nan())
print(Decimal('1').is_normal())
print(Decimal('1').is_qnan())
print(Decimal('1').is_signed())
print(Decimal('1').is_snan())
print(Decimal('1').is_subnormal())
print(Decimal('1').is_zero())
print(Decimal('1').ln())
print(Decimal('1').log10())
print(Decimal('1').logb())
print(Decimal('1').logical_and(Decimal('1')))
print(Decimal('1').logical_invert())
print(Decimal('1').logical_or(Decimal('1')))
print(Decimal('1').logical_xor(Decimal('1')))
print(Decimal('1').max(Decimal('-2')))
print(Decimal('1').max_mag(Decimal('-2')))
print(Decimal('1').min(Decimal('-2')))
print(Decimal('1').min_mag(Decimal('-2')))
print(Decimal('1').next_minus())
print(Decimal('1').next_plus())
print(Decimal('1').next_toward(Decimal('1')))
print(Decimal('1').normalize())
print(Decimal('1').number_class())
print(Decimal('1.41421356').quantize(Decimal('1.000')))
print(Decimal('1').remainder_near(Decimal('1')))
print(Decimal('1').radix())
print(Decimal('1').rotate(Decimal('1')))
print(Decimal('1').same_quantum(Decimal('1')))
print(Decimal('1').scaleb(Decimal('1')))
print(Decimal('1').shift(Decimal('1')))
print(Decimal('1').sqrt())
print(Decimal('1').to_eng_string())
print(Decimal('1').to_integral())
print(Decimal('1').to_integral_exact())
print(Decimal('1').to_integral_value())
```
```sh
$ python 1.py 
7
(-157, 50)
DecimalTuple(sign=1, digits=(3, 1, 4), exponent=-2)
-3.14
0
-1
1
1
-1
-1
12.0
12.0
-12.0
-2.3
2.718281828459045235360287471
0.1000000000000000055511151231257827021181583404541015625
11
True
True
False
False
True
False
False
False
False
False
0
0
0
1
1111111111111111111111111110
1
0
1
-2
-2
1
0.9999999999999999999999999999
1.000000000000000000000000001
1
1
+Normal
1.414
0
10
10
True
1E+1
10
1
1
1
1
1
```

