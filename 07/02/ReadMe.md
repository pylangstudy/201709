# [8.3.1.1. ChainMap の例とレシピ](https://docs.python.jp/3/library/collections.html#chainmap-examples-and-recipes)

[8.3.1. ChainMap オブジェクト](https://docs.python.jp/3/library/collections.html#chainmap-objects) < [8.3. collections — コンテナデータ型](https://docs.python.jp/3/library/collections.html#module-collections) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/collections/__init__.py](https://github.com/python/cpython/tree/3.6/Lib/collections/__init__.py)

ChainMapは不要。dictのlistに過ぎない。

## 概要

> この節では、チェーンされたマッピングを扱う様々な手法を示します。

例によってPython文書そのままだと動かない。エラー箇所もあった。適当に修正する。

### Python の内部探索チェーンをシミュレートする例

```python
import collections
import builtins
pylookup = collections.ChainMap(locals(), globals(), vars(builtins))
print(pylookup)
```

わざわざ二重にデータを持つ必要性はどこにある？

### ユーザ指定のコマンドライン引数、環境変数、デフォルト値、の順に優先させる例

```python
import collections
import os, argparse
defaults = {'color': 'red', 'user': 'guest'}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k:v for k, v in vars(namespace).items() if v}

combined = collections.ChainMap(command_line_args, os.environ, defaults)
print(combined['color'])
print(combined['user'])
```

使いそうと思ったが、最終的には、コマンドライン引数、環境変数、デフォルト値、をそれぞれ統合し、ひとつの参照に絞りこまねば使えない。そのための処理が必要。横着してこのようにしても、あとでどれを参照するかはそれぞれの処理に任されるため、処理毎に参照先を定めるための手続きの実装が必要になる。面倒。最初に一度統合してしまったほうが楽。するとChainMapは使わず、dictだけで十分。

また、データを多重に持たせるためメモリの無駄。

何も良いことがないように思える。

### ChainMap を使ってネストされたコンテキストをシミュレートするパターンの例

```python
import collections
c = collections.ChainMap()        # Create root context
d = c.new_child()     # Create nested child context
e = c.new_child()     # Child of c, independent from d
e.maps[0]             # Current context dictionary -- like Python's locals()
e.maps[-1]            # Root context -- like Python's globals()
e.parents             # Enclosing context chain -- like Python's nonlocals

#d['x']                # Get first key in the chain of contexts     KeyError: 'x'
d['x'] = 1            # Set value in current context
d['x']                # Get first key in the chain of contexts
del d['x']            # Delete from current context
list(d)               # All nested values
#k in d                # Check all nested values                    NameError: name 'k' is not defined
[k for k in d]                # Check all nested values
len(d)                # Number of nested values
d.items()             # All nested items
dict(d)               # Flatten into a regular dictionary
```

ネストされた名前空間を利用したいとき、`new_child()`などの名前はわかりやすい……か？。単純なdictとlistの場合、`namespace = [{}]; namespace.append({});`とする。別にそれでもいいと思う。むしろ新しいメソッド名を覚えずに済むので楽。

### サブクラス

> ChainMap クラスは、探索はチェーン全体に対して行いますが、更新 (書き込みと削除) は最初のマッピングに対してのみ行います。しかし、深い書き込みと削除を望むなら、チェーンの深いところで見つかったキーを更新するサブクラスを簡単に作れます:

```python
import collections
class DeepChainMap(collections.ChainMap):
    'Variant of ChainMap that allows direct updates to inner scopes'
    def __setitem__(self, key, value):
        for mapping in self.maps:
            if key in mapping:
                mapping[key] = value
                return
        self.maps[0][key] = value

    def __delitem__(self, key):
        for mapping in self.maps:
            if key in mapping:
                del mapping[key]
                return
        raise KeyError(key)

d = DeepChainMap({'zebra': 'black'}, {'elephant': 'blue'}, {'lion': 'yellow'})
print(d)
d['lion'] = 'orange'         # update an existing key two levels down
d['snake'] = 'red'           # new keys get added to the topmost dict
del d['elephant']            # remove an existing key one level down
print(d)
```
```sh
$ python 3.py 
DeepChainMap({'zebra': 'black'}, {'elephant': 'blue'}, {'lion': 'yellow'})
DeepChainMap({'zebra': 'black', 'snake': 'red'}, {}, {'lion': 'orange'})
```

面倒くさい。わざと面倒にしているように思える。dictとlistを使えば以下で済む。

```python
namespace = [{'zebra': 'black'}, {'elephant': 'blue'}, {'lion': 'yellow'}]
print(namespace)
namespace[2]['lion'] = 'orange'
namespace[0]['snake'] = 'red'
#del namespace[1]
namespace[1].clear()
print(namespace)
```
```sh
$ python 4.py 
[{'zebra': 'black'}, {'elephant': 'blue'}, {'lion': 'yellow'}]
[{'zebra': 'black', 'snake': 'red'}, {}, {'lion': 'orange'}]
```

Python文書のほうが正しいはずだと信じて、自らのコードを疑ってみたが、以下のように論破されてしまった。

* listのインデックスが面倒では？
    * もし不要なら単なるdict型でいい。現にキー名も重複していない
* `del`でclear()の意味にしたいのだが？
    * 本来の意味と違ってしまう。混乱させたなら好きにすればいい

Python文書コードの利点をさがしてみようとしたが、見つからなかった。

* `namespace[1].clear()`より`del d['elephant']`のほうがわかりやすい
    * `__delitem__`の実装を見てみると全dictのキーから削除しているだけ。だったら最初からdict型でいいし、そのほうがわかりやすい。DeepChainMapのような実装をする必要性が不明

## 所感

ChainMapの必要性や価値が見いだせなかった。要らない子認定。

