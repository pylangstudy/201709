# [8.1.2. timedelta オブジェクト](https://docs.python.jp/3/library/datetime.html#timedelta-objects)

< [8.1. datetime — 基本的な日付型および時間型](https://docs.python.jp/3/library/datetime.html#module-datetime) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/datetime.py](https://github.com/python/cpython/tree/3.6/Lib/datetime.py)

## 概要

> timedelta オブジェクトは経過時間、すなわち二つの日付や時刻間の差を表します。

属性|値
----|--
class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)|全ての引数がオプションで、デフォルト値は 0 です。引数は整数、浮動小数点数にすることができ、正でも負でもかまいません。
timedelta.min|最小の値を表す timedelta オブジェクトで、 timedelta(-999999999) です。
timedelta.max|最大の値を表す timedelta オブジェクトで、 timedelta(days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999) です。

### インスタンスの属性 (読込のみ):

属性|値
----|--
days|両端値を含む -999999999 から 999999999 の間
seconds|両端値を含む 0 から 86399 の間
microseconds|両端値を含む 0 から 999999 の間

### サポートされている演算

演算|結果
----|----
t1 = t2 + t3|t2 と t3 の和。演算後、t1-t2 == t3 および t1-t3 == t2 は真になります。(1)
t1 = t2 - t3|t2 と t3 の差。演算後、t1 == t2 - t3 および t2 == t1 + t3 は真になります。(1)
t1 = t2 * i または t1 = i * t2|時間差と整数の積。演算後、t1 // i == t2 は i != 0 であれば真となります。
 |一般的に、t1 * i == t1 * (i-1) + t1 は真となります。(1)
t1 = t2 * f または t1 = f * t2|時間差と浮動小数点の積。結果は最近接偶数への丸めを利用して最も近い timedelta.resolution の倍数に丸められます。
f = t2 / t3|t2 を t3 で除したもの (3)。float オブジェクトを返します。
t1 = t2 / f または t1 = t2 / i|時間差を浮動小数点や整数で除したもの。結果は最近接偶数への丸めを利用して最も近い timedelta.resolution の倍数に丸められます。
t1 = t2 // i または t1 = t2 // t3|floor が計算され、余りは (もしあれば) 捨てられます。後者の場合、整数が返されます。(3)
t1 = t2 % t3|剰余が timedelta オブジェクトとして計算されます。(3)
q, r = divmod(t1, t2)|商と剰余が計算されます: q = t1 // t2 (3) と r = t1 % t2 。q は整数で r は timedelta オブジェクトです。
+t1|同じ値を持つ timedelta オブジェクトを返します。(2)
-t1|timedelta(-t1.days, -t1.seconds, -t1.microseconds)、および t1* -1 と同じです。 (1)(4)
abs(t)|t.days >= 0 のときには +t, t.days < 0 のときには -t となります。(2)
str(t)|[D day[s], ][H]H:MM:SS[.UUUUUU] という形式の文字列を返します。t が負の値の場合は D は負の値となります。(5)
repr(t)|datetime.timedelta(D[, S[, U]]) という形式の文字列を返します。t が負の場合は D は負の値となります。(5)

#### 注釈

> この演算は正確ですが、オーバフローするかもしれません。

> この演算は正確であり、オーバフローしないはずです。

> 0 による除算は ZeroDivisionError を送出します。

> -timedelta.max は timedelta オブジェクトで表現することができません。

> timedelta オブジェクトの文字列表現は内部表現に類似した形に正規化されます。そのため負の timedelta は少し変な結果になります。例えば:

```python
>>> timedelta(hours=-5)
datetime.timedelta(-1, 68400)
>>> print(_)
-1 day, 19:00:00
```

> 上に列挙した操作に加えて、 timedelta オブジェクトは date および datetime オブジェクトとの間で加減算をサポートしています (下を参照してください)。

> バージョン 3.2 で変更: timedelta オブジェクトの別の timedelta オブジェクトによる、切り捨ての割り算と真の値の割り算、および剰余演算子と divmod() 関数がサポートされるようになりました。 timedelta オブジェクトと float オブジェクトの真の値の割り算と掛け算がサポートされるようになりました。

> timedelta オブジェクト間の比較はサポートされており、より小さい経過時間を表す timedelta オブジェクトがより小さい timedelta と見なされます。型混合の比較がデフォルトのオブジェクトアドレス比較となってしまうのを抑止するために、 timedelta オブジェクトと異なる型のオブジェクトが比較されると、比較演算子が == または != でないかぎり TypeError が送出されます。後者の場合、それぞれ False または True を返します。

> timedelta オブジェクトは hashable (ハッシュ可能、つまり、辞書のキーとして利用可能) であり、効率的な pickle 化をサポートします。また、ブール演算コンテキストでは、 timedelta オブジェクトは timedelta(0) に等しくない場合かつそのときに限り真となります。

### インスタンスメソッド

属性|説明
----|----
timedelta.total_seconds()|この期間に含まれるトータルの秒数を返します。td / timedelta(seconds=1) と等価です。バージョン 3.2 で追加.

#### 使用例

```python
>>> from datetime import timedelta
>>> year = timedelta(days=365)
>>> another_year = timedelta(weeks=40, days=84, hours=23,
...                          minutes=50, seconds=600)  # adds up to 365 days
>>> year.total_seconds()
31536000.0
>>> year == another_year
True
>>> ten_years = 10 * year
>>> ten_years, ten_years.days // 365
(datetime.timedelta(3650), 10)
>>> nine_years = ten_years - year
>>> nine_years, nine_years.days // 365
(datetime.timedelta(3285), 9)
>>> three_years = nine_years // 3;
>>> three_years, three_years.days // 365
(datetime.timedelta(1095), 3)
>>> abs(three_years - ten_years) == 2 * three_years + year
True
```

```python
from datetime import timedelta
year = timedelta(days=365)
another_year = timedelta(weeks=40, days=84, hours=23,
                             minutes=50, seconds=600)  # adds up to 365 days
print(year.total_seconds())
print(year == another_year)
ten_years = 10 * year
print(ten_years, ten_years.days // 365)
nine_years = ten_years - year
print(nine_years, nine_years.days // 365)
three_years = nine_years // 3;
print(three_years, three_years.days // 365)
print(abs(three_years - ten_years) == 2 * three_years + year)
```
```sh
$ python 0.py 
31536000.0
True
3650 days, 0:00:00 10
3285 days, 0:00:00 9
1095 days, 0:00:00 3
True
min
```

