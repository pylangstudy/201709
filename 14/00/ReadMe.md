# [8.5. heapq — ヒープキューアルゴリズム](https://docs.python.jp/3/library/heapq.html#module-heapq)

< [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/heapq.py](https://github.com/python/cpython/tree/3.6/Lib/heapq.py)

## 概要

> このモジュールではヒープキューアルゴリズムの一実装を提供しています。優先度キューアルゴリズムとしても知られています。

> ヒープとは、全ての親ノードの値が、その全ての子の値以下であるようなバイナリツリーです。この実装は、全ての k に対して、ゼロから要素を数えていった際に、heap[k] <= heap[2*k+1] かつ heap[k] <= heap[2*k+2] となる配列を使っています。比較のために、存在しない要素は無限大として扱われます。ヒープの興味深い性質は、最小の要素が常にルート、つまり heap[0] になることです。

> 以下の API は教科書におけるヒープアルゴリズムとは 2 つの側面で異なっています: (a) ゼロベースのインデクス化を行っています。これにより、ノードに対するインデクスとその子ノードのインデクスの関係がやや明瞭でなくなりますが、Python はゼロベースのインデクス化を使っているのでよりしっくりきます。(b) われわれの pop メソッドは最大の要素ではなく最小の要素 (教科書では “min heap:最小ヒープ” と呼ばれています; 教科書では並べ替えをインプレースで行うのに適した “max heap:最大ヒープ” が一般的です)。

> これらの 2 点によって、ユーザに戸惑いを与えることなく、ヒープを通常の Python リストとして見ることができます: heap[0] が最小の要素となり、heap.sort() はヒープ不変式を保ちます!

> ヒープを作成するには、 [] に初期化されたリストを使うか、 heapify() を用いて要素の入ったリストを変換します。

## 一覧

属性|説明
----|----
heapq.heappush(heap, item)|item を heap に push します。ヒープ不変式を保ちます。
heapq.heappop(heap)|pop を行い、 heap から最小の要素を返します。ヒープ不変式は保たれます。ヒープが空の場合、 IndexError が送出されます。pop せずに最小の要素にアクセスするには、 heap[0] を使ってください。
heapq.heappushpop(heap, item)|item を heap に push した後、pop を行って heap から最初の要素を返します。この一続きの動作を heappush() に引き続いて heappop() を別々に呼び出すよりも効率的に実行します。
heapq.heapify(x)|リスト x をインプレース処理し、線形時間でヒープに変換します。
heapq.heapreplace(heap, item)|heap から最小の要素を pop して返し、新たに item を push します。ヒープのサイズは変更されません。ヒープが空の場合、 IndexError が送出されます。

> このモジュールではさらに3つのヒープに基く汎用関数を提供します。

属性|説明
----|----
heapq.merge(*iterables, key=None, reverse=False)|複数のソートされた入力をマージ(merge)して一つのソートされた出力にします (たとえば、複数のログファイルの時刻の入ったエントリーをマージします)。ソートされた値にわたる iterator を返します。
heapq.nlargest(n, iterable, key=None)|iterable で定義されるデータセットのうち、最大値から降順に n 個の値のリストを返します。(あたえられた場合) key は、引数を一つとる、iterable のそれぞれの要素から比較キーを生成する関数を指定します: key=str.lower 以下のコードと同等です: sorted(iterable, key=key, reverse=True)[:n]
heapq.nsmallest(n, iterable, key=None)|iterable で定義されるデータセットのうち、最小値から昇順に n 個の値のリストを返します。(あたえられた場合) key は、引数を一つとる、iterable のそれぞれの要素から比較キーを生成する関数を指定します: key=str.lower 以下のコードと同等です: sorted(iterable, key=key)[:n]

> 後ろ二つの関数は n の値が小さな場合に最適な動作をします。大きな値の時には sorted() 関数の方が効率的です。さらに、 n==1 の時には min() および max() 関数の方が効率的です。この関数を繰り返し使うことが必要なら、iterable を実際のヒープに変えることを考えてください。

## [8.5.1. 基本的な例](https://docs.python.jp/3/library/heapq.html#basic-examples)

`heapq`は前回までと違い、`collections`パッケージ内ではない。例によってPython文書には一切の説明もコード例もなかった。

> すべての値をヒープに push してから最小値を 1 つずつ pop することで、ヒープソート を実装できます:

```python
import heapq

def heapsort(iterable):
    print(iterable)
    h = []
    for value in iterable: heapq.heappush(h, value)
    print(h)
    return [heapq.heappop(h) for i in range(len(h))]

heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
```
```sh
$ python 0.py 
[1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
[0, 1, 2, 6, 3, 5, 4, 7, 8, 9]
```

```python
import heapq
h = []
heapq.heappush(h, (5, 'write code'))
heapq.heappush(h, (7, 'release product'))
heapq.heappush(h, (1, 'write spec'))
heapq.heappush(h, (3, 'create tests'))
print(h)
print(heapq.heappop(h))
print(h)
```
```sh
$ python 1.py 
[(1, 'write spec'), (3, 'create tests'), (5, 'write code'), (7, 'release product')]
(1, 'write spec')
[(3, 'create tests'), (7, 'release product'), (5, 'write code')]
```

## [8.5.2. 優先度キュー実装の注釈](https://docs.python.jp/3/library/heapq.html#priority-queue-implementation-notes)

> 優先度つきキュー は、ヒープの一般的な使い方で、実装にはいくつか困難な点があります:

ようするにheapqは以下の機能がない。自前で工夫した上で実装せねばならない。

* ソート安定性: 優先度が等しい二つのタスクが、もともと追加された順序で返されるためにはどうしたらいいでしょうか？
* (priority, task) ペアに対するタプルの比較は、priority が同じで task がデフォルトの比較順を持たないときに破綻します。
* あるタスクの優先度が変化したら、どうやってそれをヒープの新しい位置に移動させるのでしょうか？
* 未解決のタスクが削除される必要があるとき、どのようにそれをキューから探して削除するのでしょうか？

> 最初の二つの困難の解決策は、項目を優先度、項目番号、そしてタスクを含む 3 要素のリストとして保存することです。この項目番号は、同じ優先度の二つのタスクが、追加された順序で返されるようにするための同点決勝戦として働きます。そして二つの項目番号が等しくなることはありませんので、タプルの比較が二つのタスクを直接比べようとすることはありえません。

> 残りの困難は主に、未解決のタスクを探して、その優先度を変更したり、完全に削除することです。タスクを探すことは、キュー内の項目を指し示す辞書によってなされます。

> 項目を削除したり、優先度を変更することは、ヒープ構造の不変関係を壊すことになるので、もっと難しいです。ですから、可能な解決策は、その項目が無効であるものとしてマークし、必要なら変更された優先度の項目を加えることです:

```python
import heapq
import itertools
pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')


print(pq)
add_task('task1', 0)
print(pq)
add_task('task2', 0)
print(pq)
add_task('task2', 1)
print(pq)
add_task('task2', 1)
print(pq)
pop_task()
print(pq)
pop_task()
print(pq)
```
```sh
$ python 2.py 
[]
[[0, 0, 'task1']]
[[0, 0, 'task1'], [0, 1, 'task2']]
[[0, 0, 'task1'], [0, 1, '<removed-task>'], [1, 2, 'task2']]
[[0, 0, 'task1'], [0, 1, '<removed-task>'], [1, 2, '<removed-task>'], [1, 3, 'task2']]
[[0, 1, '<removed-task>'], [1, 3, 'task2'], [1, 2, '<removed-task>']]
[]
```

## [8.5.3. 理論](https://docs.python.jp/3/library/heapq.html#theory)

> ヒープとは、全ての k について、要素を 0 から数えたときに、a[k] <= a[2*k+1] かつ a[k] <= a[2*k+2] となる配列です。比較のために、存在しない要素を無限大と考えます。ヒープの興味深い属性は a[0] が常に最小の要素になることです。

> 上記の奇妙な不変式は、勝ち抜き戦判定の際に効率的なメモリ表現を行うためのものです。以下の番号は a[k] ではなく k とします:

```
                               0

              1                                 2

      3               4                5               6

  7       8       9       10      11      12      13      14

15 16   17 18   19 20   21 22   23 24   25 26   27 28   29 30
```
二分木のことらしい。


上の木構造では、各セル k は 2*k+1 および 2*k+2 を最大値としています。スポーツに見られるような通常の 2 つ組勝ち抜き戦では、各セルはその下にある二つのセルに対する勝者となっていて、個々のセルの勝者を追跡していくことにより、そのセルに対する全ての相手を見ることができます。しかしながら、このような勝ち抜き戦を使う計算機アプリケーションの多くでは、勝歴を追跡する必要はりません。メモリ効率をより高めるために、勝者が上位に進級した際、下のレベルから持ってきて置き換えることにすると、あるセルとその下位にある二つのセルは異なる三つの要素を含み、かつ上位のセルは二つの下位のセルに対して “勝者と” なります。

このヒープ不変式が常に守られれば、インデクス 0 は明らかに最勝者となります。最勝者の要素を除去し、”次の” 勝者を見つけるための最も単純なアルゴリズム的手法は、ある敗者要素 (ここでは上図のセル 30 とします) を 0 の場所に持っていき、この新しい 0 を濾過するようにしてツリーを下らせて値を交換してゆきます。不変関係が再構築されるまでこれを続けます。この操作は明らかに、ツリー内の全ての要素数に対して対数的な計算量となります。全ての要素について繰り返すと、O(n log n) のソート(並べ替え)になります。

> このソートの良い点は、新たに挿入する要素が、最後に取り出された 0 番目の要素よりも “良い値” でない限り、ソートを行っている最中に新たな要素を効率的に追加できるというところです。この性質は、シミュレーション的な状況で、ツリーで全ての入力イベントを保持し、”勝者” の状況を最小のスケジュール時刻にするような場合に特に便利です。あるイベントが他のイベント群の実行をスケジュールする際、それらは未来にスケジュールされることになるので、それらのイベント群を容易にヒープに積むことができます。すなわち、ヒープはスケジューラを実装する上で良いデータ構造であるといえます (私はこれを MIDI シーケンサで使っています :-)。

MIDI シーケンサで使うのは、途中から再生するときに自動計算してくれるから？

> これまで、スケジューラを実装するための様々なデータ構造が広範に研究されてきました。ヒープは、十分高速で、速度はおおむね一定であり、最悪の場合でも平均的な速度とさほど変わらないため、良いデータ構造といえます。しかし、最悪の場合にひどい速度になるとしても、全体的にはより効率の高い他のデータ構造表現も存在します。

> ヒープはまた、巨大なディスクのソートでも非常に有用です。おそらくご存知のように、巨大なソートを行うと、複数の “ラン (run)” (予めソートされた配列で、そのサイズは通常 CPU メモリの量に関係しています) が生成され、続いて統合処理 (merging) がこれらのランを判定します。この統合処理はしばしば非常に巧妙に組織されています [1]。重要なのは、最初のソートが可能な限り長いランを生成することです。勝ち抜き戦はこれを達成するための良い方法です。もし利用可能な全てのメモリを使って勝ち抜き戦を行い、要素を置換および濾過処理して現在のランに収めれば、ランダムな入力に対してメモリの二倍のサイズのランを生成することになり、大体順序づけがなされている入力に対してはもっと高い効率になります。

> さらに、ディスク上の 0 番目の要素を出力して、現在の勝ち抜き戦に (最後に出力した値に “勝って” しまうために) 収められない入力を得たなら、ヒープには収まらないため、ヒープのサイズは減少します。解放されたメモリは二つ目のヒープを段階的に構築するために巧妙に再利用することができ、この二つ目のヒープは最初のヒープが崩壊していくのと同じ速度で成長します。最初のヒープが完全に消滅したら、ヒープを切り替えて新たなランを開始します。なんと巧妙で効率的なのでしょう！

> 一言で言うと、ヒープは知って得するメモリ構造です。私はいくつかのアプリケーションでヒープを使っていて、’ヒープ’ モジュールを常備するのはいい事だと考えています。:-)

