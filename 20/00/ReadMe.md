# [8.9. types — 動的な型生成と組み込み型に対する名前](https://docs.python.jp/3/library/types.html#module-types)

< [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/weakref.py](https://github.com/python/cpython/tree/3.6/Lib/types.py)

## 概要

> このモジュールは新しい型の動的な生成を支援するユーティリティ関数を定義しています。

> さらに、標準の Python インタプリタによって使用されているものの、 int や str のように組み込みとして公開されていないようないくつかのオブジェクト型の名前を定義しています。

> 最後に、組み込みになるほど基本的でないような追加の型関連のユーティリティと関数をいくつか提供しています。

### [8.9.1. 動的な型生成](https://docs.python.jp/3/library/types.html#dynamic-type-creation)

クラスメソッド|説明
--------------|----
types.new_class(name, bases=(), kwds=None, exec_body=None)|適切なメタクラスを使用して動的にクラスオブジェクトを生成します。
types.prepare_class(name, bases=(), kwds=None)|適切なメタクラスを計算してクラスの名前空間を生成します。

#### 参考

* [Metaclasses](https://docs.python.jp/3/reference/datamodel.html#metaclasses)
    * これらの関数によってサポートされるクラス生成プロセスの完全な詳細
* [PEP 3115](https://docs.python.jp/3/reference/datamodel.html#metaclasses) - Metaclasses in Python 3000
    * __prepare__ 名前空間フックの導入

#### new_class

```python
Human = types.new_class('Human', (object,), None)
print(Human())#<types.Human object at 0xb70a614c>

Human = types.new_class('Human', (object,), {'metaclass': abc.ABCMeta})
print(Human())#<abc.Human object at 0xb70a628c>
```

第3引数がよくわからなかった。

> キーワード引数 (例えば metaclass)

という説明では意味不明。

[ソースコード](https://github.com/python/cpython/blob/3.6/Lib/types.py#L79)を見たほうが早い。（ドキュメントの存在意義……）

`bases`, または`kwds`からメタクラスの型を取得しようとしているだけだった。第3引数は必要ないのでは？第2引数だけで十分では？

#### prepare_class

```python
import types
import abc
Object = types.prepare_class('Object', (object,), {})
print(Object)#(<class 'type'>, {}, {})

Human = types.prepare_class('Human', (object,), None)
print(Human)#(<class 'type'>, {}, {})

Human = types.prepare_class('Human', (object,), {'metaclass': abc.ABCMeta})
print(Human)#(<class 'abc.ABCMeta'>, {}, {})

#types()
Human = type('Human', (object,), {'name':'', 'age':0})
print(Human)
```

> 適切なメタクラスを計算してクラスの名前空間を生成します。

> 返り値は metaclass, namespace, kwds の3要素のタプルです

> metaclass は適切なメタクラスです。namespace は用意されたクラスの名前空間です。また kwds は、'metaclass' エントリが削除された、渡された kwds 引数の更新されたコピーです。kwds 引数が渡されなければ、これは空の dict になります。

翻訳が怪しい。以下の場合、`abc`が名前空間として返されると期待したが、空のdictだった。おそらく「kwds は、'metaclass' エントリが削除された、渡された kwds 引数の更新されたコピーです」という一文なのだろう。つまり、「第1引数と同じ」ということではないのか？それにしては、やたらまわりくどい言い方をしている。謎。

```python
Human = types.prepare_class('Human', (object,), {'metaclass': abc.ABCMeta})
print(Human)#(<class 'abc.ABCMeta'>, {}, {})
```

