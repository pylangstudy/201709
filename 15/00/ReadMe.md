# [8.6. bisect — 配列二分法アルゴリズム](https://docs.python.jp/3/library/bisect.html)

< [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/bisect.py](https://github.com/python/cpython/tree/3.6/Lib/bisect.py)

## 概要

> このモジュールは、挿入の度にリストをソートすることなく、リストをソートされた順序に保つことをサポートします。大量の比較操作を伴うような、アイテムがたくさんあるリストでは、より一般的なアプローチに比べて、パフォーマンスが向上します。動作に基本的な二分法アルゴリズムを使っているので、 bisect と呼ばれています。ソースコードはこのアルゴリズムの実例として一番役に立つかもしれません (境界条件はすでに正しいです!)。

## 一覧

属性|説明
----|----
bisect.bisect_left(a, x, lo=0, hi=len(a))|ソートされた順序を保ったまま x を a に挿入できる点を探し当てます。リストの中から検索する部分集合を指定するには、パラメーターの lo と hi を使います。デフォルトでは、リスト全体が使われます。x がすでに a に含まれている場合、挿入点は既存のどのエントリーよりも前(左)になります。戻り値は、list.insert() の第一引数として使うのに適しています。a はすでにソートされているものとします。
bisect.insort_left(a, x, lo=0, hi=len(a))|x を a にソート順で挿入します。これは、a がすでにソートされている場合、a.insert(bisect.bisect_left(a, x, lo, hi), x) と等価です。なお、O(log n) の探索に対して、遅い O(n) の挿入の段階が律速となります。
bisect.insort_right(a, x, lo=0, hi=len(a)), bisect.insort(a, x, lo=0, hi=len(a))|insort_left() と似ていますが、 a に含まれる x のうち、どのエントリーよりも後ろに x を挿入します。

## 参考

> bisect を利用して、直接の探索ができ、キー関数をサポートする、完全な機能を持つコレクションクラスを組み立てる SortedCollection recipe。キーは、探索中に不必要な呼び出しをさせないために、予め計算しておきます。

* [SortedCollection recipe](https://code.activestate.com/recipes/577197-sortedcollection/)

## 外部参考

コード例が一切ないのでググった。

* http://ja.pymotw.com/2/bisect/

```python
import bisect
import random
random.seed(1)
l = []
for i in range(1, 10):
    r = random.randint(1, 100)
    position = bisect.bisect(l, r)
    bisect.insort(l, r)
    print('%2d %2d' % (r, position), l)
```
```sh
$ python 0.py 
18  0 [18]
73  1 [18, 73]
98  2 [18, 73, 98]
 9  0 [9, 18, 73, 98]
33  2 [9, 18, 33, 73, 98]
16  1 [9, 16, 18, 33, 73, 98]
64  4 [9, 16, 18, 33, 64, 73, 98]
98  7 [9, 16, 18, 33, 64, 73, 98, 98]
58  4 [9, 16, 18, 33, 58, 64, 73, 98, 98]
```

自動的にソートしてくれる。

