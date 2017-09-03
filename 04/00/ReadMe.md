# [8.1.3. date オブジェクト](https://docs.python.jp/3/library/datetime.html#date-objects)

< [8.1. datetime — 基本的な日付型および時間型](https://docs.python.jp/3/library/datetime.html#module-datetime) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/datetime.py](https://github.com/python/cpython/tree/3.6/Lib/datetime.py)

## 概要

> date オブジェクトは日付 (年、月、および日) を表します。日付は理想的なカレンダー、すなわち現在のグレゴリオ暦を過去と未来の両方向に無限に延長したもので表されます。 1 年の 1 月 1 日は日番号 1, 1 年 1 月 2 日は日番号 2,となっていきます。この暦法は、全ての計算における基本カレンダーである、 Dershowitz と Reingold の書籍 Calendrical Calculations における先発グレゴリオ暦 (proleptic Gregorian) の定義に一致します。

## 属性一覧

コンストラクタ|説明
--------------|----
class datetime.date(year, month, day)|全ての引数が必要です。

他のコンストラクタ、および全てのを以下に示します:

クラスメソッド|説明
--------------|----
classmethod date.today()|現在のローカルな日付を返します。date.fromtimestamp(time.time()) と等価です。
classmethod date.fromtimestamp(timestamp)|time.time() で返されるような POSIX タイムスタンプに対応するローカルな日付を返します。1970 年から 2038 年までに制限されています。非 POSIX なシステムではうるう秒は無視されます。
classmethod date.fromordinal(ordinal)|先発グレゴリオ暦による序数に対応する日付を返します。 1 年 1 月 1 日が序数 1 となります。

クラス属性|説明
----------|----
date.min|表現できる最も古い日付で、date(MINYEAR, 1, 1) です。
date.max|表現できる最も新しい日付で、date(MAXYEAR, 12, 31) です。
date.resolution|等しくない日付オブジェクト間の最小の差で、timedelta(days=1) です。

インスタンス属性 (読込のみ)|説明
---------------------------|----
date.year|両端値を含む MINYEAR から MAXYEAR までの値です。
date.month|両端値を含む 1 から 12 までの値です。
date.day|1 から与えられた月と年における日数までの値です。

### サポートされている演算

演算|結果
----|----
`date2 = date1 + timedelta`|date2 はから date1 から timedelta.days 日移動した日付です。(1)
`date2 = date1 - timedelta`|date2 + timedelta == date1 であるような日付 date2 を計算します。(2)
`timedelta = date1 - date2`|(3)
`date1 < date2`|date1 が時刻として date2 よりも前を表す場合に、date1 は date2 よりも小さいと見なされます。(4)

#### 注釈:

> (1) date2 は timedelta.days > 0 の場合進む方向に、 timedelta.days < 0 の場合戻る方向に移動します。演算後は、 date2 - date1 == timedelta.days となります。 timedelta.seconds および timedelta.microseconds は無視されます。 date2.year が MINYEAR になってしまったり、 MAXYEAR より大きくなってしまう場合には OverflowError が送出されます。

> (2) この操作は date1 + (-timedelta) と等価ではありません。なぜならば、date1 - timedelta がオーバフローしない場合でも、-timedelta 単体がオーバフローする可能性があるからです。timedelta.seconds および timedelta.microseconds は無視されます。

> (3) この演算は厳密で、オーバフローしません。timedelta.seconds および timedelta.microseconds は 0 で、演算後には date2 + timedelta == date1 となります。

> (4) 別の言い方をすると、 date1.toordinal() < date2.toordinal() であり、かつそのときに限り date1 < date2 となります。型混合の比較がデフォルトのオブジェクトアドレス比較となってしまうのを抑止するために、 date オブジェクトと異なる型のオブジェクトが比較されると TypeError が送出されます。しかしながら、被比較演算子のもう一方が timetuple() 属性を持つ場合には NotImplemented が返されます。このフックにより、他種の日付オブジェクトに型混合比較を実装するチャンスを与えています。そうでない場合、 date オブジェクトと異なる型のオブジェクトが比較されると、比較演算子が == または != でないかぎり TypeError が送出されます。後者の場合、それぞれ False または True を返します。

> date オブジェクトは辞書のキーとして用いることができます。ブール演算コンテキストでは、全ての date オブジェクトは真であるとみなされます。

### インスタンスメソッド

インスタンスメソッド|説明
--------------------|----
date.replace(year=self.year, month=self.month, day=self.day)|キーワード引数で指定されたパラメタが置き換えられることを除き、同じ値を持つ date オブジェクトを返します。例えば、d == date(2002, 12, 31) とすると、d.replace(day=26) == date(2002, 12, 26) となります。
date.timetuple()|time.localtime() が返す形式の time.struct_time を返します。時間、分、および秒は 0 で、DST フラグは -1 になります。 d.timetuple() は次の値と同値です: time.struct_time((d.year, d.month, d.day, 0, 0, 0, d.weekday(), yday, -1)) ただし yday = d.toordinal() - date(d.year, 1, 1).toordinal() + 1 が 1月1日に 1 で始まる現在の年の日を表す。
date.toordinal()|先発グレゴリオ暦における日付序数を返します。 1 年の 1 月 1 日が序数 1 となります。任意の date オブジェクト d について、 date.fromordinal(d.toordinal()) == d となります。
date.weekday()|月曜日を 0、日曜日を 6 として、曜日を整数で返します。例えば、 date(2002, 12, 4).weekday() == 2 であり、水曜日を示します。 isoweekday() も参照してください。
date.isoweekday()|月曜日を 1,日曜日を 7 として、曜日を整数で返します。例えば、 date(2002, 12, 4).isoweekday() == 3 であり、水曜日を示します。 weekday(), isocalendar() も参照してください。
date.isocalendar()|3 要素のタプル (ISO 年、ISO 週番号、ISO 曜日) を返します。グレゴリオ暦の変種。[参照](https://www.staff.science.uu.nl/~gent0113/calendar/isocalendar.htm)
date.isoformat()|ISO 8601 形式、 ‘YYYY-MM-DD’ の日付を表す文字列を返します。例えば、date(2002, 12, 4).isoformat() == '2002-12-04' となります。
date.__str__()|date オブジェクト d において、str(d) は d.isoformat() と等価です。
date.ctime()|日付を表す文字列を、例えば date(2002, 12, 4).ctime() == 'Wed Dec 4 00:00:00 2002' のようにして返します。
date.strftime(format)|明示的な書式文字列で制御された、日付を表現する文字列を返します。 [strftime() と strptime() の振る舞い](https://docs.python.jp/3/library/datetime.html#strftime-strptime-behavior)参照。
date.__format__(format)|date.strftime（）と同じです。 Same as date.strftime(). This makes it possible to specify a format string for a date object in formatted string literals and when using str.format(). For a complete list of formatting directives, see strftime() と strptime() の振る舞い. 

### イベントまでの日数を数える例

```python
import time
from datetime import date
today = date.today()
print(today)
print(today == date.fromtimestamp(time.time()))
my_birthday = date(today.year, 6, 24)
if my_birthday < today:
    my_birthday = my_birthday.replace(year=today.year + 1)
print(my_birthday)
time_to_birthday = abs(my_birthday - today)
print(time_to_birthday.days)
```
```sh
$ python 0.py 
2017-09-04
True
2018-06-24
293
```
### date と併用する例

```python
from datetime import date
d = date.fromordinal(730920) # 730920th day after 1. 1. 0001
print(d)
t = d.timetuple()
for i in t: print(i, end=', ')
print()
ic = d.isocalendar()
for i in ic: print(i, end=', ')
print()

print(d.isoformat())
print(d.strftime("%d/%m/%y"))
print(d.strftime("%A %d. %B %Y"))
print('The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month"))
```
```sh
$ python 1.py 
2002-03-11
2002, 3, 11, 0, 0, 0, 0, 70, -1, 
2002, 11, 1, 
2002-03-11
11/03/02
Monday 11. March 2002
The day is 11, the month is March.
```

