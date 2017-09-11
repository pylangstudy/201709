# [8.3.7. UserDict オブジェクト](https://docs.python.jp/3/library/collections.html#userdict-objects)

< [8.3. collections — コンテナデータ型](https://docs.python.jp/3/library/collections.html#module-collections) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/collections/__init__.py](https://github.com/python/cpython/tree/3.6/Lib/collections/__init__.py)

## 概要

> クラス UserDict は、辞書オブジェクトのラッパとしてはたらきます。このクラスの必要性は、 dict から直接的にサブクラス化できる能力に部分的に取って代わられました; しかし、根底の辞書に属性としてアクセスできるので、このクラスを使った方が簡単になることもあります。

## 一覧

属性|説明
----|----
class collections.UserDict([initialdata])|辞書をシミュレートするクラスです。インスタンスの内容は通常の辞書に保存され、 UserDict インスタンスの data 属性を通してアクセスできます。
data|UserDict クラスの内容を保存するために使われる実際の辞書です。

## コード

```python
from collections import UserDict

class HumanUD(UserDict):
    def __init__(self, d):
        self.data = {}
        if isinstance(d, dict):
            self.data.update(d)

class HumanD(dict):
    def __init__(self, d):
        if isinstance(d, dict):
            self.update(d)


d = {'name':'Yamada', 'age':100}
hud = HumanUD(d)
hd = HumanD(d)
print(hud)
print(d)
```
```sh
$ python 0.py 
{'name': 'Yamada', 'age': 100}
{'name': 'Yamada', 'age': 100}
```

UserDictからの継承とdictからの継承。

使い道がわからない。

