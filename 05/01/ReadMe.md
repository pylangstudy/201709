# [8.1.6. tzinfo オブジェクト](https://docs.python.jp/3/library/datetime.html#tzinfo-objects)

< [8.1. datetime — 基本的な日付型および時間型](https://docs.python.jp/3/library/datetime.html#module-datetime) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/datetime.py](https://github.com/python/cpython/tree/3.6/Lib/datetime.py)

tzinfoは使わないと思う。

tzinfoはタイムゾーン自作用クラスと思われる。自力で新規タイムゾーンを実装することはない。

ふつう、既存のタイムゾーンを参照するだけの使い方が一般的。その場合、tzinfoの具象クラス`datetime.timezone`を使う。しかしUTCしか存在しない。`Asia/Tokyo`などがない。

結果的に、外部ライブラリ`pytz`を使って各種タイムゾーンを参照するのが一般的と思われる。よってtzinfo, timezoneは使わない、と思う。

## 属性一覧

コンストラクタ|説明
--------------|----
class datetime.tzinfo|このクラスは抽象基底クラスで、直接インスタンス化すべきでないことを意味します。 具象サブクラスを作成し、(少なくとも) 使いたい datetime のメソッドが必要とする tzinfo のメソッドを実装する必要があります。 datetime モジュールは tzinfo のシンプルな具象サブクラス timezone を提供します。 これは UTC そのものか北アメリカの EST と EDT のような UTC からの固定されたオフセットを持つタイムゾーンを表せます。

インスタンスメソッド|説明
--------------------|----
tzinfo.utcoffset(dt)|ローカル時間の UTC からのオフセットを、 UTC から東向きを正とした分で返します。
tzinfo.dst(dt)|夏時間 (DST) 修正を、 UTC から東向きを正とした分で返します。
tzinfo.tzname(dt)|datetime オブジェクト dt に対応するタイムゾーン名を文字列で返します。
tzinfo.fromutc(dt)|デフォルトの datetime.astimezone() 実装で呼び出されます。 datetime.astimezone() から呼ばれた場合、 dt.tzinfo は self であり、 dt の日付および時刻データは UTC 時刻を表しているものとして見えます。 fromutc() の目的は、 self のローカル時刻に等しい datetime オブジェクトを返すことにより日付と時刻データメンバを修正することにあります。