算数が苦手な私には難しすぎた。知っても理解できない。アルゴリズムの基礎から勉強する必要がありそう。

### 脚注

> [1] 現在使われているディスクバランス化アルゴリズムは、最近ではもはや巧妙というよりも目障りになっています。これは、ディスクのシーク機能が向上した結果です。巨大な容量を持つテープドライブなど、シーク不能なデバイスでは、事情は全く異なります。テープの 1 つ 1 つの動きが可能な限り効率的に行われるように非常に巧妙な処理を (相当前もって) 確保しなければなりません (統合処理の “進行” に最も多く使用させます)。テープによっては逆方向に読むことさえでき、巻き戻しに時間を取られるのを避けるために使うこともできます。正直、本当に良いテープソートは見ていて素晴らしく驚異的なものです！ソートというのは常に偉大な芸術なのです！:-)

今回のPython文書は感情的な表現が多い。

## 参考

* http://d.hatena.ne.jp/dwarfjay/20140418/1397825281
* https://www.google.co.jp/url?sa=t&rct=j&q=&esrc=s&source=web&cd=4&ved=0ahUKEwjmnaTrl6PWAhWMoJQKHbBvBtIQFgg4MAM&url=http%3A%2F%2Flethe2211.hatenablog.com%2Fentry%2F2014%2F12%2F30%2F011030&usg=AFQjCNEmHY1jciBY3gMCAM5lEHVzcyjzyA

アルゴリズム、グラフ理論、探索、などがキーワードか。アルゴリズムの基礎を学習するのも面白そう。

