# [8.3. collections — コンテナデータ型](https://docs.python.jp/3/library/collections.html#module-collections)

< [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/collections/__init__.py](https://github.com/python/cpython/tree/3.6/Lib/collections/__init__.py)

## 概要

> このモジュールは、汎用の Python 組み込みコンテナ dict, list, set, および tuple に代わる、特殊なコンテナデータ型を実装しています。

* [dict](https://docs.python.jp/3/library/stdtypes.html#dict)
* [list](https://docs.python.jp/3/library/stdtypes.html#list)
* [set](https://docs.python.jp/3/library/stdtypes.html#set)
* [tuple](https://docs.python.jp/3/library/stdtypes.html#tuple)

型|説明
--|----
[namedtuple](https://docs.python.jp/3/library/collections.html#collections.namedtuple)|名前付きフィールドを持つタプルのサブクラスを作成するファクトリ関数
[deque](https://docs.python.jp/3/library/collections.html#collections.deque)|両端における append や pop を高速に行えるリスト風のコンテナ
[ChainMap](https://docs.python.jp/3/library/collections.html#collections.ChainMap)|複数のマッピングの一つのビューを作成する辞書風のクラス
[Counter](https://docs.python.jp/3/library/collections.html#collections.Counter)|ハッシュ可能なオブジェクトを数え上げる辞書のサブクラス
[OrderedDict](https://docs.python.jp/3/library/collections.html#collections.OrderedDict)|項目が追加された順序を記憶する辞書のサブクラス
[defaultdict](https://docs.python.jp/3/library/collections.html#collections.defaultdict)|ファクトリ関数を呼び出して存在しない値を供給する辞書のサブクラス
[UserDict](https://docs.python.jp/3/library/collections.html#collections.UserDict)|辞書のサブクラス化を簡単にする辞書オブジェクトのラッパ
[UserList](https://docs.python.jp/3/library/collections.html#collections.UserList)|リストのサブクラス化を簡単にするリストオブジェクトのラッパ
[UserString](https://docs.python.jp/3/library/collections.html#collections.UserString)|文字列のサブクラス化を簡単にする文字列オブジェクトのラッパ

> バージョン 3.3 で変更: コレクション抽象基底クラス が collections.abc モジュールに移動されました。後方互換性のため、それらは引き続きこのモジュールでも利用できます。

* [コレクション抽象基底クラス](https://docs.python.jp/3/library/collections.abc.html#collections-abstract-base-classes)
* [collections.abc](https://docs.python.jp/3/library/collections.abc.html#module-collections.abc)

