# [8.3.6. OrderedDict オブジェクト](https://docs.python.jp/3/library/collections.html#ordereddict-objects)

< [8.3. collections — コンテナデータ型](https://docs.python.jp/3/library/collections.html#module-collections) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/collections/__init__.py](https://github.com/python/cpython/tree/3.6/Lib/collections/__init__.py)

## 概要

> 名前付きタプルは、タプルの中のすべての場所に意味を割り当てて、より読みやすく自己解説的なコードを書けるようにします。通常のタプルが利用される場所ならどこでも利用でき、場所に対するインデックスの代わりに名前を使ってフィールドにアクセスできるようになります。

## 一覧

属性|説明
----|----
 class collections.OrderedDict([items])|通常の dict メソッドをサポートする、辞書のサブクラスのインスタンスを返します。 OrderedDict は、キーが最初に追加された順序を記憶します。新しい項目が既存の項目を上書きしても、元の挿入位置は変わらないままです。項目を削除して再挿入するとそれが最後に移動します。
popitem(last=True)|順序付き辞書の popitem() メソッドは、(key, value) 対を返して消去します。この対は last が真なら LIFO で、偽なら FIFO (first-in, first-out 先入先出)` で返されます。
move_to_end(key, last=True)|既存の key を順序付き辞書の両端に移動します。項目は、 last が真 (デフォルト) なら右端に、 last が偽なら最初に移動されます。 key が存在しなければ KeyError を送出します:

0.py参照

## [8.3.6.1. OrderedDict の例とレシピ](https://docs.python.jp/3/library/collections.html#ordereddict-examples-and-recipes)

1.py,2.py,3.py参照
