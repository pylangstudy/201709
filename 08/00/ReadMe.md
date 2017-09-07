# [8.3.2. Counter オブジェクト](https://docs.python.jp/3/library/collections.html#counter-objects)

< [8.3. collections — コンテナデータ型](https://docs.python.jp/3/library/collections.html#module-collections) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/collections/__init__.py](https://github.com/python/cpython/tree/3.6/Lib/collections/__init__.py)

ChainMapは不要。dictのlistに過ぎない。

## 概要

> 便利で迅速な検数をサポートするカウンタツールが提供されています。例えば:

```python
import collections

cnt = collections.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print(cnt)

import re
words = re.findall(r'\w+', 'my name is is ann.')
print(collections.Counter(words).most_common(10))
```
```sh
$ python 0.py 
Counter({'blue': 3, 'red': 2, 'green': 1})
[('is', 2), ('my', 1), ('name', 1), ('ann', 1)]
```

## 属性

コンストラクタ|説明
--------------|----
class collections.Counter([iterable-or-mapping])|Counter はハッシュ可能なオブジェクトをカウントする dict のサブクラスです。これは、要素を辞書のキーとして保存し、そのカウントを辞書の値として保存する、順序付けされていないコレクションです。カウントは、0 や負のカウントを含む整数値をとれます。

> カウンタオブジェクトは、すべての辞書で利用できるメソッドに加えて、次の 3 つのメソッドをサポートしています。

インスタンスメソッド|説明
--------------------|----
elements()|それぞれの要素を、そのカウント分の回数だけ繰り返すイテレータを返します。要素は任意の順序で返されます。ある要素のカウントが 1 未満なら、 elements() はそれを無視します。
most_common([n])|最も多い n 要素を、カウントが多いものから少ないものまで順に並べたリストを返します。 n が省略されるか None であれば、 most_common() はカウンタの すべての 要素を返します。等しいカウントの要素は任意に並べられます。バージョン 3.2 で追加.

> 普通の辞書のメソッドは、以下の 2 つのメソッドがカウンタに対して異なる振る舞いをするのを除き、 Counter オブジェクトにも利用できます。

インスタンスメソッド|説明
--------------------|----
fromkeys(iterable)|このクラスメソッドは Counter オブジェクトには実装されていません。
update([iterable-or-mapping])|要素が iterable からカウントされるか、別の mapping (やカウンタ) が追加されます。 dict.update() に似ていますが、カウントを置き換えるのではなく追加します。また、 iterable には (key, value) 対のシーケンスではなく、要素のシーケンスが求められます。

## わかりづらい点

* 自然数(1以上の整数)と負数(0以下の整数)を使い分ける必要がある
    * `+c`, `-c`, 演算などの操作により、正数もしくは負数が消えてしまう
        * どちらかが消えてしまいうる and どちらを消すか意識する ことが必要不可欠になる
            * 加算だけする単なるカウンタではない（できそうな機能はとにかくつぎ込んだような実装）
* 0以下の場合、操作方法ごとに結果が変わってしまう（統一性がない）
    * 代入(`c['key'] = -1`): キーごと残る
    * 演算(`c - d`): キーごと消える

## 不便な点

* 並べ替えキーが必ずカウント値である（キー名でソートできない）

## 自作

4.py
```python
class Counter:
    def __init__(self):
        self.__values = {}
    def count(self, name):
        if name not in self.__values: self.__values[name] = 0
        self.__values[name] += 1
    @property
    def Values(self): return self.__values
```

これで十分では？言語仕様のせいでカプセル化できないから必要性も感じないが。

## 所感

安心して使えない印象。

elements()、使いどころが不明。用途とか考えずに用意したメソッドだろこれ……。そういうメソッド多すぎ。邪魔。

こんなものよりC言語のようなインクリメント(`c++`)が使いたい。`counter.key++`とできたら楽なのだが、現実は`counter['key'] += 1`である……。

未だにPythonに慣れない。

