# [8.9.3. 追加のユーティリティクラスと関数](https://docs.python.jp/3/library/types.html#additional-utility-classes-and-functions)

< [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/weakref.py](https://github.com/python/cpython/tree/3.6/Lib/types.py)

## 概要

> このモジュールは、Python インタプリタを実装するために必要な多くの型に対して名前を提供します。それは、listiterator 型のような、単に処理中に付随的に発生するいくつかの型が含まれることを意図的に避けています。

> これらの名前は典型的に isinstance() や issubclass() によるチェックに使われます。

## 一覧

属性|説明
----|----
class types.SimpleNamespace|名前空間への属性アクセスに加えて意味のある repr を提供するための、単純な object サブクラスです。
types.DynamicClassAttribute(fget=None, fset=None, fdel=None, doc=None)|クラスの属性アクセスを __getattr__ に振り替えます。

### class types.SimpleNamespace

> 名前空間への属性アクセスに加えて意味のある repr を提供するための、単純な object サブクラスです。

> object とは異なり、 SimpleNamespace は、属性を追加したり削除したりすることができます。 SimpleNamespace オブジェクトがキーワード引数で初期化される場合、それらは元になる名前空間に直接追加されます。

> この型は以下のコードとほぼ等価です:

```python
class SimpleNamespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        keys = sorted(self.__dict__)
        items = ("{}={!r}".format(k, self.__dict__[k]) for k in keys)
        return "{}({})".format(type(self).__name__, ", ".join(items))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
```

> SimpleNamespace は class NS: pass を置き換えるものとして有用かもしれません。ですが、構造化されたレコード型に対しては、これよりはむしろ namedtuple() を使用してください。

> バージョン 3.3 で追加.

```python
import types

print(types.SimpleNamespace)
print(dir(types.SimpleNamespace))

Human = types.SimpleNamespace(**{'Name':'', 'Age':0})
print(Human)
print(dir(Human))
print(Human.Name)
print(Human.Age)
print(Human.__repr__())
print(Human.Name.__repr__())
print(Human.Age.__repr__())
#print(Human())#TypeError: 'types.SimpleNamespace' object is not callable
```
```sh
$ python 0.py 
<class 'types.SimpleNamespace'>
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
namespace(Age=0, Name='')
['Age', 'Name', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

0
namespace(Age=0, Name='')
''
0
```

### types.DynamicClassAttribute(fget=None, fset=None, fdel=None, doc=None)

> クラスの属性アクセスを __getattr__ に振り替えます。

> これは記述子で、インスタンス経由のアクセスとクラス経由のアクセスで振る舞いが異なる属性を定義するのに使います。インスタンスアクセスは通常通りですが、クラス経由の属性アクセスはクラスの __getattr__ メソッドに振り替えられます。これは AttributeError の送出により行われます。

> これによって、インスタンス上で有効なプロパティを持ち、クラス上で同名の仮想属性を持つことができます (例については Enum を参照してください)。

> バージョン 3.4 で追加.

クラスオブジェクトとインスタンスで異なる動作をさせたいときに使う。

* クラスオブジェクトでアクセスされたときは、同名属性のクラス変数を返す。
* クラスインスタンスでアクセスされたときは、同名属性の`@DynamicClassAttribute`付きインスタンス関数の戻り値を返す。

```python
from types import DynamicClassAttribute

# Metaclass
class Funny(type):
    def __getattr__(self, value):
        print('search in meta')
        # Normally you would implement here some ifs/elifs or a lookup in a dictionary
        # but I'll just return the attribute
        return Funny.dynprop
    # Metaclasses dynprop:
    dynprop = 'Meta'

class Fun(metaclass=Funny):
    def __init__(self, value):
        self._dynprop = value
    @DynamicClassAttribute
    def dynprop(self):
        return self._dynprop

print('-------クラス変数---------')
print(Fun.dynprop)#Meta
print('-------インスタンス変数---------')
fun = Fun('Not-Meta')
print(fun)
print(fun.dynprop)#Not-Meta
```
```sh
----------------
search in meta
Meta
----------------
<__main__.Fun object at 0xb713c24c>
Not-Meta
```

いつも通り、Python文書だけでは使い方がわからなかった。以下参照。感謝。

* https://stackoverflow.com/questions/36040996/what-is-a-dynamicclassattribute-and-how-do-i-use-it

