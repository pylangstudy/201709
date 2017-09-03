# [8.1. datetime — 基本的な日付型および時間型](https://docs.python.jp/3/library/datetime.html#module-datetime)

< [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/datetime.py](https://github.com/python/cpython/tree/3.6/Lib/datetime.py)

## 概要

> datetime モジュールでは、日付や時間データを簡単な方法と複雑な方法の両方で操作するためのクラスを提供しています。日付や時刻を対象にした四則演算がサポートされている一方で、このモジュールの実装では出力の書式化や操作を目的とした属性の効率的な取り出しに焦点を絞っています。機能については、 time および calendar も参照してください。

>“naive” と “aware” の2種類の日付と時刻オブジェクトがあります。

### aware

> aware オブジェクトは他の aware オブジェクトとの相対関係を把握出来るように、タイムゾーンや夏時間の情報のような、アルゴリズム的で政治的な適用可能な時間調節に関する知識を持っています。aware オブジェクトは解釈の余地のない特定の実時刻を表現するのに利用されます [1]。

### naive

> naive オブジェクトには他の日付時刻オブジェクトとの相対関係を把握するのに足る情報が含まれません。あるプログラム内の数字がメートルを表わしているのか、マイルなのか、それとも質量なのかがプログラムによって異なるように、naive オブジェクトが協定世界時 (UTC) なのか、現地時間なのか、それとも他のタイムゾーンなのかはそのプログラムに依存します。Naive オブジェクトはいくつかの現実的な側面を無視してしまうというコストを無視すれば、簡単に理解でき、うまく利用することができます。

### tzinfo

aware オブジェクトを必要とするアプリケーションのために、 datetime と time オブジェクトは追加のタイムゾーン情報の属性 tzinfo を持ちます。 tzinfo には抽象クラス tzinfo のサブクラスのインスタンスを設定することができます。 これらの tzinfo オブジェクトは UTC 時間からのオフセットやタイムゾーンの名前、夏時間が実施されるかの情報を保持しています。 ただ一つの具象 tzinfo クラスである timezone クラスが datetime モジュールで提供されています。 timezone クラスは単純な UTC からの固定オフセットだけを表わすUTC 自身や北アメリカの EST や EDT タイムゾーンのようなものも表現できます。 より深く詳細までタイムゾーンをサポートするかはアプリケーションに依存します。 世界中の時刻の調整を決めるルールは合理的というよりかは政治的なもので、頻繁に変わり、UTC を除くと都合のよい基準というものはありません。

## 定数

> datetime モジュールでは以下の定数を公開しています:

定数|説明
----|----
datetime.MINYEAR|date や datetime オブジェクトで許されている、年を表現する最小の数字です。 MINYEAR は 1 です。
datetime.MAXYEAR|date や datetime オブジェクトで許されている、年を表現する最大の数字です。 MAXYEAR は 9999 です。

```python
import datetime
print(datetime.MINYEAR)
print(datetime.MAXYEAR)
```
```sh
$ python 0.py 
1
9999
```

### 参考

* [calendar](https://docs.python.jp/3/library/calendar.html#module-calendar) モジュール(汎用のカレンダー関連関数)
* [time](https://docs.python.jp/3/library/time.html#module-time) モジュール(時刻へのアクセスと変換)

