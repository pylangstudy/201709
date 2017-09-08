# [8.3.3.1. deque のレシピ](https://docs.python.jp/3/library/collections.html#deque-recipes)

< [8.3.3. deque オブジェクト](https://docs.python.jp/3/library/collections.html#deque-objects) < [8.3. collections — コンテナデータ型](https://docs.python.jp/3/library/collections.html#module-collections) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/collections/__init__.py](https://github.com/python/cpython/tree/3.6/Lib/collections/__init__.py)

> この節では deque を使った様々なアプローチを紹介します。

## 最後尾にある要素を指定数分だけ取得する

> 長さが制限された deque は Unix における tail フィルタに相当する機能を提供します:

```python
def tail(filename, n=10):
    with open(filename) as f:
        return deque(f, n)
```

tailフィルタとやらが何か知らない。ようするに「最後尾にある要素を指定数分だけ取得する」らしい。

```python
from collections import deque
print(deque('abcdefg', 3))
```
```sh
$ python 0.py
deque(['e', 'f', 'g'], maxlen=3)
```

## deque

```python
import collections
import itertools
def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    d = collections.deque(itertools.islice(it, n-1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n

for a in moving_average([40, 30, 50, 46, 39, 44]): print(a)
```

[移動平均](https://ja.wikipedia.org/wiki/%E7%A7%BB%E5%8B%95%E5%B9%B3%E5%9D%87)。難しくてわからない。

> deque を使用する別のアプローチは、右に要素を追加し左から要素を取り出すことで最近追加した要素のシーケンスを保持することです:

`append()`、`popleft()`のことを言っているのだろう。

そもそもdequeはどういうデータ構造なのか。両端queueのことらしい。

* https://ja.wikipedia.org/wiki/%E4%B8%A1%E7%AB%AF%E3%82%AD%E3%83%A5%E3%83%BC

ふつうのqueueはいわゆるFIFO(先入れ先出し)。dequeは両端queueなので先頭と末尾どちらからでも要素の出し入れ可能。

queueから要素をとりだす操作をdequeue, とりこむ操作をenqueueと呼ぶ。今回のdequeは`double-ended queue`の略。dequeueだと操作名と重複してしまうため、dequeと呼ぶらしい。

## 指定位置にある要素の削除

```python
import collections

def delete_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)

d = collections.deque('abcdefg')
print(d)
delete_nth(d, 3)
print(d)
```
```sh
$ python 2.py 
deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
deque(['a', 'b', 'c', 'e', 'f', 'g'])
```

もはやFIFOも両端も関係ないのでは？こんな使い方したらデータ構造の意味がないと思うのだが。操作の方法を限定することがデータ構造の意義なのでは？

> deque のスライスの実装でも、同様のアプローチを使います。まず対象となる要素を rotate() によって deque の左端まで移動させてから、 popleft() で古い要素を削除します。そして、 extend() で新しい要素を追加したのち、循環を逆にします。このアプローチをやや変えたものとして、Forth スタイルのスタック操作、つまり dup, drop, swap, over, pick, rot, および roll を実装するのも簡単です。

* [Forth](https://ja.wikipedia.org/wiki/Forth)

[Forth](https://ja.wikipedia.org/wiki/Forth)が何なのか良くわからない。Pythonのdequeに関する話から大きく逸れている。それについて知らないと理解できないのか？私はとりあえずメソッドの名前と実行結果だけ把握できればOKとする。

