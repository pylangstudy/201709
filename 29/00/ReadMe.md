# [9.4. decimal — 十進固定及び浮動小数点数の算術演算](https://docs.python.jp/3/library/decimal.html#module-decimal)

< [9. 数値と数学モジュール](https://docs.python.jp/3/library/numeric.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/decimal.py](https://github.com/python/cpython/tree/3.6/Lib/decimal.py)

> decimal モジュールは正確に丸められた十進浮動小数点算術をサポートします。 decimal には、 float データ型に比べて、以下のような利点があります:

>     「(Decimal は) 人々を念頭にデザインされた浮動小数点モデルを元にしており、必然的に最も重要な指針があります – コンピュータは人々が学校で習った算術と同じように動作する算術を提供しなければならない」 – 十進数演算仕様より。

>     十進数を正確に表現できます。 1.1 や 2.2 のような数は、二進数の浮動小数点型では正しく表現できません。エンドユーザは普通、 二進数における 1.1 + 2.2 の近似値が 3.3000000000000003 だからといって、そのように表示してほしいとは考えないものです。

>     値の正確さは算術にも及びます。十進の浮動小数点による計算では、 0.1 + 0.1 + 0.1 - 0.3 は厳密にゼロに等しくなります。 二進浮動小数点では 5.5511151231257827e-017 になってしまいます。ゼロに近い値とはいえ、この誤差は数値間の等価性テストの信頼性を阻害します。また、誤差が蓄積されることもあります。こうした理由から、数値間の等価性を厳しく保たなければならないようなアプリケーションを考えるなら、十進数による数値表現が望ましいということになります。

>     decimal モジュールでは、有効桁数の表記が取り入れられており、例えば 1.30 + 1.20 は 2.50 になります。すなわち、末尾のゼロは有効数字を示すために残されます。こうした仕様は通貨計算を行うアプリケーションでは慣例です。乗算の場合、「教科書的な」アプローチでは、乗算の被演算子すべての桁数を使います。例えば、 1.3 * 1.2 は 1.56 になり、 1.30 * 1.20 は 1.5600 になります。

>     ハードウェアによる 2 進浮動小数点表現と違い、decimal モジュールでは計算精度をユーザが変更できます(デフォルトでは 28 桁です)。この桁数はほとんどの問題解決に十分な大きさです:

```python
from decimal import *
getcontext().prec = 6
print(Decimal(1) / Decimal(7))
getcontext().prec = 28
print(Decimal(1) / Decimal(7))
```
```sh
$ python 0.py 
0.142857
0.1428571428571428571428571429
```

>     二進と十進の浮動小数点は、いずれも広く公開されている標準仕様のもとに実装されています。組み込みの浮動小数点型では、標準仕様で提唱されている機能のほんのささやかな部分を利用できるにすぎませんが、decimal では標準仕様が要求している全ての機能を利用できます。必要に応じて、プログラマは値の丸めやシグナル処理を完全に制御できます。この中には全ての不正確な操作を例外でブロックして正確な算術を遵守させるオプションもあります。

>     decimal モジュールは「偏見なく、正確な丸めなしの十進算術(固定小数点算術と呼ばれることもある)と丸めありの浮動小数点数算術」(十進数演算仕様より引用)をサポートするようにデザインされました。

> このモジュールは、十進数型、算術コンテキスト (context for arithmetic)、そしてシグナル (signal) という三つの概念を中心に設計されています。

> 十進数型は変更不能です。これは符号、係数部、そして指数を持ちます。有効桁数を残すために、仮数部の末尾にあるゼロは切り詰められません。 decimal では、 Infinity, -Infinity, および NaN といった特殊な値も定義されています。標準仕様では -0 と +0 も区別します。

> 算術コンテキストとは、精度や値丸めの規則、指数部の制限を決めている環境です。この環境では、演算結果を表すためのフラグや、演算上発生した特定のシグナルを例外として扱うかどうかを決めるトラップイネーブラも定義しています。丸め規則には ROUND_CEILING, ROUND_DOWN, ROUND_FLOOR, ROUND_HALF_DOWN, ROUND_HALF_EVEN, ROUND_HALF_UP, ROUND_UP, および ROUND_05UP があります。

> シグナルとは、演算の過程で生じる例外的条件です。個々のシグナルは、アプリケーションそれぞれの要求に従って、無視されたり、単なる情報とみなされたり、例外として扱われたりします。 decimal モジュールには、 Clamped, InvalidOperation, DivisionByZero, Inexact, Rounded, Subnormal, Overflow, Underflow, および FloatOperation といったシグナルがあります。

> 各シグナルには、フラグとトラップイネーブラがあります。演算上何らかのシグナルに遭遇すると、フラグは 1 にセットされます。このとき、もしトラップイネーブラが 1 にセットされていれば、例外を送出します。フラグの値は膠着型 (sticky) なので、演算によるフラグの変化をモニタしたければ、予めフラグをリセットしておかなければなりません。

> 参考

>     IBM による汎用十進演算仕様、The General Decimal Arithmetic Specification。


## [9.4.1. クイックスタートチュートリアル](https://docs.python.jp/3/library/decimal.html#quick-start-tutorial)

メソッド|説明
--------|----

```python
from decimal import *
getcontext()
Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
        capitals=1, clamp=0, flags=[], traps=[Overflow, DivisionByZero,
        InvalidOperation])
getcontext().prec = 7       # Set a new precision

getcontext().prec = 28
print(Decimal(10))
print(Decimal('10'))
print(Decimal('3.14'))
print(Decimal('3.14'))
print(Decimal(3.14))

print(Decimal((0, (3, 1, 4), -2)))
print(Decimal(str(2.0 ** 0.5)))
print(Decimal(2) ** Decimal('0.5'))
print(Decimal('NaN'))
print(Decimal('-Infinity'))
```
```sh
$ python 1.py 
10
10
3.14
3.14
3.140000000000000124344978758017532527446746826171875
3.14
1.4142135623730951
1.414213562373095048801688724
NaN
-Infinity
```

他、ソースコード参照。

> ほとんどのプログラムでは、開始時に一度だけ現在の演算コンテキストを修正します。また、多くのアプリケーションでは、データから Decimal への変換はループ内で一度だけキャストして行います。コンテキストを設定し、 Decimal オブジェクトを生成できたら、ほとんどのプログラムは他の Python 数値型と全く変わらないかのように Decimal を操作できます。

