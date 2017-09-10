# [8.3.5. namedtuple() 名前付きフィールドを持つタプルのファクトリ関数](https://docs.python.jp/3/library/collections.html#namedtuple-factory-function-for-tuples-with-named-fields)

< [8.3. collections — コンテナデータ型](https://docs.python.jp/3/library/collections.html#module-collections) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/collections/__init__.py](https://github.com/python/cpython/tree/3.6/Lib/collections/__init__.py)

## 概要

> 名前付きタプルは、タプルの中のすべての場所に意味を割り当てて、より読みやすく自己解説的なコードを書けるようにします。通常のタプルが利用される場所ならどこでも利用でき、場所に対するインデックスの代わりに名前を使ってフィールドにアクセスできるようになります。

## 一覧

属性|説明
----|----
collections.namedtuple(typename, field_names, *, verbose=False, rename=False, module=None)|typename という名前の tuple の新しいサブクラスを返します。新しいサブクラスは、 tuple に似ているけれどもインデックスやイテレータだけでなく属性名によるアクセスもできるオブジェクトを作るのに使います。
classmethod somenamedtuple._make(iterable)|既存の sequence や Iterable から新しいインスタンスを作るクラスメソッド.
somenamedtuple._asdict()|フィールド名を対応する値にマッピングする新しい:class:OrderedDict を返します:
somenamedtuple._replace(kwargs)|指定されたフィールドを新しい値で置き換えた、新しい名前付きタプルを作って返します:
somenamedtuple._source|名前付きタプルクラスを作成するのに使われる pure Python ソースコードの文字列です。このソースは名前付きタプルを自己文書化します。これは表示したり、 exec() を使って実行したり、ファイルに保存してインポートしたりできます。
somenamedtuple._fields|フィールド名をリストにしたタプルです。内省 (introspection) したり、既存の名前付きタプルをもとに新しい名前つきタプルを作成する時に便利です。

## 操作

### getattr()

```python
>>> getattr(p, 'x')
11
```

### 辞書→namedtuple

```python
>>> d = {'x': 11, 'y': 22}
>>> Point(**d)
Point(x=11, y=22)
```

### 継承

> 名前付きタプルは通常の Python クラスなので、継承して機能を追加したり変更するのは容易です。次の例では計算済みフィールドと固定幅の print format を追加しています:

```python
>>> class Point(namedtuple('Point', ['x', 'y'])):
...     __slots__ = ()
...     @property
...     def hypot(self):
...         return (self.x ** 2 + self.y ** 2) ** 0.5
...     def __str__(self):
...         return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)

>>> for p in Point(3, 4), Point(14, 5/7):
...     print(p)
Point: x= 3.000  y= 4.000  hypot= 5.000
Point: x=14.000  y= 0.714  hypot=14.018
```

> このサブクラスは __slots__ に空のタプルをセットしています。これにより、インスタンス辞書の作成を抑制してメモリ使用量を低く保つのに役立ちます。

### 新フィールド追加は不可

> サブクラス化は新しいフィールドを追加するのには適していません。代わりに、新しい名前付きタプルを _fields 属性を元に作成してください:

```python
>>> Point3D = namedtuple('Point3D', Point._fields + ('z',))

__doc__ フィールドに直接代入することでドックストリングをカスタマイズすることが出来ます:
>>>

>>> Book = namedtuple('Book', ['id', 'title', 'authors'])
>>> Book.__doc__ += ': Hardcover book in active collection'
>>> Book.id.__doc__ = '13-digit ISBN'
>>> Book.title.__doc__ = 'Title of first printing'
>>> Book.authors.__doc__ = 'List of authors sorted by last name'
```

### __doc__

> バージョン 3.5 で変更: 属性ドックストリングが書き込み可能になりました。

> _replace() でプロトタイプのインスタンスをカスタマイズする方法で、デフォルト値を実装できます:

```python
>>> Account = namedtuple('Account', 'owner balance transaction_count')
>>> default_account = Account('<owner name>', 0.0, 0)
>>> johns_account = default_account._replace(owner='John')
>>> janes_account = default_account._replace(owner='Jane')
```

### 参考

> Jan Kaliszewski による 名前付きタプル抽象基底クラスとメタクラス mix-in のレシピ 。名前付きタプルの abstract base class を提供するだけでなく、 metaclass に基づくコンストラクタの代わりもサポートするので、名前付きタプルがサブクラス化されるユースケースで便利です。

* [名前付きタプル抽象基底クラスとメタクラス mix-in のレシピ](https://code.activestate.com/recipes/577629-namedtupleabc-abstract-base-class-mix-in-for-named/)
* [abstract-base-class](https://docs.python.jp/3/glossary.html#term-abstract-base-class)
* [metaclass](https://docs.python.jp/3/glossary.html#term-metaclass)

> タプルではなく、辞書をもとにした変更可能な名前空間を作成するには types.SimpleNamespace() を参照してください。

* [types.SimpleNamespace](https://docs.python.jp/3/library/types.html#types.SimpleNamespace)

> 名前付きタプルに型ヒントを追加する方法については、 typing.NamedTuple() を参照してください。

* [typing.NamedTuple](https://docs.python.jp/3/library/typing.html#typing.NamedTuple)

