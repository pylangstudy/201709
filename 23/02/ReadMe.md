# [8.11.1. PrettyPrinter オブジェクト](https://docs.python.jp/3/library/pprint.html#prettyprinter-objects)

< [8.11. pprint — データ出力の整然化](https://docs.python.jp/3/library/pprint.html#module-pprint) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/pprint.py](https://github.com/python/cpython/tree/3.6/Lib/pprint.py)

## 一覧

> PrettyPrinter インスタンスには以下のメソッドがあります:

属性|説明
----|----
PrettyPrinter.pformat(object)|object の書式化した表現を返します。これは PrettyPrinter のコンストラクタに渡されたオプションを考慮して書式化されます。
PrettyPrinter.pprint(object)|object の書式化した表現を指定したストリームに出力し、最後に改行します。
PrettyPrinter.isreadable(object)|object を書式化して出力できる（”readable”）か、あるいは eval() を使って値を再構成できるかを返します。これは再帰的なオブジェクトに対して False を返すことに注意して下さい。もし PrettyPrinter の depth 引数が設定されていて、オブジェクトのレベルが設定よりも深かったら、 False を返します。
PrettyPrinter.isrecursive(object)|オブジェクトが再帰的な表現かどうかを返します。
PrettyPrinter.format(object, context, maxlevels, level)|次の3つの値を返します。object をフォーマット化して文字列にしたもの、その結果が読み込み可能かどうかを示すフラグ、再帰が含まれているかどうかを示すフラグ。最初の引数は表示するオブジェクトです。 2つめの引数はオブジェクトの id() をキーとして含むディクショナリで、オブジェクトを含んでいる現在の（直接、間接に object のコンテナとして表示に影響を与える）環境です。ディクショナリ context の中でどのオブジェクトが表示されたか表示する必要があるなら、3つめの返り値は True になります。 format() メソッドの再帰呼び出しではこのディクショナリのコンテナに対してさらにエントリを加えます。 3つめの引数 maxlevels で再帰呼び出しのレベルを制限します。制限しない場合、 0 になります。この引数は再帰呼び出しでそのまま渡されます。 4つめの引数 level で現在のレベルを設定します。再帰呼び出しでは、現在の呼び出しより小さい値が渡されます。

## コード例

```python
import pprint
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter()
print(pp.pformat(stuff))
pp.pprint(stuff)
print(pp.isreadable(stuff))
print(pp.isrecursive(stuff))
print(pp.format(stuff, locals(), 0, 0))
```
```sh
$ python 0.py 
[['spam', 'eggs', 'lumberjack', 'knights', 'ni'],
 'spam',
 'eggs',
 'lumberjack',
 'knights',
 'ni']
[['spam', 'eggs', 'lumberjack', 'knights', 'ni'],
 'spam',
 'eggs',
 'lumberjack',
 'knights',
 'ni']
True
False
("[['spam', 'eggs', 'lumberjack', 'knights', 'ni'], 'spam', 'eggs', 'lumberjack', 'knights', 'ni']", True, False)
```

