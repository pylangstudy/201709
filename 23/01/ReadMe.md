# [8.11. pprint — データ出力の整然化](https://docs.python.jp/3/library/pprint.html#module-pprint)

< [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/pprint.py](https://github.com/python/cpython/tree/3.6/Lib/pprint.py)

## 概要

> pprint モジュールを使うと、Pythonの任意のデータ構造をインタープリタへの入力で使われる形式にして “pretty-print” できます。書式化された構造の中にPythonの基本的なタイプではないオブジェクトがあるなら、表示できないかもしれません。表示できないのは、ファイル、ソケット、あるいはクラスのようなオブジェクトや、 その他Pythonのリテラルとして表現できない様々なオブジェクトが含まれていた場合です。

> 可能であればオブジェクトを1行で整形しますが、与えられた幅に合わないなら複数行に分けて整形します。 出力幅を指定したい場合は、 PrettyPrinter オブジェクトを作成して明示してください。

> 辞書は表示される前にキーの順でソートされます。

> pprint モジュールには1つのクラスが定義されています:

## 一覧

属性|説明
----|----
class pprint.PrettyPrinter(indent=1, width=80, depth=None, stream=None, *, compact=False)|PrettyPrinter インスタンスを作ります。

属性|説明
----|----
pprint.pformat(object, indent=1, width=80, depth=None, *, compact=False)|object を書式化して文字列として返します。
pprint.pprint(object, stream=None, indent=1, width=80, depth=None, *, compact=False)|stream 上に object の書式化された表現、続いて改行を出力します。
pprint.isreadable(object)|object を書式化して出力できる(“readable”) か、あるいは eval() を使って値を再構成できるかを返します。再帰的なオブジェクトに対しては常に False を返します。
pprint.isrecursive(object)|object が再帰的な表現かどうかを返します。
pprint.saferepr(object)|object の文字列表現を、再帰的なデータ構造から保護した形式で返します。もし object の文字列表現が再帰的な要素を持っているなら、再帰的な参照は <Recursion on typename with id=number> で表示されます。出力は他と違って書式化されません。

## コード例

```python
import pprint
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)
pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(stuff)
tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead', ('parrot', ('fresh fruit',))))))))
pp = pprint.PrettyPrinter(depth=6)
pp.pprint(tup)
```
```sh
$ python 0.py 
[   ['spam', 'eggs', 'lumberjack', 'knights', 'ni'],
    'spam',
    'eggs',
    'lumberjack',
    'knights',
    'ni']
[['spam', 'eggs', 'lumberjack',
  'knights', 'ni'],
 'spam', 'eggs', 'lumberjack', 'knights',
 'ni']
('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead', (...)))))))
```

```python
import pprint
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff)
pprint.pprint(stuff)

print(pprint.isreadable(stuff))
print(pprint.saferepr(stuff))
```
```sh
$ python 1.py 
[<Recursion on list with id=3070976684>,
 'spam',
 'eggs',
 'lumberjack',
 'knights',
 'ni']
False
[<Recursion on list with id=3070976684>, 'spam', 'eggs', 'lumberjack', 'knights', 'ni']
```








## 詳細

### 浅い or 深い

> 浅い (shallow) コピーと深い (deep) コピーの違いが関係するのは、複合オブジェクト (リストやクラスインスタンスのような他のオブジェクトを含むオブジェクト) だけです:

#### 浅いコピー

> 浅いコピー (shallow copy) は新たな複合オブジェクトを作成し、その後 (可能な限り) 元のオブジェクト中に見つかったオブジェクトに対する 参照 を挿入します。

#### 深いコピー

> 深いコピー (deep copy) は新たな複合オブジェクトを作成し、その後元のオブジェクト中に見つかったオブジェクトの コピー を挿入します。

> 深いコピー操作には、しばしば浅いコピー操作の時には存在しない 2 つの問題がついてまわります:

> 再帰的なオブジェクト (直接、間接に関わらず、自分自身に対する参照を持つ複合オブジェクト) は再帰ループを引き起こします。

> 深いコピーは何もかもコピーしてしまうため、例えば複数のコピー間で共有するつもりだったデータも余分にコピーしてしまいます。

#### 回避

> deepcopy() 関数では、これらの問題を以下のようにして回避しています:

> 現在のコピー過程ですでにコピーされたオブジェクトからなる、”メモ” 辞書を保持します; かつ

> ユーザ定義のクラスでコピー操作やコピーされる内容の集合を上書きできるようにします。

### コピーしないもの

> このモジュールでは、モジュール、メソッド、スタックトレース、スタックフレーム、ファイル、ソケット、ウィンドウ、アレイ、その他これらに類似の型をコピーしません。このモジュールでは元のオブジェクトを変更せずに返すことで関数とクラスを (浅くまたは深く)「コピー」します。これは pickle モジュールでの扱われかたと同じです。

### dict.copy()

> 辞書型の浅いコピーは dict.copy() で、リストの浅いコピーはリスト全体を指すスライス (例えば copied_list = original_list[:]) でできます。

### pickleインタフェース

> クラスは、コピーを制御するために pickle の制御に使用するのと同じインターフェースを使用することができます。これらのメソッドについての情報はモジュール pickle の説明を参照してください。実際、 copy モジュールは、 copyreg モジュールによって登録された picle 関数を使用します。

### __copy__, __deepcopy__

クラス独自のコピー実装を定義するために、特殊メソッド __copy__() および __deepcopy__() を定義することができます。前者は浅いコピー操作を実装するために使われます; 追加の引数はありません。後者は深いコピー操作を実現するために呼び出されます; この関数には単一の引数としてメモ辞書が渡されます。 __deepcopy__() の実装で、内容のオブジェクトに対して深いコピーを生成する必要がある場合、 deepcopy() を呼び出し、最初の引数にそのオブジェクトを、メモ辞書を二つ目の引数に与えなければなりません。

### 参考

* [pickle](https://docs.python.jp/3/library/pickle.html#module-pickle) モジュール

> オブジェクト状態の取得と復元をサポートするために使われる特殊メソッドについて議論されています。

