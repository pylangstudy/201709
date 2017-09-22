# [8.12. reprlib — もう一つの repr() の実装](https://docs.python.jp/3/library/reprlib.html)

< [8.11. pprint — データ出力の整然化](https://docs.python.jp/3/library/pprint.html#module-pprint) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/reprlib.py](https://github.com/python/cpython/tree/3.6/Lib/reprlib.py)

## 概要

> reprlib モジュールは、結果の文字列のサイズに対する制限付きでオブジェクト表現を生成するための手段を提供します。これは Python デバッガの中で使用されており、他の文脈でも同様に役に立つかもしれません。

> このモジュールはクラスとインスタンス、それに関数を提供します:

## 一覧

属性|説明
----|----
class reprlib.Repr|組み込み関数 repr() に似た関数を実装するために役に立つフォーマット用サービスを提供します。 過度に長い表現を作り出さないようにするための大きさの制限をオブジェクト型ごとに設定できます。
reprlib.aRepr|これは下で説明される repr() 関数を提供するために使われる Repr のインスタンスです。このオブジェクトの属性を変更すると、 repr() と Python デバッガが使うサイズ制限に影響します。
reprlib.repr(obj)|これは aRepr の repr() メソッドです。同じ名前の組み込み関数が返す文字列と似ていますが、最大サイズに制限のある文字列を返します。
@reprlib.recursive_repr(fillvalue="...")|__repr__() メソッドに対する同一スレッド内の再帰呼び出しを検出するデコレータです。再帰呼び出しが行われている場合 fillvalue が返されます。そうでなければ通常の __repr__() 呼び出しが行われます。例えば:

## コード例

```python
import reprlib
class MyList(list):
    @reprlib.recursive_repr()
    def __repr__(self):
        return '<' + '|'.join(map(repr, self)) + '>'
m = MyList('abc')
m.append(m)
m.append('x')
print(m)
```
```sh
$ python 0.py 
<'a'|'b'|'c'|...|'x'>
```

## [8.12.1. Reprオブジェクト](https://docs.python.jp/3/library/reprlib.html#repr-objects)

> Repr インスタンスはオブジェクト型毎に表現する文字列のサイズを制限するために使えるいくつかの属性と、特定のオブジェクト型をフォーマットするメソッドを提供します。

属性|説明
----|----
Repr.maxlevel|再帰的な表現を作る場合の深さ制限。デフォルトは 6 です。
Repr.maxdict, Repr.maxlist, Repr.maxtuple, Repr.maxset, Repr.maxfrozenset, Repr.maxdeque, Repr.maxarray|指定されたオブジェクト型に対するエントリ表現の数についての制限。 maxdict に対するデフォルトは 4 で、 maxarray は 5 、その他に対しては 6 です。
Repr.maxlong|整数の表現のおける文字数の最大値。中央の数字が抜け落ちます。デフォルトは 40 です。
Repr.maxstring|文字列の表現における文字数の制限。文字列の”通常の”表現は文字の「元」として使われることに注意してください。表現にエスケープシーケンスが必要とされる場合、表現が短縮されるときにこれらのエスケープシーケンスの形式は崩れます。デフォルトは 30 です。
Repr.maxother|この制限は Repr オブジェクトに利用できる特定のフォーマットメソッドがないオブジェクト型のサイズをコントロールするために使われます。 maxstring と同じようなやり方で適用されます。デフォルトは 20 です。
Repr.repr(obj)|このインスタンスで設定されたフォーマットを使う、組み込み repr() と等価なもの。
Repr.repr1(obj, level)|repr() が使う再帰的な実装。 obj の型を使ってどのフォーマットメソッドを呼び出すかを決定し、それに obj と level を渡します。 再帰呼び出しにおいて level の値に対して level - 1 を与える再帰的なフォーマットを実行するために、型に固有のメソッドは repr1() を呼び出します。
Repr.repr_TYPE(obj, level)|型名に基づく名前をもつメソッドとして、特定の型に対するフォーマットメソッドは実装されます。メソッド名では、 TYPE は '_'.join(type(obj).__name__.split()) に置き換えられます。これらのメソッドへのディスパッチは repr1() によって処理されます。再帰的に値をフォーマットする必要がある型固有のメソッドは、 self.repr1(subobj, level - 1) を呼び出します。

```python
import reprlib
r = reprlib.Repr()
print(r)
print(r.maxdict)
print(r.maxlist)
print(r.maxtuple)
print(r.maxset)
print(r.maxfrozenset)
print(r.maxdeque)
print(r.maxarray)

print(r.maxlong)
print(r.maxstring)
print(r.maxother)
print(r.repr)
print(r.repr1)
print(r.repr_TYPE({}, 0))#AttributeError: 'Repr' object has no attribute 'repr_TYPE'
```
```sh
$ python 1.py 
<reprlib.Repr object at 0xb70f0d6c>
4
6
6
6
6
6
5
40
30
30
<bound method Repr.repr of <reprlib.Repr object at 0xb70f0d6c>>
<bound method Repr.repr1 of <reprlib.Repr object at 0xb70f0d6c>>
Traceback (most recent call last):
  File "1.py", line 17, in <module>
    print(r.repr_TYPE({}, 0))#AttributeError: 'Repr' object has no attribute 'repr_TYPE'
AttributeError: 'Repr' object has no attribute 'repr_TYPE'
```

## [8.12.2. Reprオブジェクトをサブクラス化する](https://docs.python.jp/3/library/reprlib.html#subclassing-repr-objects)

> 更なる組み込みオブジェクト型へのサポートを追加するため、あるいはすでにサポートされている型の扱いを変更するために、 Repr.repr1() による動的なディスパッチは Repr のサブクラス化に対応しています。 この例はファイルオブジェクトのための特別なサポートを追加する方法を示しています:

```python
import reprlib
import sys

class MyRepr(reprlib.Repr):
    def repr_TextIOWrapper(self, obj, level):
        if obj.name in {'<stdin>', '<stdout>', '<stderr>'}:
            return obj.name
        return repr(obj)

aRepr = MyRepr()
print(aRepr.repr(sys.stdin))         # prints '<stdin>'
```
```sh
$ python 2.py 
<stdin>
```
