# [8.1.4. datetime オブジェクト](https://docs.python.jp/3/library/datetime.html#datetime-objects)

< [8.1. datetime — 基本的な日付型および時間型](https://docs.python.jp/3/library/datetime.html#module-datetime) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/datetime.py](https://github.com/python/cpython/tree/3.6/Lib/datetime.py)

## 概要

> datetime オブジェクトは date オブジェクトおよび time オブジェクトの全ての情報が入っている単一のオブジェクトです。 date オブジェクトと同様に、 datetime は現在のグレゴリオ暦が両方向に延長されているものと仮定します; また、 time オブジェクトと同様に, datetime は毎日が厳密に 3600*24 秒であると仮定します。

つまり、うるう秒は無視するということか。

* [date](https://docs.python.jp/3/library/datetime.html#datetime.date)
* [time](https://docs.python.jp/3/library/datetime.html#datetime.time)

## 属性一覧

### モジュール属性

コンストラクタ|説明
--------------|----
class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)|年、月、および日の引数は必須です。 tzinfo は None または tzinfo クラスのサブクラスのインスタンスにすることができます。残りの引数は整数

### クラス属性

クラスメソッド|説明
--------------|----
classmethod datetime.today()|現在のローカルな datetime を返します。 tzinfo は None です。 この関数は datetime.fromtimestamp(time.time()) と等価です。 now(), fromtimestamp() も参照してください。
classmethod datetime.now(tz=None)|現在のローカルな日付および時刻を返します。
classmethod datetime.utcnow()|tzinfo が None である現在の UTC の日付および時刻を返します。
classmethod datetime.fromtimestamp(timestamp, tz=None)|time.time() が返すような、 POSIX タイムスタンプに対応するローカルな日付と時刻を返します。
classmethod datetime.utcfromtimestamp(timestamp)|与えられた POSIX タイムスタンプに対応する UTC の datetime で、 tzinfo が None に設定されたものを返します。
classmethod datetime.fromordinal(ordinal)|1 年 1 月 1 日を序数 1 とする早期グレゴリオ暦序数に対応する datetime オブジェクトを返します。
classmethod datetime.combine(date, time, tzinfo=self.tzinfo)|日付コンポーネントが指定された日付オブジェクトと等しく、時刻コンポーネントが指定された時刻オブジェクトに等しい新しいdatetimeオブジェクトを返します。
classmethod datetime.strptime(date_string, format)|date_string に対応した datetime を返します。 format にしたがって構文解析されます。

クラス属性|説明
----------|----
datetime.min|表現できる最も古い datetime で、 datetime(MINYEAR, 1, 1, tzinfo=None) です。
datetime.max|表現できる最も新しい datetime で、 datetime(MAXYEAR, 12, 31, 23, 59, 59, 999999, tzinfo=None) です。
datetime.resolution|等しくない datetime オブジェクト間の最小の差で、 timedelta(microseconds=1) です。
インスタンスの属性 (読み込みのみ):
datetime.year|両端値を含む MINYEAR から MAXYEAR までの値です。
datetime.month|両端値を含む 1 から 12 までの値です。
datetime.day|1 から与えられた月と年における日数までの値です。
datetime.hour|in range(24) を満たします。。
datetime.minute|in range(60) を満たします。
datetime.second|in range(60) を満たします。
datetime.microsecond|in range(1000000) を満たします。
datetime.tzinfo|datetime コンストラクタに tzinfo 引数として与えられたオブジェクトになり、何も渡されなかった場合には None になります。
datetime.fold|繰り返しの間に壁の時間を明確にするために使用されます。In [0, 1]. Used to disambiguate wall times during a repeated interval. (A repeated interval occurs when clocks are rolled back at the end of daylight saving time or when the UTC offset for the current zone is decreased for political reasons.) The value 0 (1) represents the earlier (later) of the two moments with the same wall time representation.

### インスタンス属性

インスタンス属性 (読込のみ)|説明
---------------------------|----
year|年
month|月
day|日
hour|時
minute|分
second|秒
microsecond|マイクロ秒

インスタンスメソッド|説明
--------------------|----
datetime.date()|同じ年、月、日の date オブジェクトを返します。
datetime.time()|Return time object with same hour, minute, second, microsecond and fold. tzinfo is None. See also method timetz().
datetime.timetz()|Return time object with same hour, minute, second, microsecond, fold, and tzinfo attributes. See also method time().
datetime.replace(year=self.year, month=self.month, day=self.day, hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, * fold=0)|キーワード引数で指定した属性の値を除き、同じ属性をもつ datetime オブジェクトを返します。メンバに対する変換を行わずに aware な datetime オブジェクトから naive な datetime オブジェクトを生成するために、tzinfo=None を指定することもできます。
datetime.astimezone(tz=None)|tz を新たに tzinfo 属性 として持つ datetime オブジェクトを返します。 日付および時刻データを調整して、返り値が self と同じ UTC 時刻を持ち、 tz におけるローカルな時刻を表すようにします。
datetime.utcoffset()|tzinfo が None の場合、 None を返し、そうでない場合には self.tzinfo.utcoffset(self) を返します。 後者の式が None か、1 日以下の大きさを持つ経過時間を表す timedelta オブジェクトのいずれかを返さない場合には例外を送出します。
datetime.dst()|tzinfo が None の場合 None を返し、そうでない場合には self.tzinfo.dst(self) を返します。 後者の式が None もしくは、1 日未満の経過時間を表す timedelta オブジェクトのいずれかを返さない場合には例外を送出します。
datetime.tzname()|tzinfo が None の場合 None を返し、そうでない場合には self.tzinfo.tzname(self) を返します。 後者の式が None か文字列オブジェクトのいずれかを返さない場合には例外を送出します。
datetime.timetuple()|time.localtime() が返す形式の time.struct_time を返します。
datetime.utctimetuple()|datetime インスタンス d が naive の場合、このメソッドは d.timetuple() と同じであり、 d.dst() の返す内容にかかわらず tm_isdst が 0 に強制される点だけが異なります。
datetime.toordinal()|先発グレゴリオ暦における日付序数を返します。self.date().toordinal() と同じです。
datetime.timestamp()|datetime インスタンスに対応する POSIX タイムスタンプを返します。
datetime.weekday()|月曜日を 0、日曜日を 6 として、曜日を整数で返します。 self.date().weekday() と同じです。 isoweekday() も参照してください。
datetime.isoweekday()|月曜日を 1、日曜日を 7 として、曜日を整数で返します。 self.date().isoweekday() と等価です。 weekday() 、 isocalendar() も参照してください。
datetime.isocalendar()|3 要素のタプル (ISO 年、ISO 週番号、ISO 曜日) を返します。self.date().isocalendar() と等価です。
datetime.isoformat(sep='T', timespec='auto')|日付と時刻を ISO 8601 形式、すなわち YYYY-MM-DDTHH:MM:SS.mmmmmm か、 microsecond が 0 の場合には YYYY-MM-DDTHH:MM:SS で表した文字列を返します。
datetime.__str__()|datetime オブジェクト d において、 str(d) は d.isoformat(' ') と等価です。
datetime.ctime()|日付を表す文字列を、例えば datetime(2002, 12, 4, 20, 30, 40).ctime() == 'Wed Dec  4 20:30:40 2002' のようにして返します。
datetime.strftime(format)|明示的な書式文字列で制御された、日付および時刻を表現する文字列を返します。完全な書式化ディレクティブのリストについては strftime() と strptime() の振る舞い を参照してください。
datetime.__format__(format)|datetime.strftime（）と同じです。

## サポートされている演算

演算|結果
----|----
`datetime2 = datetime1 + timedelta`|(1)
`datetime2 = datetime1 - timedelta`|(2)
`timedelta = datetime1 - datetime2`|(3)
`datetime1 < datetime2`|datetime を datetime と比較します。 (4)

> (1) datetime2 は datetime1 から時間 timedelta 移動したもので、 timedelta.days > 0 の場合未来へ、 timedelta.days < 0 の場合過去へ移動します。 結果は入力の datetime と同じ tzinfo 属性を持ち、演算後には datetime2 - datetime1 == timedelta となります。 datetime2.year が MINYEAR よりも小さいか、 MAXYEAR より大きい場合には OverflowError が送出されます。 入力が aware なオブジェクトの場合でもタイムゾーン修正は全く行われません。

> (2) datetime2 + timedelta == datetime1 となるような datetime2 を計算します。 ちなみに、結果は入力の datetime と同じ tzinfo 属性を持ち、入力が aware でもタイムゾーン修正は全く行われません。 この操作は date1 + (-timedelta) と等価ではありません。 なぜならば、 date1 - timedelta がオーバフローしない場合でも、-timedelta 単体がオーバフローする可能性があるからです。

> (3) datetime から datetime の減算は両方の被演算子が naive であるか、両方とも aware である場合にのみ定義されています。片方が aware でもう一方が naive の場合、 TypeError が送出されます。

> 両方とも naive か、両方とも aware で同じ tzinfo 属性を持つ場合、 tzinfo 属性は無視され、結果は datetime2 + t == datetime1 であるような timedelta オブジェクト t となります。 この場合タイムゾーン修正は全く行われません。

> 両方が aware で異なる tzinfo 属性を持つ場合、 a-b は a および b をまず naive な UTC datetime オブジェクトに変換したかのようにして行います。 演算結果は決してオーバフローを起こさないことを除き、 (a.replace(tzinfo=None) - a.utcoffset()) - (b.replace(tzinfo=None) - b.utcoffset()) と同じになります。

> (4) datetime1 が時刻として datetime2 よりも前を表す場合に、datetime1 は datetime2 よりも小さいと見なされます。

> 比較の一方が naive であり、もう一方が aware の場合に、順序比較が行われると TypeError が送出されます。等価比較では、 naive インスタンスと aware インスタンスは等価になることはありません。

> 比較対象が両方とも aware で、同じ tzinfo 属性を持つ場合、 tzinfo は無視され datetime だけで比較が行われます。 比較対象が両方とも aware であり、異なる tzinfo 属性を持つ場合、まず最初に (self.utcoffset() で取得できる) それぞれの UTC オフセットを引いて調整します。

> バージョン 3.3 で変更: naive な datetime インスタンスと aware な datetime インスタンスの等価比較では TypeError は送出されません。

### 注釈:

> 型混合の比較がデフォルトのオブジェクトアドレス比較となってしまうのを抑止するために、被演算子のもう一方が datetime オブジェクトと異なる型のオブジェクトの場合には TypeError が送出されます。しかしながら、被比較演算子のもう一方が timetuple() 属性を持つ場合には NotImplemented が返されます。このフックにより、他種の日付オブジェクトに型混合比較を実装するチャンスを与えています。そうでない場合, datetime オブジェクトと異なる型のオブジェクトが比較されると、比較演算子が == または != でないかぎり TypeError が送出されます。後者の場合、それぞれ False または True を返します。

> datetime オブジェクトは辞書のキーとして用いることができます。ブール演算コンテキストでは、全ての datetime オブジェクトは真であるとみなされます。

### datetime オブジェクトを使う例

```python
from datetime import datetime, date, time
# Using datetime.combine()
d = date(2005, 7, 14)
t = time(12, 30)
print(datetime.combine(d, t))
# Using datetime.now() or datetime.utcnow()
print(datetime.now())
print(datetime.utcnow())
# Using datetime.strptime()
dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print(dt)
# Using datetime.timetuple() to get tuple of all attributes
tt = dt.timetuple()
for it in tt: print(it, end=',')
print()
# Date in ISO format
ic = dt.isocalendar()
for it in ic: print(it, end=',')
print()
# Formatting datetime
print(dt.strftime("%A, %d. %B %Y %I:%M%p"))
print('The {1} is {0:%d}, the {2} is {0:%B}, the {3} is {0:%I:%M%p}.'.format(dt, "day", "month", "time"))
```

```sh
$ python 0.py 
2005-07-14 12:30:00
2017-09-04 08:45:10.443678
2017-09-03 23:45:10.443753
2006-11-21 16:30:00
2006,11,21,16,30,0,1,325,-1,
2006,47,2,
Tuesday, 21. November 2006 04:30PM
The day is 21, the month is November, the time is 04:30PM.
```

### datetime を tzinfo と組み合わせて使う:

```python
from datetime import datetime, date, time
from datetime import timedelta, datetime, tzinfo
class GMT1(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=1) + self.dst(dt)
    def dst(self, dt):
        # DST starts last Sunday in March
        d = datetime(dt.year, 4, 1)   # ends last Sunday in October
        self.dston = d - timedelta(days=d.weekday() + 1)
        d = datetime(dt.year, 11, 1)
        self.dstoff = d - timedelta(days=d.weekday() + 1)
        if self.dston <=  dt.replace(tzinfo=None) < self.dstoff:
            return timedelta(hours=1)
        else:
            return timedelta(0)
    def tzname(self,dt):
         return "GMT +1"
   
class GMT2(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=2) + self.dst(dt)
    def dst(self, dt):
        d = datetime(dt.year, 4, 1)
        self.dston = d - timedelta(days=d.weekday() + 1)
        d = datetime(dt.year, 11, 1)
        self.dstoff = d - timedelta(days=d.weekday() + 1)
        if self.dston <=  dt.replace(tzinfo=None) < self.dstoff:
            return timedelta(hours=1)
        else:
            return timedelta(0)
    def tzname(self,dt):
        return "GMT +2"
   
gmt1 = GMT1()
# Daylight Saving Time
dt1 = datetime(2006, 11, 21, 16, 30, tzinfo=gmt1)
print(dt1.dst())
print(dt1.utcoffset())
dt2 = datetime(2006, 6, 14, 13, 0, tzinfo=gmt1)
print(dt2.dst())
print(dt2.utcoffset())
# Convert datetime to another time zone
dt3 = dt2.astimezone(GMT2())
print(dt3)
print(dt2)
print(dt2.utctimetuple() == dt3.utctimetuple())
```
```sh
 $ python 1.py 
0:00:00
1:00:00
1:00:00
2:00:00
2006-06-14 14:00:00+03:00
2006-06-14 13:00:00+02:00
True
```

