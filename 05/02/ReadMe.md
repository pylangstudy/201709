# [8.1.7. timezone オブジェクト](https://docs.python.jp/3/library/datetime.html#timezone-objects)

< [8.1. datetime — 基本的な日付型および時間型](https://docs.python.jp/3/library/datetime.html#module-datetime) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/datetime.py](https://github.com/python/cpython/tree/3.6/Lib/datetime.py)

> timezone クラスは tzinfo のサブクラスで、各インスタンスは UTC からの固定されたオフセットで定義されたタイムゾーンを表しています。このクラスのオブジェクトは、一年のうち異なる日に異なるオフセットが使われていたり、常用時 (civil time) に歴史的な変化が起きた場所のタイムゾーン情報を表すのには使えないので注意してください。

標準ライブラリの`tzinfo`, `timezone`は使わないと思う。かわりに`pytz`を使う。

tzinfoはタイムゾーン自作用クラスと思われる。自力で新規タイムゾーンを実装することはない。

ふつう、既存のタイムゾーンを参照するだけの使い方が一般的。その場合、tzinfoの具象クラス`datetime.timezone`を使う。しかしUTCしか存在しない。`Asia/Tokyo`などがない。

結果的に、外部ライブラリ`pytz`を使って各種タイムゾーンを参照するのが一般的と思われる。よってtzinfo, timezoneは使わない、と思う。

## 属性一覧

クラス属性|説明
----------|----
timezone.utc|UTC タイムゾーン timezone(timedelta(0)) です。

コンストラクタ|説明
--------------|----
class datetime.timezone(offset, name=None)|ローカル時刻と UTC の差分を表す timedelta オブジェクトを offset 引数に指定しなくてはいけません。これは -timedelta(hours=24) から timedelta(hours=24) までの両端を含まない範囲に収まっており、分単位で表現していなくてはなりません。そうでない場合 ValueError が送出されます。

インスタンスメソッド|説明
--------------------|----
timezone.utcoffset(dt)|timezone インスタンスの作成時に指定された固定の値を返します。 dt 引数は無視されます。返り値は、ローカル時刻と UTC の差分に等しい timedelta インスタンスです。
timezone.tzname(dt)|Return the fixed value specified when the timezone instance is constructed. If name is not provided in the constructor, the name returned by tzname(dt) is generated from the value of the offset as follows. If offset is timedelta(0), the name is “UTC”, otherwise it is a string ‘UTC±HH:MM’, where ± is the sign of offset, HH and MM are two digits of offset.hours and offset.minutes respectively.
timezone.dst(dt)|常に None を返します。
timezone.fromutc(dt)|dt + offset を返します。 dt 引数は tzinfo が self になっている aware な datetime インスタンスでなければなりません。

