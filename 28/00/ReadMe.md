# [9.3. cmath — 複素数のための数学関数](https://docs.python.jp/3/library/cmath.html#module-cmath)

< [9. 数値と数学モジュール](https://docs.python.jp/3/library/numeric.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

> このモジュールは常に利用可能です。提供しているのは複素数を扱う数学関数へのアクセスです。このモジュール中の関数は整数、浮動小数点数または複素数を引数にとります。また、 __complex__() または __float__() どちらかのメソッドを提供している Python オブジェクトも受け付けます。これらのメソッドはそのオブジェクトを複素数または浮動小数点数に変換するのにそれぞれ使われ、呼び出された関数はそうして変換された結果を利用します。

> 注釈

> ハードウェア及びシステムレベルでの符号付きゼロのサポートがあるプラットフォームでは、分枝切断 (branch cut) の関わる関数において切断された 両側 の分枝で連続になります。ゼロの符号でどちらの分枝であるかを区別するのです。符号付きゼロがサポートされないプラットフォームでは連続性は以下の仕様で述べるようになります。 

## [9.3.1. 極座標変換](https://docs.python.jp/3/library/cmath.html#conversions-to-and-from-polar-coordinates)

メソッド|説明
--------|----
cmath.phase(x)|x の位相 (x の 偏角 とも呼びます) を浮動小数点数で返します。phase(x) は math.atan2(x.imag, x.real) と同等です。返り値は [-π, π] の範囲にあり、この演算の分枝切断は負の実軸に沿って延びていて、上から連続です。(現在のほとんどのシステムはそうですが) 符号付きゼロをサポートしているシステムでは、結果の符号は x.imag がゼロであってさえ x.imag の符号と等しくなります:
cmath.polar(x)|x の極座標表現を返します。x の半径 r と x の位相 phi の組 (r, phi) を返します。polar(x) は (abs(x), phase(x)) に等しいです。
cmath.rect(r, phi)|極座標 r, phi を持つ複素数 x を返します。値は r * (math.cos(phi) + math.sin(phi)*1j) に等しいです。

```python
import cmath
import math
j = complex(-1.0, 0.0)
print('cmath.phase')
print(cmath.phase(j))
print('math.atan2')
print(math.atan2(j.imag, j.real))
```
```sh
$ python 0.py 
cmath.phase
3.141592653589793
math.atan2
3.141592653589793
```

## [9.3.2. 指数関数と対数関数](https://docs.python.jp/3/library/cmath.html#power-and-logarithmic-functions)

メソッド|説明
--------|----
cmath.exp(x)|指数 e**x を返します。
cmath.log(x[, base])|base を底とする x の対数を返します。もし base が指定されていない場合には、x の自然対数を返します。分枝切断を一つもち、0 から負の実数軸に沿って -∞ へと延びており、上から連続しています。
cmath.log10(x)|x の底を 10 とする対数を返します。 log() と同じ分枝切断を持ちます。
cmath.sqrt(x)|x の平方根を返します。 log() と同じ分枝切断を持ちます。

## [9.3.3. 三角関数](https://docs.python.jp/3/library/cmath.html#trigonometric-functions)

メソッド|説明
--------|----
cmath.acos(x)|x の逆余弦を返します。この関数には二つの分枝切断 (branch cut) があります: 一つは 1 から右側に実数軸に沿って∞へと延びていて、下から連続しています。もう一つは -1 から左側に実数軸に沿って -∞へと延びていて、上から連続しています。
cmath.asin(x)|x の逆正弦を返します。 acos() と同じ分枝切断を持ちます。
cmath.atan(x)|x の逆正接を返します。二つの分枝切断があります: 一つは 1j から虚数軸に沿って ∞j へと延びており、右から連続です。もう一つは -1j から虚数軸に沿って -∞j へと延びており、左から連続です。
cmath.cos(x)|x の余弦を返します。
cmath.sin(x)|x の正弦を返します。
cmath.tan(x)|x の正接を返します。

## [9.3.4. 双曲線関数](https://docs.python.jp/3/library/cmath.html#hyperbolic-functions)

メソッド|説明
--------|----
cmath.acosh(x)|x の逆双曲線余弦を返します。分枝切断が一つあり、1 の左側に実数軸に沿って -∞へと延びていて、上から連続しています。
cmath.asinh(x)|x の逆双曲線正弦を返します。二つの分枝切断があります: 一つは 1j から虚数軸に沿って ∞j へと延びており、右から連続です。もう一つは -1j から虚数軸に沿って -∞j へと延びており、左から連続です。
cmath.atanh(x)|x の逆双曲線正接を返します。二つの分枝切断があります: 一つは 1 から実数軸に沿って ∞ へと延びており、下から連続です。もう一つは -1 から実数軸に沿って -∞ へと延びており、上から連続です。
cmath.cosh(x)|x の双曲線余弦を返します。
cmath.sinh(x)|x の双曲線正弦を返します。
cmath.tanh(x)|x の双曲線正接を返します。

## [9.3.5. 類別関数](https://docs.python.jp/3/library/cmath.html#classification-functions)

メソッド|説明
--------|----
cmath.isfinite(x)|x の実部、虚部ともに有限であれば True を返し、それ以外の場合 False を返します。
cmath.isinf(x)|x の実数部または虚数部が正または負の無限大であれば True を、そうでなければ False を返します。
cmath.isnan(x)|x の実部と虚部のどちらかが NaN のとき True を返し、それ以外の場合 False を返します。
cmath.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)|値 a と b が互いに近い場合 True を、そうでない場合は False を返します。

