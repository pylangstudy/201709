# [8.3.1. ChainMap オブジェクト](https://docs.python.jp/3/library/collections.html#chainmap-objects)

< [8.3. collections — コンテナデータ型](https://docs.python.jp/3/library/collections.html#module-collections) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/collections/__init__.py](https://github.com/python/cpython/tree/3.6/Lib/collections/__init__.py)

ChainMapは不要。dictのlistに過ぎない。

## 概要

> バージョン 3.3 で追加.

> ChainMap クラスは、複数のマッピングを素早く連結し、一つの単位として扱うために提供されています。これはたいてい、新しい辞書を作成して update() を繰り返すよりも早いです。

> このクラスはネストされたスコープをシミュレートするのに使え、テンプレート化に便利です。

属性|説明
----|----
class collections.ChainMap(*maps)|ChainMap は、複数の辞書やその他のマッピングをまとめて、一つの、更新可能なビューを作成します。
maps|マッピングのユーザがアップデートできるリストです。
new_child(m=None)|新しい辞書の後ろに現在のインスタンスにある全ての辞書が続いたものを持つ、新しい ChainMap を返します。
parents|現在のインスタンスの最初のマッピング以外のすべてのマッピングを含む新しい ChainMap を返すプロパティです。

### 参考

#### [CodeTools](https://github.com/enthought/codetools).[MultiContext](https://github.com/enthought/codetools/blob/4.0.0/codetools/contexts/multi_context.py)

> Enthought 社の CodeTools パッケージ に含まれる MultiContext クラス は、チェーン内のすべてのマッピングへの書き込みをサポートするオプションを持ちます。

#### [Context](https://github.com/django/django/blob/master/django/template/context.py)クラス

> Django のテンプレート用の Context class は、読み込み専用のマッピングのチェーンです。 new_child() メソッドや parents() プロパティに似た push や pop の機能もあります。

#### [Nested Contexts recipe](https://code.activestate.com/recipes/577434/)

> Nested Contexts recipe は、書き込みその他の変更が最初のマッピングにのみ適用されるか、チェーンのすべてのマッピングに適用されるか、制御するオプションを持ちます。

#### [Chainmap](https://code.activestate.com/recipes/305268/)

[非常に単純化した読み出し専用バージョンの Chainmap](https://code.activestate.com/recipes/305268/)。

## 参考

* http://qiita.com/Kodaira_/items/b2cd37dfe216746723cc

## コード

```python
import collections

cm = collections.ChainMap()
print(cm.maps)
print(cm.new_child({'a':'A'}))#インスタンスに変更なし
print(cm.maps)

print(cm.maps[0].update({'b':'B'}))#更新
print(cm.maps.append({'c':'C'}))#追加
print(cm.maps.append({'d':'D'}))
print(cm.maps)

print(cm.parents)#最初の項目を飛ばす
```
```sh
$ python collections.ChainMap.py 
[{}]
ChainMap({'a': 'A'}, {})
[{}]
None
None
None
[{'b': 'B'}, {'c': 'C'}, {'d': 'D'}]
ChainMap({'c': 'C'}, {'d': 'D'})
```

dictとlistの操作が必要。そしてそれらの操作を知っていればChainMap型とその操作はまかなえる。

ChainMapの必要性を感じない。余計な型がある分、検討したり名前を覚えねばならないだけ。

## 所感

ChainMapは覚える必要なし。ChainMapという専用のクラス名やメソッド名を覚えるより、都度`[{},{},{},...]`を作ればいいだけだと思う。

* `[{},{},{},...]`
    * 単にdictのlistに過ぎない
    * 名前にchildやparentを使っているのは、listの順序を親子に見立てているに過ぎない

