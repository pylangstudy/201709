# [8.3.3. deque オブジェクト](https://docs.python.jp/3/library/collections.html#deque-objects)

< [8.3. collections — コンテナデータ型](https://docs.python.jp/3/library/collections.html#module-collections) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/collections/__init__.py](https://github.com/python/cpython/tree/3.6/Lib/collections/__init__.py)

ChainMapは不要。dictのlistに過ぎない。

## 一覧

コンストラクタ|説明
--------------|----
class collections.deque([iterable[, maxlen]])|iterable で与えられるデータから、新しい deque オブジェクトを (append() をつかって) 左から右に初期化して返します。

インスタンスメソッド|説明
--------------------|----
append(x)|x を deque の右側につけ加えます。
appendleft(x)|x を deque の左側につけ加えます。
clear()|deque からすべての要素を削除し、長さを 0 にします。
copy()|deque の浅いコピーを作成します。バージョン 3.5 で追加.
count(x)|deque の x に等しい要素を数え上げます。バージョン 3.2 で追加.
extend(iterable)|イテラブルな引数 iterable から得られる要素を deque の右側に追加し拡張します。
extendleft(iterable)|イテラブルな引数 iterable から得られる要素を deque の左側に追加し拡張します。注意: 左から追加した結果は、イテラブルな引数の順序とは逆になります。
index(x[, start[, stop]])|deque 内の x の位置を返します (インデックス start からインデックス stop の両端を含む範囲で)。最初のマッチを返すか、見つからない場合には ValueError を発生させます。バージョン 3.5 で追加.
insert(i, x)|x を deque の位置 i に挿入します。バージョン 3.5 で追加.
pop()|deque の右側から要素をひとつ削除し、その要素を返します。要素がひとつも存在しない場合は IndexError を発生させます。
popleft()|deque の左側から要素をひとつ削除し、その要素を返します。要素がひとつも存在しない場合は IndexError を発生させます。
remove(value)|value の最初に現れるものを削除します。要素が見付からないない場合は ValueError を送出します。
reverse()|deque の要素をインプレースに反転し、None を返します。バージョン 3.2 で追加.
rotate(n)|deque の要素を全体で n 単位だけ右に循環させます。n が負の値の場合は左に循環させます。一単位右に循環させることは d.appendleft(d.pop()) と等価です。

属性(読取専用)|説明
--------------|----
maxlen|deque の最大長で、制限されていなければ None です。バージョン 3.1 で追加.

## その他の操作

> 上記に加え、deque はイテレーション、pickle、 len(d), reversed(d), copy.copy(d), copy.deepcopy(d), in 演算子による帰属検査、そして d[-1] などの添え字による参照をサポートしています。 両端への添字アクセスは O(1) ですが、中央部分へは O(n) と遅くなります。 高速なランダムアクセスが必要であればリストを使ってください。

> バージョン 3.5 から deque は __add__(), __mul__(), __imul__() をサポートしました。


