# [8.1.5. time オブジェクト](https://docs.python.jp/3/library/datetime.html#time-objects)

< [8.1. datetime — 基本的な日付型および時間型](https://docs.python.jp/3/library/datetime.html#module-datetime) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/datetime.py](https://github.com/python/cpython/tree/3.6/Lib/datetime.py)

## 概要

> time オブジェクトは (ローカルの) 日中時刻を表現します。この時刻表現は特定の日の影響を受けず、 tzinfo オブジェクトを介した修正の対象となります。

* [tzinfo](https://docs.python.jp/3/library/datetime.html#datetime.tzinfo)

## 属性一覧

## 以下にクラス属性を示します:

クラス属性|説明
----------|----
time.min|表現できる最も古い time で、 time(0, 0, 0, 0) です。
time.max|表現できる最も新しい time で、 time(23, 59, 59, 999999) です。
time.resolution|等しくない time オブジェクト間の最小の差で、 timedelta(microseconds=1) ですが, time オブジェクト間の四則演算はサポートされていないので注意してください。

クラスメソッド|説明
--------------|----
なし|なし

インスタンス属性|説明
----------------|----
time.hour|in range(24) を満たします。
time.minute|in range(60) を満たします。
time.second|in range(60) を満たします。
time.microsecond|in range(1000000) を満たします。
time.tzinfo|time コンストラクタに tzinfo 引数として与えられたオブジェクトになり、何も渡されなかった場合には None になります。
time.fold|In [0、1]である。繰り返しの間に壁の時間を明確にするために使用されます。 （夏時間の終了時にクロックがロールバックされたり、現在のゾーンのUTCオフセットが政治的理由により減少した場合、繰り返し間隔が発生します。）値0（1）は、同じ壁の時間表現。（In [0, 1]. Used to disambiguate wall times during a repeated interval. (A repeated interval occurs when clocks are rolled back at the end of daylight saving time or when the UTC offset for the current zone is decreased for political reasons.) The value 0 (1) represents the earlier (later) of the two moments with the same wall time representation.）バージョン 3.6 で追加.

「壁の時間」とは一体……。

インスタンスメソッド|説明
--------------------|----
time.replace(hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, * fold=0)|キーワード引数で指定したメンバの値を除き、同じ値をもつ time オブジェクトを返します。
time.isoformat(timespec='auto')|ISO 8601形式、HH：MM：SS.mmmmmm、またはマイクロ秒が0の場合はHH：MM：SSの時刻を表す文字列を返します。。utcoffset（）がNoneを返さない場合、6文字の文字列が追加され、UTC HH：MM：SS.mmmmmm + HH：MMまたは、self.microsecondが0の場合、HH：MM：SS + HH：MM（オフセット）。timespec=['auto','hours','minutes','seconds','milliseconds','microseconds'] （Return a string representing the time in ISO 8601 format, HH:MM:SS.mmmmmm or, if microsecond is 0, HH:MM:SS If utcoffset() does not return None, a 6-character string is appended, giving the UTC offset in (signed) hours and minutes: HH:MM:SS.mmmmmm+HH:MM or, if self.microsecond is 0, HH:MM:SS+HH:MM）
time.__str__()|time オブジェクト t において、str(t) は t.isoformat() と等価です。
time.strftime(format)|明示的な書式文字列で制御された、時刻を表現する文字列を返します。完全な書式化ディレクティブのリストについては strftime() と strptime() の振る舞い を参照してください。
time.__format__(format)|strftime()と同じ。Same as time.strftime(). This makes it possible to specify a format string for a time object in formatted string literals and when using str.format(). For a complete list of formatting directives, see strftime() と strptime() の振る舞い.
time.utcoffset()|tzinfo が None の場合 None を返し、そうでない場合には self.tzinfo.utcoffset(None) を返します。 後者の式が None もしくは、1 日未満の経過時間を表す timedelta オブジェクトのいずれかを返さない場合には例外を送出します。
time.dst()|tzinfo が None の場合 None を返し、そうでない場合には self.tzinfo.dst(None) を返します。 後者の式が None もしくは、 1日未満の経過時間を表す timedelta オブジェクトのいずれかを返さない場合には例外を送出します。
time.tzname()|tzinfo が None の場合 None を返し、そうでない場合には self.tzinfo.tzname(None) を返します。 後者の式が None か文字列オブジェクトのいずれかを返さない場合には例外を送出します。

## サポートされている演算

    time と time の比較では、 a が b より前の時刻だった場合 a が b より小さいとされます。比較の一方が naive であり、もう一方が aware の場合に、順序比較が行われると TypeError が送出されます。等価比較では、 naive インスタンスと aware インスタンスは等価になることはありません。

    比較対象が両方とも aware であり、同じ tzinfo 属性を持つ場合、 tzinfo は無視され datetime だけで比較が行われます。 比較対象が両方とも aware であり、異なる tzinfo 属性を持つ場合、まず最初に (self.utcoffset() で取得できる) それぞれの UTC オフセットを引いて調整します。 異なる型どうしの比較がデフォルトのオブジェクトアドレス比較となってしまうのを防ぐために、 time オブジェクトを異なる型のオブジェクトと比較すると、比較演算子が == または != でないかぎり TypeError が送出されます。 比較演算子が == または != である場合、それぞれ False または True を返します。

    バージョン 3.3 で変更: naive な time インスタンスと aware な time インスタンスの等価比較では、 TypeError は送出されません。

    ハッシュ化、辞書のキーとしての利用

    効率的な pickle 化

ブール値の文脈では、 time オブジェクトは常に真とみなされます。

バージョン 3.5 で変更: Python 3.5 以前は、 time オブジェクトは UTC で深夜を表すときに偽とみなされていました。 この挙動は分かりにくく、エラーの元となると考えられ、Python 3.5 で削除されました。 全詳細については bpo-13936 を参照してください。

## インスタンスメソッド:











例:
>>>

>>> from datetime import time, tzinfo, timedelta
>>> class GMT1(tzinfo):
...     def utcoffset(self, dt):
...         return timedelta(hours=1)
...     def dst(self, dt):
...         return timedelta(0)
...     def tzname(self,dt):
...         return "Europe/Prague"
...
>>> t = time(12, 10, 30, tzinfo=GMT1())
>>> t                               
datetime.time(12, 10, 30, tzinfo=<GMT1 object at 0x...>)
>>> gmt = GMT1()
>>> t.isoformat()
'12:10:30+01:00'
>>> t.dst()
datetime.timedelta(0)
>>> t.tzname()
'Europe/Prague'
>>> t.strftime("%H:%M:%S %Z")
'12:10:30 Europe/Prague'
>>> 'The {} is {:%H:%M}.'.format("time", t)
'The time is 12:10.'


