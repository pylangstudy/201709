# [8.3.4. defaultdict オブジェクト](https://docs.python.jp/3/library/collections.html#defaultdict-objects)

< [8.3. collections — コンテナデータ型](https://docs.python.jp/3/library/collections.html#module-collections) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/collections/__init__.py](https://github.com/python/cpython/tree/3.6/Lib/collections/__init__.py)

コンストラクタ|説明
--------------|----
class collections.defaultdict([default_factory[, ...]])|新しいディクショナリ様のオブジェクトを返します。 defaultdict は組み込みの dict のサブクラスです。

インスタンスメソッド|説明
--------------------|----
__missing__(key)|もし default_factory 属性が None であれば、このメソッドは KeyError 例外を、 key を引数として発生させます。

defaultdict オブジェクトは以下のインスタンス変数をサポートしています:

インスタンス変数|説明
----------------|----
default_factory|この属性は __missing__() メソッドによって使われます。これは存在すればコンストラクタの第1引数によって初期化され、そうでなければ None になります。

## [8.3.4.1. defaultdict の使用例](https://docs.python.jp/3/library/collections.html#defaultdict-examples)

* 要素を複数管理したい
* 要素はすべて特定の型にしたい
* 要素にそれぞれ一意の名前をつけたい
* mutable（変更可能）である

### dictの要素型を指定する

#### list型

```python
from collections import defaultdict
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print(s)
d = defaultdict(list)
for k, v in s: d[k].append(v)
print(sorted(d.items()))
```
```sh
$ python 0.py 
[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
```

集合のような使い方。

##### setdefault()

`d = defaultdict(list)`の別の手段。ただし冗長である。

```python
...
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = {}
for k, v in s: d.setdefault(k, []).append(v)
print(sorted(d.items()))
```
```sh
$ python 1.py 
[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
...
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
```

#### int型

```python
from collections import defaultdict
s = 'mississippi'
d = defaultdict(int)
for k in s: d[k] += 1
print(sorted(d.items()))
```
```sh
$ python 2.py 
[('i', 4), ('m', 1), ('p', 2), ('s', 4)]
```

Counterのような使い方。

> 最初に文字が出現したときは、マッピングが存在しないので default_factory 関数が int() を呼んでデフォルトのカウント0を生成します。インクリメント操作が各文字を数え上げます。

#### lambda型

```python
from collections import defaultdict
def constant_factory(value):
    return lambda: value
d = defaultdict(constant_factory('<missing>'))
d.update(name='John', action='ran')
print('%(name)s %(action)s to %(object)s' % d)
```
```sh
$ python 3.py 
John ran to <missing>
```

#### set型

```python
from collections import defaultdict
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
print(s)
d = defaultdict(set)
for k, v in s:
    d[k].add(v)
print(sorted(d.items()))
```
```sh
$ python 4.py 
[('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
[('blue', {2, 4}), ('red', {1, 3})]
```

重複を排除するset型。

