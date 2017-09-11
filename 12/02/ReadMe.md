# [8.3.9. UserString オブジェクト](https://docs.python.jp/3/library/collections.html#userlist-objects)

< [8.3. collections — コンテナデータ型](https://docs.python.jp/3/library/collections.html#module-collections) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/collections/__init__.py](https://github.com/python/cpython/tree/3.6/Lib/collections/__init__.py)

## 概要

> クラス UserString は、文字列オブジェクトのラッパとしてはたらきます。このクラスの必要性は、 str から直接的にサブクラス化できる能力に部分的に取って代わられました; しかし、根底の文字列に属性としてアクセスできるので、このクラスを使った方が簡単になることもあります。

## 一覧

属性|説明
----|----
class collections.UserString([sequence])|文字列をシミュレートするクラスです。インスタンスの内容は通常の文字列に保存され、 UserString インスタンスの data 属性を通してアクセスできます。インスタンスの内容は最初に sequence のコピーに設定されます。 sequence は bytes 、 str 、 UserString (やサブクラス) のインスタンス、または組み込みの str() 関数で文字列に変換できる任意のシーケンスです。バージョン 3.5 で変更: 新たなメソッド __getnewargs__, __rmod__, casefold, format_map, isprintable, maketrans。

## コード

```python
```
```sh
```

UserStringからの継承とstrからの継承。

使い道がわからない。

