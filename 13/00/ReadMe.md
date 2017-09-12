# [8.4. collections.abc — コレクションの抽象基底クラス](https://docs.python.jp/3/library/collections.abc.html#module-collections.abc)

< [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/_collections_abc.py](https://github.com/python/cpython/tree/3.6/Lib/_collections_abc.py)

## 概要

> このモジュールは、 抽象基底クラス を提供します。抽象基底クラスは、クラスが特定のインタフェースを提供しているか、例えばハッシュ可能であるかやマッピングであるかを判定します。

* [抽象基底クラス](https://docs.python.jp/3/glossary.html#term-abstract-base-class)

## 抽象基底クラス一覧

> collections モジュールは以下の ABC (抽象基底クラス) を提供します:

ABC|継承しているクラス|抽象メソッド|mixin メソッド
---|------------------|------------|--------------
Container| |__contains__| 
Hashable| |__hash__| 
Iterable| |__iter__| 
Iterator|Iterable|__next__|__iter__
Reversible|Iterable|__reversed__| 
Generator|Iterator|send, throw|close, __iter__, __next__
Sized| |__len__| 
Callable| |__call__| 
Collection|Sized, Iterable, Container|__contains__, __iter__, __len__| 
Sequence|Reversible, Collection|__getitem__, __len__|__contains__, __iter__, __reversed__, index, count
MutableSequence|Sequence|__getitem__, __setitem__, __delitem__, __len__, insert|Sequence から継承したメソッドと、 append, reverse, extend, pop, remove, __iadd__
ByteString|Sequence|__getitem__, __len__|Sequence から継承したメソッド
Set|Collection|__contains__, __iter__, __len__|__le__, __lt__, __eq__, __ne__, __gt__, __ge__, __and__, __or__, __sub__, __xor__, isdisjoint
MutableSet|Set|__contains__, __iter__, __len__, add, discard|Set から継承したメソッドと、 clear, pop, remove, __ior__, __iand__, __ixor__, __isub__
Mapping|Collection|__getitem__, __iter__, __len__|__contains__, keys, items, values, get, __eq__, __ne__
MutableMapping|Mapping|__getitem__, __setitem__, __delitem__, __iter__, __len__|Mapping から継承したメソッドと、 pop, popitem, clear, update, setdefault
MappingView|Sized| |__len__
ItemsView|MappingView, Set| |__contains__, __iter__
KeysView|MappingView, Set| |__contains__, __iter__
ValuesView|MappingView| |__contains__, __iter__
Awaitable| |__await__| 
Coroutine|Awaitable|send, throw|close
AsyncIterable| |__aiter__| 
AsyncIterator|AsyncIterable|__anext__|__aiter__
AsyncGenerator|AsyncIterator|asend, athrow|aclose, __aiter__, __anext__

これらを継承することで特定のメソッド実装を強要できる。1つずつ見ていくのは大変……と思ったがPython文書にも説明はわずかしかなかった。

## 用途

### クラスが特定のメソッドを備えているかまとめて確認

> これらの ABC はクラスやインスタンスが特定の機能を提供しているかどうかを調べるのに使えます。例えば:

```python
import collections.abc
myvar = [1,2,3]
if isinstance(myvar, collections.abc.Sized): print(f'size: {len(myvar)}')
else: print('not collections.abc.Sized.')
```
```sh
$ python 0.py 
size: 3
```
### 継承

> 幾つかの ABC はコンテナ型 API を提供するクラスを開発するのを助ける mixin 型としても使えます。例えば、 Set API を提供するクラスを作る場合、3つの基本になる抽象メソッド __contains__(), __iter__(), __len__() だけが必要です。ABC が残りの __and__() や isdisjoint() といったメソッドを提供します:

```python
import collections.abc
class ListBasedSet(collections.abc.Set):
    ''' Alternate set implementation favoring space over speed
        and not requiring the set elements to be hashable. '''
    def __init__(self, iterable):
        self.elements = lst = []
        for value in iterable:
            if value not in lst:
                lst.append(value)

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, value):
        return value in self.elements

    def __len__(self):
        return len(self.elements)

s1 = ListBasedSet('abcdef')
s2 = ListBasedSet('defghi')
overlap = s1 & s2            # The __and__() method is supported automatically
print(s1.elements)
print(s2.elements)
print(overlap.elements)
#print(dir(s1))
```
```sh
$ python 1.py 
['a', 'b', 'c', 'd', 'e', 'f']
['d', 'e', 'f', 'g', 'h', 'i']
['d', 'e', 'f']
```

Set と MutableSet を mixin 型として利用するときの注意点:

> 1. 幾つかの set の操作は新しい set を作るので、デフォルトの mixin メソッドは iterable から新しいインスタンスを作成する方法を必要とします。クラスのコンストラクタは ClassName(iterable) の形のシグネチャを持つと仮定されます。内部の _from_iterable() というクラスメソッドが cls(iterable) を呼び出して新しい set を作る部分でこの仮定が使われています。コンストラクタのシグネチャが異なるクラスで Set を使う場合は、 iterable 引数から新しいインスタンスを生成するように _from_iterable() をオーバーライドする必要があります。

> 2. (たぶん意味はそのままに速度を向上する目的で)比較をオーバーライドする場合、 __le__() と __ge__() だけを再定義すれば、その他の演算は自動的に追随します。

> 3. Set mixin型は set のハッシュ値を計算する _hash() メソッドを提供しますが、すべての set が hashable や immutable とは限らないので、 __hash__() は提供しません。 mixin を使ってハッシュ可能な set を作る場合は、 Set と Hashable の両方を継承して、 __hash__ = Set._hash と定義してください。

## 参考

* [OrderedSet recipe](https://code.activestate.com/recipes/576694/)
* [abc](https://docs.python.jp/3/library/abc.html#module-abc)モジュール, [PEP 3119](https://www.python.org/dev/peps/pep-3119)