> 参考

> PEP 485 – A function for testing approximate equality

* [PEP 485](https://www.python.org/dev/peps/pep-0485)

## [9.3.6. 定数](https://docs.python.jp/3/library/cmath.html#constants)

メソッド|説明
--------|----
cmath.pi|定数 π (円周率)で、浮動小数点数です。
cmath.e|定数 e (自然対数の底)で、浮動小数点数です。
cmath.tau|数学定数 τ で、浮動小数点数です。
cmath.inf|浮動小数点数の正の無限大です。float('inf') と等価です。
cmath.infj|実部がゼロ、虚部が正の無限大の複素数です。complex(0.0, float('inf')) と等価です。
cmath.nan|浮動小数点数の非数 “not a number” (NaN) です。float('nan') と等価です。
cmath.nanj|実部がゼロ、虚部が NaN の複素数です。complex(0.0, float('nan')) と等価です。

> math と同じような関数が選ばれていますが、全く同じではないので注意してください。機能を二つのモジュールに分けているのは、複素数に興味がなかったり、もしかすると複素数とは何かすら知らないようなユーザがいるからです。そういった人たちはむしろ、 math.sqrt(-1) が複素数を返すよりも例外を送出してほしいと考えます。また、 cmath で定義されている関数は、たとえ結果が実数で表現可能な場合 (虚数部がゼロの複素数) でも、常に複素数を返すので注意してください。

私は複素数とは何かすら知らないので、おとなしくmathを使おう。

> 分枝切断 (branch cut) に関する注釈: 分枝切断を持つ曲線上では、与えられた関数は連続ではなくなります。これらは多くの複素関数における必然的な特性です。複素関数を計算する必要がある場合、これらの分枝に関して理解しているものと仮定しています。悟りに至るために何らかの (到底基礎的とはいえない) 複素数に関する書をひもといてください。数値計算を目的とした分枝切断の正しい選択方法についての情報としては、以下がよい参考文献となります:

悟りを開くに至る必要すらあるらしい。

> 参考

> Kahan, W: Branch cuts for complex elementary functions; or, Much ado about nothings’s sign bit. In Iserles, A., and Powell, M. (eds.), The state of the art in numerical analysis. Clarendon Press (1987) pp165–211. 
