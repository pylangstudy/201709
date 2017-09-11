# [8.3.8. UserList オブジェクト](https://docs.python.jp/3/library/collections.html#userlist-objects)

< [8.3. collections — コンテナデータ型](https://docs.python.jp/3/library/collections.html#module-collections) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/collections/__init__.py](https://github.com/python/cpython/tree/3.6/Lib/collections/__init__.py)

## 概要

> このクラスはリストオブジェクトのラッパとしてはたらきます。これは独自のリスト風クラスの基底クラスとして便利で、既存のメソッドをオーバーライドしたり新しいメソッドを加えたりできます。こうして、リストに新しい振る舞いを加えられます。

> このクラスの必要性は、 list から直接的にサブクラス化できる能力に部分的に取って代わられました; しかし、根底のリストに属性としてアクセスできるので、このクラスを使った方が簡単になることもあります。

## 一覧

属性|説明
----|----
class collections.UserList([list])|リストをシミュレートするクラスです。インスタンスの内容は通常のリストに保存され、 UserList インスタンスの data 属性を通してアクセスできます。インスタンスの内容は最初に list のコピーに設定されますが、デフォルトでは空リスト [] です。 list は何らかのイテラブル、例えば通常の Python リストや UserList オブジェクト、です。
data|UserList クラスの内容を保存するために使われる実際の list オブジェクトです。

## サブクラス化の要件

> UserList のサブクラスは引数なしか、あるいは一つの引数のどちらかとともに呼び出せるコンストラクタを提供することが期待されています。新しいシーケンスを返すリスト演算は現在の実装クラスのインスタンスを作成しようとします。そのために、データ元として使われるシーケンスオブジェクトである一つのパラメータとともにコンストラクタを呼び出せると想定しています。

> 派生クラスがこの要求に従いたくないならば、このクラスがサポートしているすべての特殊メソッドはオーバーライドされる必要があります。その場合に提供される必要のあるメソッドについての情報は、ソースを参考にしてください。

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
print(hd)
```
```sh
$ python 0.py 
[0, 1, 2]
[0, 1, 2]
```

UserListからの継承とlistからの継承。

使い道がわからない。

