# [8.13. enum — 列挙型のサポート](https://docs.python.jp/3/library/enum.html#module-enum)

< [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/enum.py](https://github.com/python/cpython/tree/3.6/Lib/enum.py)

## [8.13.1. モジュールコンテンツ](https://docs.python.jp/3/library/enum.html#module-contents)

属性|説明
----|----
class enum.Enum|列挙型定数を作成する基底クラスです。もうひとつの構築構文については 機能 API を参照してください。
class enum.IntEnum|int のサブクラスでもある列挙型定数を作成する基底クラスです。
class enum.IntFlag|列挙型定数を作成する基底クラスで、ビット演算子を使って組み合わせられ、その結果も IntFlag メンバーになります。 IntFlag は int のサブクラスでもあります。
class enum.Flag|列挙型定数を作成する基底クラスで、ビット演算を使って組み合わせられ、その結果も IntFlag メンバーになります。
enum.unique()|一つの名前だけがひとつの値に束縛されていることを保証する Enum クラスのデコレーターです。
class enum.auto|このインスタンスは列挙型のメンバーのための適切な値に置き換えられます。

> バージョン 3.6 で追加: Flag, IntFlag, auto

## [8.13.2. Enum の作成](https://docs.python.jp/3/library/enum.html#creating-an-enum)

```python
from enum import Enum
class Color(Enum):
    RED = 100
    GREEN = 200
    BLUE = 300

print(Color.RED)
print(repr(Color.RED))
print(type(Color.RED))
print(isinstance(Color.GREEN, Color))
print(Color.RED.name)
print(Color.RED.value)

for c in Color: print(c)

apples = {}
apples[Color.RED] = 'red delicious'
apples[Color.GREEN] = 'granny smith'
apples == {Color.RED: 'red delicious', Color.GREEN: 'granny smith'}
print(apples
```
```sh
$ python 0.py 
Color.RED
<Color.RED: 100>
<enum 'Color'>
True
RED
100
Color.RED
Color.GREEN
Color.BLUE
{<Color.RED: 100>: 'red delicious', <Color.GREEN: 200>: 'granny smith'}
```

## [8.13.3. 列挙型メンバーおよびそれらの属性へのプログラム的アクセス](https://docs.python.jp/3/library/enum.html#programmatic-access-to-enumeration-members-and-their-attributes)

```python
from enum import Enum
class Color(Enum):
    RED = 100
    GREEN = 200
    BLUE = 300

print(Color(100))
print(Color(200))
print(Color(300))
print(Color['RED'])
print(Color['GREEN'])
print(Color['BLUE'])
print(Color.RED.name)
print(Color.RED.value)
```
```sh
$ python 1.py 
Color.RED
Color.GREEN
Color.BLUE
Color.RED
Color.GREEN
Color.BLUE
RED
100
```

## [8.13.4. 列挙型メンバーと値の重複](https://docs.python.jp/3/library/enum.html#duplicating-enum-members-and-values)

```python
from enum import Enum
class Shape(Enum):
    SQUARE = 2
    SQUARE = 3
```
```sh
$ python 2.py 
TypeError: Attempted to reuse key: 'SQUARE'
```

```python
from enum import Enum
class Shape(Enum):
    SQUARE = 2
    DIAMOND = 1
    CIRCLE = 3
    ALIAS_FOR_SQUARE = 2

print(Shape.SQUARE)
print(Shape.ALIAS_FOR_SQUARE)
print(Shape(2))
```
```sh
$ python 3.py 
Shape.SQUARE
Shape.SQUARE
Shape.SQUARE
```

## [8.13.5. 番号付けの値が同一であることの確認](https://docs.python.jp/3/library/enum.html#ensuring-unique-enumeration-values)

> デフォルトでは、前述のように複数の名前への同じ値の定義は別名とすることで許されています。この挙動を望まない場合、以下のデコレーターを使用することで各値が列挙型内で一意かどうか確認できます:

> @enum.unique

> 列挙型専用の class デコレーターです。列挙型の __members__ に別名がないかどうか検索します; 見つかった場合、ValueError が詳細情報とともに送出されます:

```python
from enum import Enum, unique
@unique
class Mistake(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 3
```
```sh
$ python 4.py 
...
ValueError: duplicate values found in <enum 'Mistake'>: FOUR -> THREE
```

## [8.13.6. 値の自動設定を使う](https://docs.python.jp/3/library/enum.html#using-automatic-values)

> 正確な値が重要でない場合、 auto が使えます:

```python
from enum import Enum, auto
class Color(Enum):
    RED = auto()
    BLUE = auto()
    GREEN = auto()
print(list(Color))
```
```sh
 $ python 5.py 
[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
```

```python
from enum import Enum, auto
class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name
class Ordinal(AutoName):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()
print(list(Ordinal))
```
```sh
$ python 6.py 
[<Ordinal.NORTH: 'NORTH'>, <Ordinal.SOUTH: 'SOUTH'>, <Ordinal.EAST: 'EAST'>, <Ordinal.WEST: 'WEST'>]
```

C#なら`enum Color {RED, BLUE, GREEN};`, C/C++言語なら`enum EColor {RED, BLUE, GREEN} Color;`のように、それぞれ`auto()`がなくとも自動的に0から割り振られる。また、代入されたら、以降はその値をインクリメント(+1)した値になる。Pythonではこれらができない。

Python文書の[チュートリアル](https://docs.python.jp/3/tutorial/appetite.html)ではC言語より優れている(短く書ける)と謳われていたが、enum宣言に関してはC言語より不自由かつ冗長である。

## [8.13.7. イテレーション](https://docs.python.jp/3/library/enum.html#iteration)

> 列挙型のメンバーのイテレートは別名をサポートしていません:

```python
from enum import Enum
class Shape(Enum):
    SQUARE = 2
    DIAMOND = 1
    CIRCLE = 3
    ALIAS_FOR_SQUARE = 2
print(list(Shape))

for name, member in Shape.__members__.items():
    print(name, member)

print([name for name, member in Shape.__members__.items() if member.name != name])
```
```sh
$ python 7.py 
[<Shape.SQUARE: 2>, <Shape.DIAMOND: 1>, <Shape.CIRCLE: 3>]
SQUARE Shape.SQUARE
DIAMOND Shape.DIAMOND
CIRCLE Shape.CIRCLE
ALIAS_FOR_SQUARE Shape.SQUARE
['ALIAS_FOR_SQUARE']
```

## [8.13.8. 比較](https://docs.python.jp/3/library/enum.html#comparisons)

> 列挙型メンバーは同一性を比較できます:

```python
from enum import Enum
class Color(Enum):
    RED = 100
    GREEN = 200
    BLUE = 300

print(Color.RED is Color.RED)
print(Color.RED is Color.BLUE)
print(Color.RED is not Color.BLUE)
print(Color.RED == Color.RED)
print(Color.RED == Color.BLUE)
print(Color.RED != Color.BLUE)
#print(Color.RED < Color.BLUE)#TypeError: '<' not supported between instances of 'Color' and 'Color'
print(Color.RED == 100)#非列挙型の値との比較は常に不等となります(それを望むならIntEnumを使う)
print(Color.RED.value == 100)
```
```sh
$ python 8.py 
True
False
True
True
False
True
False
True
```

## [8.13.9. 列挙型で許されるメンバーと属性](https://docs.python.jp/3/library/enum.html#allowed-members-and-attributes-of-enumerations)

> 上述の例では列挙型の値に整数を使用しています。整数の使用は短くて使いやすい (そして 機能 API でデフォルトで提供されています) のですが、厳密には強制ではありません。ほとんどの事例では列挙型の実際の値が何かを気にしていません。しかし、値が重要で ある 場合、列挙型は任意の値を持つことができます。

> 列挙型は Python のクラスであり、通常どおりメソッドや特殊メソッドを持つことができます:

```python
from enum import Enum
class Mood(Enum):
    FUNKY = 1
    HAPPY = 3
    def describe(self):
        # self is the member here
        return self.name, self.value
    def __str__(self):
        return 'my custom str! {0}'.format(self.value)
    @classmethod
    def favorite_mood(cls):
        # cls here is the enumeration
        return cls.HAPPY

print(Mood.favorite_mood())
#print(Mood.describe())#TypeError: describe() missing 1 required positional argument: 'self'd())
#print(Mood().describe())#TypeError: __call__() missing 1 required positional argument: 'value'
#print(Mood())#TypeError: __call__() missing 1 required positional argument: 'value'
print(str(Mood.FUNKY))
```

> 上記の結果が以下のようになります:

```sh
>>> Mood.favorite_mood()
<Mood.HAPPY: 3>
>>> Mood.HAPPY.describe()
('HAPPY', 3)
>>> str(Mood.FUNKY)
'my custom str! 1'
```

なりません。少なくとも私の環境では`Mood.HAPPY.describe()`がエラーになりました。

```sh
TypeError: describe() missing 1 required positional argument: 'self'
```

コメントアウトし、他の結果を出すと以下。

```sh
$ python 9.py 
my custom str! 3
my custom str! 1
```

> 何が許されているかのルールは次のとおりです。先頭と末尾が 1 個のアンダースコアの名前は列挙型により予約されているため、使用できません。列挙型内で定義されたその他すべての名前は、その列挙型のメンバーとして使用できます。特殊メソッド (__str__(), __add__(), など) と、メソッドを含むデスクリプタ (記述子) は例外です。

使える名前に制限があるらしい。Python文書にコード例がないため、試してみた。

```python
from enum import Enum
class Mood(Enum):
    _NOT_USE_ = 1

print(Mood._NOT_USE_)
```
```sh
$ python A.py 
ValueError: _names_ are reserved for future Enum use
```

> 注意: 列挙型で __new__() および/または __init__() を定義した場合、列挙型メンバーに与えられた値はすべてこれらのメソッドに渡されます。例 Planet を参照してください。

* [Planet](https://docs.python.jp/3/library/enum.html#planet)

## [8.13.10. 列挙型のサブクラス化の制限事項](https://docs.python.jp/3/library/enum.html#restricted-subclassing-of-enumerations)

> 列挙型のサブクラスの作成はその列挙型にメンバーが一つも定義されていない場合のみ行なえます。従って以下は許されません:

```python
from enum import Enum
class Color(Enum):
    RED = 100
    GREEN = 200
    BLUE = 300
class MoreColor(Color):
    PINK = 17
```
```sh
$ python B.py 
TypeError: Cannot extend enumerations
```

これはひどい。拡張(マージ)できない…。

メソッドの場合は問題ないが、enumの本質ではないため無価値。

```python
from enum import Enum
class Foo(Enum):
    def some_behavior(self):
        pass
class Bar(Foo):
    HAPPY = 1
    SAD = 2
```
```sh
$ python C.py 
```

> メンバーが定義された列挙型のサブクラス化を許可すると、いくつかのデータ型およびインスタンスの重要な不変条件の違反を引き起こします。とはいえ、それが許可されると、列挙型のグループ間での共通の挙動を共有するという利点もあります。 (OrderedEnum の例を参照してください。)

* [OrderedEnum](https://docs.python.jp/3/library/enum.html#orderedenum)

[OrderedEnum](https://docs.python.jp/3/library/enum.html#orderedenum)という型ならサブクラス化できるという意味なのか？

と、勘違いしてしまう。しかし全く違う。Pythonの列挙型はすべて、値定義された型からはサブクラス化できない。

あくまでEnumならIntEnumではできない「不変条件の違反を許可することが可能」という話。

* [OrderedEnum](https://docs.python.jp/3/library/enum.html#orderedenum)という型はない
    * リンク先を見ればわかるが`Enum`を継承した独自クラスに過ぎない
        * リンク先のコードでもやはり定数宣言はしていない（したら継承できない）
* これまでIntEnumのことについてはほとんど触れられていない
    * 「不変条件の違反」とは何か説明がない
        * この話と「変数宣言クラスからのサブクラス化不能」の制限に何の関係があるか不明
        * 文脈から察するにクラスごとに以下の違いがあるのだろう
            * IntEnumでは「不変条件の違反を許可」できない
            * Enumでは「不変条件の違反を許可」できる

この文書の書き方は、あたかも可能であるかのように期待させておいて、全く別の話にすり替えているだけ。欺瞞に満ちた文書にみえる。順番に文書をみていると、まだIntEnumについてコード例がひとつも出ていない。どんな関係なのか何も判断できない。

## [8.13.11. Pickle 化](https://docs.python.jp/3/library/enum.html#pickling)

> 列挙型は pickle 化と unpickle 化が行えます:

Pythonでいうpickle化、unpickle化は、C#など他の言語でいう、Serialize, Deserialize, と同義。つまりオブジェクトをファイル保存し永続化すること、それを再びオブジェクトに戻すことを言う。

```python
from enum import Enum
class Color(Enum):
    RED = 100
    GREEN = 200
    BLUE = 300

from pickle import dumps, loads
print(Color.RED is loads(dumps(Color.RED)))
```
```sh
$ python E.py 
True
```

> 通常の pickle 化の制限事項が適用されます: pickle 可能な列挙型はモジュールのトップレベルで定義されていなくてはならず、unpickle 化はモジュールからインポート可能でなければなりません。

> 注釈 pickle プロトコルバージョン 4 では他のクラスで入れ子になった列挙型の pickle 化も容易です。 

> Enum メンバーをどう pickle 化/unpickle 化するかは、列挙型クラス内の __reduce_ex__() で定義することで変更できます。

制限と注釈が相反するせいで、結局Python3.6.1ではどうなっているのか不明。pickleプロトコルとやらが唐突に出てきて何者なのか不明。Python3.6.1ではそれのバージョンばいくつなのか不明。

とりあえず以下のように、module.class.enumの階層にして試したが問題なくpickle化できたようにみえる。
```python
from enum import Enum
class UserClass:
    class Color(Enum):
        RED = 100
        GREEN = 200
        BLUE = 300

from pickle import dumps, loads
print(UserClass.Color.RED is loads(dumps(UserClass.Color.RED)))
```
```sh
$ python F.py 
True
```

コード例もないため、こういうことを言っているのではないのかもしれないが。

## [8.13.12. 機能 API](https://docs.python.jp/3/library/enum.html#functional-api)

> Enum クラスは呼び出し可能で、以下の機能 API を提供しています:

```python
from enum import Enum
Animal = Enum('Animal', 'ANT BEE CAT DOG')
print(Animal)
print(Animal.ANT)
print(Animal.ANT.value)
print(list(Animal))
```
```sh
$ python G.py 
<enum 'Animal'>
Animal.ANT
1
[<Animal.ANT: 1>, <Animal.BEE: 2>, <Animal.CAT: 3>, <Animal.DOG: 4>]
```

> この API の動作は namedtuple と似ています。Enum 呼び出しの第 1 引数は列挙型の名前です。

> 第 2 引数は列挙型メンバー名の ソース です。空白で区切った名前の文字列、名前のシーケンス、キー/値のペアの 2 要素タプルのシーケンス、あるいは名前と値のマッピング (例: 辞書) を指定できます。最後の 2 個のオプションでは、列挙型へ任意の値を割り当てることができます。前の 2 つのオプションでは、1 から始まり増加していく整数を自動的に割り当てます (別の開始値を指定するには、start 引数を使用します)。Enum から派生した新しいクラスが返されます。言い換えれば、上記の Animal への割り当ては以下と等価です:

この文章は混乱する。以下3点の異なる話をしている。

* `Enum(...)`はEnum派生クラスを返す
* 第2引数はさまざまな型を受け付ける
* 第2引数とは別の引数として`start`がある

最初にメソッドの定義を書かない上、異なる話をごちゃまぜにしているせいで混乱する。

### デフォルト開始値が0でなく1の理由

> デフォルトの開始番号が 0 ではなく 1 である理由は、0 がブール演算子では False になりますが、すべての列挙型メンバーの評価は True でなければならないためです。

なぜTrueでなければならないのか謎。そうであるなら、「enumメンバ値には`0`, `False`を設定できない」という新たな制限があるということになる。

### pickle化

> 機能 API による Enum の pickle 化は、その列挙型がどのモジュールで作成されたかを見つけ出すためにフレームスタックの実装の詳細が使われるので、トリッキーになることがあります (例えば別のモジュールのユーティリティ関数を使うと失敗しますし、IronPython や Jython ではうまくいきません)。解決策は、以下のようにモジュール名を明示的に指定することです:

```python
Animal = Enum('Animal', 'ANT BEE CAT DOG', module=__name__)
```

> 警告  module が与えられない場合、Enum はそれがなにか決定できないため、新しい Enum メンバーは unpickle 化できなくなります; エラーをソースの近いところで発生させるため、pickle 化は無効になります。 

> 新しい pickle プロトコルバージョン 4 では、一部の状況において、pickle がクラスを発見するための場所の設定に __qualname__ を参照します。例えば、そのクラスがグローバルスコープ内のクラス SomeData 内で利用可能とするには以下のように指定します:

```python
Animal = Enum('Animal', 'ANT BEE CAT DOG', qualname='SomeData.Animal')
```

### 構文

> 完全な構文は以下のようになります:

```
Enum(value='NewEnumName', names=<...>, *, module='...', qualname='...', type=<mixed-in class>, start=1)
```

引数|説明
----|----
value|新しい Enum クラスに記録されるそれ自身の名前です。
names|Enum のメンバーです。 空白またはカンマで区切った文字列でも構いません (特に指定がない限り、値は 1 から始まります):`'RED GREEN BLUE' | 'RED,GREEN,BLUE' | 'RED, GREEN, BLUE'`または名前のイテレータで指定もできます:`['RED', 'GREEN', 'BLUE']`または (名前, 値) のペアのイテレータでも指定できます:`[('CYAN', 4), ('MAGENTA', 5), ('YELLOW', 6)]`またはマッピングでも指定できます:`{'CHARTREUSE': 7, 'SEA_GREEN': 11, 'ROSEMARY': 42}`
module|新しい Enum クラスが属するモジュールの名前です。
qualname|新しい Enum クラスが属するモジュールの場所です。
type|新しい Enum クラスに複合されるデータ型です。
start|names のみが渡されたときにカウントを開始する数です。

> バージョン 3.5 で変更: start 引数が追加されました。

typeがよくわからない。「複合される」とは一体どういうことか？module, qualnameはpickle化に関する部分なのだろう。

```python
from enum import Enum
class UserClass: pass
Animal = Enum(value='Animal', names='ANT BEE CAT DOG', module=__name__, qualname=UserClass.__qualname__+'.Animal', start=100)
print(Animal)
print(Animal.ANT)
print(Animal.ANT.value)
print(list(Animal))
print()

Animal2 = Enum(value='Animal', names='ANT BEE CAT DOG', type=UserClass)
print(Animal2)
print(Animal2.ANT)
print(Animal2.ANT.value)
print(list(Animal2))
```
```sh
$ python H.py 
<enum 'Animal'>
Animal.ANT
100
[<Animal.ANT: 100>, <Animal.BEE: 101>, <Animal.CAT: 102>, <Animal.DOG: 103>]

<enum 'Animal'>
Animal.ANT
1
[<Animal.ANT: 1>, <Animal.BEE: 2>, <Animal.CAT: 3>, <Animal.DOG: 4>]
```

