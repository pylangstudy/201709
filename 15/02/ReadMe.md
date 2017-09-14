# [8.6.2. その他の使用例](https://docs.python.jp/3/library/bisect.html#other-examples)

< [8.6. bisect — 配列二分法アルゴリズム](https://docs.python.jp/3/library/bisect.html) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/bisect.py](https://github.com/python/cpython/tree/3.6/Lib/bisect.py)

## 検索

bisect() 関数は数値テーブルの探索に役に立ちます。この例では、 bisect() を使って、(たとえば)順序のついた数値の区切り点の集合に基づいて、試験の成績の等級を表す文字を調べます。区切り点は 90 以上は ‘A’、 80 から 89 は ‘B’、などです:

```python
import bisect
breakpoints = [60, 70, 80, 90]
grades = 'FDCBA'
scores = [33, 99, 77, 70, 89, 90, 100]
def grade(score, breakpoints=breakpoints, grades=grades):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

print('breakpoints:', breakpoints)
print('grades:', grades)
print('scores:', scores)
print([grade(score) for score in scores])
```
```sh
$ python 0.py 
breakpoints: [60, 70, 80, 90]
grades: FDCBA
scores: [33, 99, 77, 70, 89, 90, 100]
['F', 'A', 'C', 'C', 'B', 'A', 'A']
```

## インデックス取得

> sorted() 関数と違い、 bisect() 関数に key や reversed 引数を用意するのは、設計が非効率になるので、非合理的です (連続する bisect 関数の呼び出しは前回の key 参照の結果を “記憶” しません)。

> 代わりに、事前に計算しておいたキーのリストから検索して、レコードのインデックスを見つけます:

```python
import bisect
data = [('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
data.sort(key=lambda r: r[1])
keys = [r[1] for r in data]         # precomputed list of keys
print(data[bisect.bisect_left(keys, 0)])
print(data[bisect.bisect_left(keys, 1)])
print(data[bisect.bisect_left(keys, 5)])
print(data[bisect.bisect_left(keys, 8)])
```
```sh
$ python 1.py 
('black', 0)
('blue', 1)
('red', 5)
('yellow', 8)
```
