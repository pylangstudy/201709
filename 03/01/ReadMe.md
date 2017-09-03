# [8.1.1. 利用可能なデータ型](https://docs.python.jp/3/library/datetime.html#available-types)

< [8.1. datetime — 基本的な日付型および時間型](https://docs.python.jp/3/library/datetime.html#module-datetime) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/datetime.py](https://github.com/python/cpython/tree/3.6/Lib/datetime.py)

## 概要

属性|説明
----|----
class datetime.date|理想的な naive な日付で、これまでもこれからも現在のグレゴリオ暦 (Gregorian calender) が有効であることを仮定しています。 属性は year, month,および day です。
class datetime.time|理想的な時刻で、特定の日から独立しており、毎日が厳密に 24*60*60 秒であると仮定しています (“うるう秒: leap seconds” の概念はありません)。 属性は hour, minute, second, microsecond, および tzinfo です。
class datetime.datetime|日付と時刻を組み合わせたものです。 属性は year, month, day, hour, minute, second, microsecond, および tzinfo です。
class datetime.timedelta|date, time, あるいは datetime クラスの二つのインスタンス間の時間差をマイクロ秒精度で表す経過時間値です。
class datetime.tzinfo|タイムゾーン情報オブジェクトの抽象基底クラスです。 datetime および time クラスで用いられ、カスタマイズ可能な時刻修正の概念 (たとえばタイムゾーンや夏時間の計算）を提供します。
class datetime.timezone|tzinfo 抽象基底クラスを UTC からの固定オフセットとして実装するクラスです。|バージョン 3.2 で追加.

```python
import datetime
print(datetime.date)
print(datetime.time)
print(datetime.datetime)
print(datetime.timedelta)
print(datetime.tzinfo)
print(datetime.timezone)
```
```sh
$ python 0.py 
<class 'datetime.date'>
<class 'datetime.time'>
<class 'datetime.datetime'>
<class 'datetime.timedelta'>
<class 'datetime.tzinfo'>
<class 'datetime.timezone'>
```

> これらの型のオブジェクトは変更不可能 (immutable) です。

> date 型のオブジェクトは常に naive です。

> time や datetime 型のオブジェクトは naive か aware のどちらかになります。 datetime オブジェクト d は d.tzinfo が None でなく d.tzinfo.utcoffset(d) が None を返さない場合、aware です。d.tzinfo が None であるか d.tzinfo が None でないが d.tzinfo.utcoffset(d) が None を返す場合、 d は naive です。 time のオブジェクト t は t.tzinfo が None でなく t.tzinfo.utcoffset(None) が None を返さない場合に aware になって、それ以外の場合には t は naive になります。

> naive なオブジェクトと aware なオブジェクトの区別は timedelta オブジェクトにはあてはまりません。
サブクラスの関係は以下のようになります:

```
object
    timedelta
    tzinfo
        timezone
    time
    date
        datetime
```

