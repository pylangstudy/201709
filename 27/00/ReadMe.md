# [9.2. math — 数学関数](https://docs.python.jp/3/library/math.html#module-math) < [9. 数値と数学モジュール](https://docs.python.jp/3/library/numeric.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## [9.2.4. 角度変換](https://docs.python.jp/3/library/math.html#angular-conversion)

メソッド|説明
--------|----
math.degrees(x)|角 x をラジアンから度に変換します。
math.radians(x)|角 x を度からラジアンに変換します。

```python
import math
print('math.radians')
print(math.radians(180))
print('math.degrees')
print(math.degrees(math.radians(180)))
```
```sh
$ python 0.py 
math.radians
3.141592653589793
math.degrees
180.0
```

## [9.2.5. 双曲線関数](https://docs.python.jp/3/library/math.html#hyperbolic-functions)

> 双曲線関数 は円ではなく双曲線を元にした三角関数のようなものです。

* [双曲線関数](https://ja.wikipedia.org/wiki/%E5%8F%8C%E6%9B%B2%E7%B7%9A%E9%96%A2%E6%95%B0)

メソッド|説明
--------|----
math.acosh(x)|x の逆双曲線余弦を返します。
math.asinh(x)|x の逆双曲線正弦を返します。
math.atanh(x)|x の逆双曲線正接を返します。
math.cosh(x)|x の双曲線余弦を返します。
math.sinh(x)|x の双曲線正弦を返します。
math.tanh(x)|x の双曲線正接を返します。

まったく理解できないので割愛。

## [9.2.6. 特殊関数](https://docs.python.jp/3/library/math.html#special-functions)

メソッド|説明
--------|----
math.erf(x)|x の 誤差関数 を返します。
math.erfc(x)|x の相補誤差関数を返します。相補誤差関数 は 1.0 - erf(x) と定義されます。この関数は、1との引き算では 桁落ち をするような大きな x に対し使われます。
math.gamma(x)|x の ガンマ関数 を返します。
math.lgamma(x)|x のガンマ関数の絶対値の自然対数を返します。

まったく理解できないので割愛。


## [9.2.7. 定数](https://docs.python.jp/3/library/math.html#constants)

メソッド|説明
--------|----
math.pi|利用可能な精度の、数学定数π = 3.141592... (円周率)。
math.e|利用可能な精度の、数学定数 e = 2.718281... (自然対数の底)。
math.tau|数学定数 τ = 6.283185... (利用可能な精度まで) です。タウは2πに等しい円定数で、円周と半径の比です。タウについて学ぶには Vi Hart のビデオ [Pi is (still) Wrong](https://www.youtube.com/watch?v=jG7vhMMXagQ) をチェックして、パイを二倍食べて [Tau day](https://tauday.com/) を祝い始めましょう！
math.inf|浮動小数の正の無限大です。(負の無限大には -math.inf を使います。) float('inf') の出力と等価です。
math.nan|浮動小数の非数 “not a number” (NaN) です。float('nan') の出力と等価です。

上記の通り単なる定数なので割愛。唐突に入るユーモアが浮いている。数学信者のジョークなのか？

> CPython 実装の詳細: math モジュールは、ほとんどが実行プラットフォームにおける C 言語の数学ライブラリ関数に対する薄いラッパでできています。 例外時の挙動は、適切である限り C99 標準の Annex F に従います。 現在の実装では、sqrt(-1.0) や log(0.0) といった (C99 Annex F で不正な演算やゼロ除算を通知することが推奨されている) 不正な操作に対して ValueError を送出し、(例えば exp(1000.0) のような) 演算結果がオーバーフローする場合には OverflowError を送出します。 上記の関数群は、1つ以上の引数が NaN であった場合を除いて NaN を返しません。 引数に NaN が与えられた場合は、殆どの関数は NaN を返しますが、 (C99 Annex F に従って) 別の動作をする場合があります。 例えば、 pow(float('nan'), 0.0) や hypot(float('nan'), float('inf')) といった場合です。 訳注: 例外が発生せずに結果が返ると、計算結果がおかしくなった原因が複素数を渡したためだということに気づくのが遅れる可能性があります。

> Python は signaling NaN と quiet NaN を区別せず、signaling NaN に対する挙動は未定義とされていることに注意してください。典型的な挙動は、全ての NaN を quiet NaN として扱うことです。

> 参考

> cmath モジュール

>    これらの多くの関数の複素数版。
