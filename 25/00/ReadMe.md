# [8.13.13.1. IntEnum](https://docs.python.jp/3/library/enum.html#intenum)

< [8.13. enum — 列挙型のサポート](https://docs.python.jp/3/library/enum.html#module-enum) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/enum.py](https://github.com/python/cpython/tree/3.6/Lib/enum.py)

## [8.13.13.1. IntEnum](https://docs.python.jp/3/library/enum.html#intenum)

> 提供されている 1 つ目の Enum の派生型であり、 int のサブクラスでもあります。 IntEnum のメンバーは整数と比較できます; さらに言うと、異なる整数列挙型どうしでも比較できます:

```python
from enum import IntEnum
class Shape(IntEnum):
    CIRCLE = 1
    SQUARE = 2
class Request(IntEnum):
    POST = 1
    GET = 2
print(Shape == 1)
print(Shape.CIRCLE == 1)
print(Shape.CIRCLE == Request.POST)

print(int(Shape.CIRCLE))
print(['a', 'b', 'c'][Shape.CIRCLE])
print([i for i in range(Shape.SQUARE)])
```
```sh
$ python 0.py 
False
True
True
1
b
[0, 1]
```

```python
from enum import Enum, IntEnum
class Shape(IntEnum):
    CIRCLE = 1
    SQUARE = 2
class Color(Enum):
    RED = 1
    GREEN = 2
print(Shape.CIRCLE == Color.RED)
```
```sh
$ python 1.py 
False
```

## [8.13.13.2. IntFlag](https://docs.python.jp/3/library/enum.html#intflag)

> 提供されている 2 つ目の Enum の派生型 IntFlag も int を基底クラスとしています。 IntFlag メンバーが Enum メンバーと異なるのは、ビット演算子 (&, |, ^, ~) を使って組み合わせられ、その結果も IntFlag メンバーになることです。 しかし、名前が示すように、 IntFlag は int のサブクラスでもあり、 int が使われるところでもどこでも使えます。 IntFlag メンバーに対してビット演算以外のどんな演算をしても、その結果は IntFlag メンバーではなくなります。

> バージョン 3.6 で追加.

致命的な問題を見つけた。

> フラグが設定されていない (値が0である) 場合、その真偽値としての評価は False になることです:

```python
from enum import IntFlag
class Perm(IntFlag):
    R   = 0b100
    W   = 0b010
    X   = 0b001
    RWX = 0b111
print(Perm.R | Perm.W)
print(Perm.R + Perm.W)
RW = Perm.R | Perm.W
print(Perm.R in RW)

print(Perm.RWX)
print(~Perm.RWX)

print(Perm.R & Perm.X)#定義に宣言がないと0になる！全パターン定義する必要がある…
print((Perm.R & Perm.X).value)
print(bool(Perm.R & Perm.X))#定義に宣言がないとFalseになる！全パターン定義する必要がある…

print(Perm.X | 8)
```

```sh
 $ python 3.py 
Perm.R|W
6
True
Perm.RWX
Perm.-8
Perm.0
0
False
Perm.8|X
```

## [8.13.13.3. Flag](https://docs.python.jp/3/library/enum.html#flag)

> 最後の派生型は Flag です。 IntFlag と同様に、 Flag メンバーもビット演算子 (&, |, ^, ~) を使って組み合わせられます。 しかし IntFlag とは違い、他のどの Flag 列挙型とも int とも組み合わせたり、比較したりできません。 値を直接指定することも可能ですが、値として auto を使い、 Flag に適切な値を選ばせることが推奨されています。

> バージョン 3.6 で追加.

> IntFlag と同様に、 Flag メンバーの組み合わせがどのフラグも設定されていない状態になった場合、その真偽値としての評価は False となります:


```python
from enum import Flag, auto
class Color(Flag):
    RED = auto()
    BLUE = auto()
    GREEN = auto()

print(Color.RED & Color.GREEN)
print(bool(Color.RED & Color.GREEN))
```
```sh
$ python 4.py 
Color.0
False
```

> 注釈

> ほとんどの新しいコードでは、 Enum と Flag が強く推奨されます。 というのは、 IntEnum と IntFlag は (整数と比較でき、従って推移的に他の無関係な列挙型と比較できてしまうことにより) 列挙型の意味論的な約束に反するからです。 IntEnum と IntFlag は、 Enum や Flag では上手くいかない場合のみに使うべきです; 例えば、整数定数を列挙型で置き換えるときや、他のシステムとの相互運用性を持たせたいときです。 

## [8.13.13.4. その他](https://docs.python.jp/3/library/enum.html#others)

> IntEnum は enum モジュールの一部ですが、単独での実装もとても簡単に行なえます:

```python
class IntEnum(int, Enum):
    pass
```

> ここでは似たような列挙型の派生を定義する方法を紹介します; 例えば、StrEnum は int ではなく str で複合させたものです。

> いくつかのルール:

>    Enum のサブクラスを作成するとき、複合させるデータ型は、基底クラスの並びで Enum 自身より先に記述しなければなりません (上記 IntEnum の例を参照)。

>    Enum のメンバーはどんなデータ型でも構いませんが、追加のデータ型 (例えば、上の例の int) と複合させてしまうと、すべてのメンバーの値はそのデータ型でなければならなくなります。 この制限は、メソッドの追加するだけの、 int や str のような他のデータ型を指定しない複合には適用されません。

>    他のデータ型と複合された場合、 value 属性は、たとえ等価であり等価であると比較が行えても、列挙型メンバー自身としては 同じではありません 。

>    %-方式の書式: %s および %r はそれぞれ Enum クラスの __str__() および __repr__() を呼び出します; その他のコード (IntEnum の %i や %h など) は列挙型のメンバーを複合されたデータ型として扱います。

>    フォーマット済み文字列リテラル 、 str.format() 、 format() では、複合されたデータ型の __format__() が使われます。 Enum クラスの str() や repr() を使って欲しいときは、フォーマットのコードで !s および !r を使ってください。

文章でなくコード例を出してくれ。定義する方法でなく、定義するときの注意点に見える。

## [8.13.14. 興味深い例](https://docs.python.jp/3/library/enum.html#interesting-examples)

> Enum, IntEnum, IntFlag, Flag は用途の大部分をカバーすると予想されますが、そのすべてをカバーできているわけではありません。 ここでは、そのまま、あるいは独自の列挙型を作る例として使える、様々なタイプの列挙型を紹介します。

### [8.13.14.1. 値の省略](8.13.14.1. 値の省略)

> 多くの用途では、列挙型の実際の値が何かは気にされません。 このタイプの単純な列挙型を定義する方法はいくつかあります:

>    値に auto インスタンスを使用する

>    値として object インスタンスを使用する

>    値として解説文字列を使用する

>    値としてタプルを使用し、独自の __new__() を使用してタプルを int 値で置き換える

これらのどの方法を使ってもユーザーに対して、値は重要ではなく、他のメンバーの番号の振り直しをする必要無しに、メンバーの追加、削除、並べ替えが行えるということを示せます。

どの方法を選んでも、(重要でない) 値を隠す repr() を提供すべきです:

```python
>>> class NoValue(Enum):
...     def __repr__(self):
...         return '<%s.%s>' % (self.__class__.__name__, self.name)
```

### [8.13.14.1.1. auto を使う](https://docs.python.jp/3/library/enum.html#using-auto)

```python
>>> class Color(NoValue):
...     RED = auto()
...     BLUE = auto()
...     GREEN = auto()
...
>>> Color.GREEN
<Color.GREEN>
```

### [8.13.14.1.2. object を使う](https://docs.python.jp/3/library/enum.html#using-object)

```python
>>> class Color(NoValue):
...     RED = object()
...     GREEN = object()
...     BLUE = object()
...
>>> Color.GREEN
<Color.GREEN>
```

### [8.13.14.1.3. 解説文字列を使う](https://docs.python.jp/3/library/enum.html#using-a-descriptive-string)

```python
>>> class Color(NoValue):
...     RED = 'stop'
...     GREEN = 'go'
...     BLUE = 'too fast!'
...
>>> Color.GREEN
<Color.GREEN>
>>> Color.GREEN.value
'go'
```

### [8.13.14.1.4. 独自の __new__() を使う](https://docs.python.jp/3/library/enum.html#using-a-custom-new)

```python
>>> class AutoNumber(NoValue):
...     def __new__(cls):
...         value = len(cls.__members__) + 1
...         obj = object.__new__(cls)
...         obj._value_ = value
...         return obj
...
>>> class Color(AutoNumber):
...     RED = ()
...     GREEN = ()
...     BLUE = ()
...
>>> Color.GREEN
<Color.GREEN>
>>> Color.GREEN.value
2
```

> 注釈

> __new__() メソッドが定義されていれば、Enum 番号の作成時に使用されます; これは Enum の __new__() と置き換えられ、クラスが作成された後の既存の番号を取得に使用されます。 

### [8.13.14.2. OrderedEnum](https://docs.python.jp/3/library/enum.html#orderedenum)

```python
from enum import Enum
class OrderedEnum(Enum):
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented
    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented
    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

class Grade(OrderedEnum):
    A = 5
    B = 4
    C = 3
    D = 2
    F = 1

print(Grade.C < Grade.A)
```
```sh
$ python 8.py 
True
```

### [8.13.14.3. DuplicateFreeEnum](https://docs.python.jp/3/library/enum.html#duplicatefreeenum)

```python
from enum import Enum
class DuplicateFreeEnum(Enum):
    def __init__(self, *args):
        cls = self.__class__
        if any(self.value == e.value for e in cls):
            a = self.name
            e = cls(self.value).name
            raise ValueError(
                "aliases not allowed in DuplicateFreeEnum:  %r --> %r"
                % (a, e))

class Color(DuplicateFreeEnum):
    RED = 1
    GREEN = 2
    BLUE = 3
    GRENE = 2
```

> 注釈

> これは Enum に別名を無効にするのと同様な振る舞いの追加や変更をおこなうためのサブクラス化に役立つ例です。単に別名を無効にしたいだけなら、 unique() デコレーターを使用して行えます。 

### [8.13.14.4. Planet](https://docs.python.jp/3/library/enum.html#planet)

```python
from enum import Enum
class Planet(Enum):
    MERCURY = (3.303e+23, 2.4397e6)
    VENUS   = (4.869e+24, 6.0518e6)
    EARTH   = (5.976e+24, 6.37814e6)
    MARS    = (6.421e+23, 3.3972e6)
    JUPITER = (1.9e+27,   7.1492e7)
    SATURN  = (5.688e+26, 6.0268e7)
    URANUS  = (8.686e+25, 2.5559e7)
    NEPTUNE = (1.024e+26, 2.4746e7)
    def __init__(self, mass, radius):
        self.mass = mass       # in kilograms
        self.radius = radius   # in meters
    @property
    def surface_gravity(self):
        # universal gravitational constant  (m3 kg-1 s-2)
        G = 6.67300E-11
        return G * self.mass / (self.radius * self.radius)
print(Planet.EARTH.value)
print(Planet.EARTH.surface_gravity)
```
```sh
$ python A.py 
(5.976e+24, 6378140.0)
9.802652743337129
```

### [8.13.15. Enum はどう違うのか?]()

> EnumMeta メタクラスは、__contains__()、__dir__()、__iter__() および標準的なクラスでは失敗するが Enum クラスでは動作するその他のメソッド (list(Color) や some_var in Color など) を責任を持って提供します。EnumMeta は最終的な Enum クラスのさまざまなメソッド (__new__()、__getnewargs__()、__str__() および __repr__()) が正しいことを責任を持って保証します。

### [8.13.15.2. Enum メンバー (インスタンス)](https://docs.python.jp/3/library/enum.html#enum-members-aka-instances)

> Enum メンバーについて最も興味深いのは、それらがシングルトンであるということです。EnumMeta は Enum 自身を作成し、メンバーを作成し、新しいインスタンスが作成されていないかどうかを確認するために既存のメンバーインスタンスだけを返すカスタム __new__() を追加します。

### [8.13.15.3. 細かい点](https://docs.python.jp/3/library/enum.html#finer-points)

#### [8.13.15.3.1. __dunder__ 名のサポート](https://docs.python.jp/3/library/enum.html#supported-dunder-names)

> __members__ は member_name:member を要素とする OrderedDict です。 これはクラスでのみ利用可能です。

> __new__() が、もし指定されていた場合、列挙型のメンバーを作成し、返します; そのメンバー の _value_ を適切に設定するのも非常によい考えです。 いったん全てのメンバーが作成されると、それ以降 __new__() は使われません。

#### [8.13.15.3.2. _sunder_ 名のサポート](https://docs.python.jp/3/library/enum.html#supported-sunder-names)



>    _name_ – メンバー名

>    _value_ – メンバーの値; __new__ で設定したり、変更したりできます

>    _missing_ – 値が見付からなかったときに使われる検索関数; オーバーライドされていることがあります

>    _order_ – used in Python 2/3 code to ensure member order is consistent (class attribute, removed during class creation)

>    _generate_next_value_ – used by the Functional API and by auto to get an appropriate value for an enum member; may be overridden

バージョン 3.6 で追加: _missing_, _order_, _generate_next_value_

To help keep Python 2 / Python 3 code in sync an _order_ attribute can be provided. It will be checked against the actual order of the enumeration and raise an error if the two do not match:

```python
from enum import Enum
class Color(Enum):
    _order_ = 'RED GREEN BLUE'
    RED = 1
    BLUE = 3
    GREEN = 2
```
```sh
$ python B.py 
...
TypeError: member order does not match _order_
```

> 注釈

> In Python 2 code the _order_ attribute is necessary as definition order is lost before it can be recorded. 

#### [8.13.15.3.3. Enum メンバー型](https://docs.python.jp/3/library/enum.html#enum-member-type)

> Enum メンバーは、それらの Enum クラスのインスタンスで、通常は EnumClass.member のようにアクセスします。 ある状況下では、 EnumClass.member.member としてもアクセスできますが、この方法は絶対に使うべきではありません。 というのは、この検索は失敗するか、さらに悪い場合には、探している Enum メンバー以外のものを返す場合もあるからです (これがメンバーの名前に大文字のみを使うのが良い理由の 1 つでもあります):

```python
from enum import Enum
class FieldTypes(Enum):
    name = 0
    value = 1
    size = 2
print(FieldTypes.value.size)
print(FieldTypes.size.value)
```
```sh
$ python C.py 
FieldTypes.size
2
```

これはひどい。まずメンバ変数から別のメンバを参照できることが初耳。そして「絶対に使うべきではありません」と言っているにも関わらず、そんな方法が実際にできてしまう。

メンバ変数を作成すると、そのメンバ変数には`value`,`name`などの属性が付与される。それらと名前が同一の場合、ユーザが作成した側が無視されるらしい。つまり`value`というメンバを作っても無視され、Enumが自動作成した`value`属性が優先される。

Pythonで頻発する名前重複問題はEnumにもあった。

#### [8.13.15.3.4. Enum クラスとメンバーの真偽値](https://docs.python.jp/3/library/enum.html#boolean-value-of-enum-classes-and-members)

> (int, str などのような) 非 Enum 型と複合させた Enum のメンバーは、その複合された型の規則に従って評価されます; そうでない場合は、全てのメンバーは True と評価されます。 メンバーの値に依存する独自の Enum の真偽値評価を行うには、クラスに次のコードを追加してください:

```
def __bool__(self):
    return bool(self.value)
```

> Enum クラスは常に True と評価されます。

#### [8.13.15.3.5. メソッド付きの Enum クラス](https://docs.python.jp/3/library/enum.html#enum-classes-with-methods)

> Enum サブクラスに追加のメソッドを与えた場合、上述の Planet クラスのように、そのメソッドはメンバーの dir() に表示されますが、クラスの dir() には表示されません:

```python
>>> dir(Planet)
['EARTH', 'JUPITER', 'MARS', 'MERCURY', 'NEPTUNE', 'SATURN', 'URANUS', 'VENUS', '__class__', '__doc__', '__members__', '__module__']
>>> dir(Planet.EARTH)
['__class__', '__doc__', '__module__', 'name', 'surface_gravity', 'value']
```

#### [8.13.15.3.6. Flag のメンバーの組み合わせ](8.13.15.3.6. Flag のメンバーの組み合わせ)

> Flag メンバーの組み合わせに名前が無い場合、 repr() の出力には、その値にある全ての名前を持つフラグと全ての名前を持つ組み合わせが含まれます:

```python
>>> class Color(Flag):
...     RED = auto()
...     GREEN = auto()
...     BLUE = auto()
...     MAGENTA = RED | BLUE
...     YELLOW = RED | GREEN
...     CYAN = GREEN | BLUE
...
>>> Color(3)  # named combination
<Color.YELLOW: 3>
>>> Color(7)      # not named combination
<Color.CYAN|MAGENTA|BLUE|YELLOW|GREEN|RED: 7>
```

```python
from enum import Flag, auto
class Color(Flag):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    MAGENTA = RED | BLUE
    YELLOW = RED | GREEN
    CYAN = GREEN | BLUE

print(Color.RED.value)#1
print(Color.GREEN.value)#2
print(Color.BLUE.value)#4
print(Color.MAGENTA.value)#5
print(Color.YELLOW.value)#3
print(Color.CYAN.value)#6

print(Color(3))
print(Color(7))
print(Color(7).value)
print((Color.CYAN|Color.MAGENTA|Color.BLUE|Color.YELLOW|Color.GREEN|Color.RED).value)#7(0b111)
print((Color.BLUE|Color.GREEN|Color.RED).value)#7(0b111)
print(Color(8).value)#ValueError: 8 is not a valid Color
```
```sh
$ python D.py 
1
2
4
5
3
6
Color.YELLOW
Color.CYAN|MAGENTA|BLUE|YELLOW|GREEN|RED
7
7
7
...
ValueError: 8 is not a valid Color
```

# Enumの欠点まとめ

* Enum, Flag, IntEnum, IntFlagを使い分けねばならない（わかりづらい）
    * Enum
        * 値の型は任意
        * 同値比較(`==`,`is`)のみ可（比較演算(`<,>`等)、ビット演算(`&,|,^,~`)、不可）
            * 同Enum型とのみ比較可（他の型とは不可）
    * Flag
        * 値は`auto()`推奨（int型）
        * 同Flag型とのみ比較可（他の型とは不可）
        * ビット演算子(`&,|,^,~`)が使える
    * IntFlag, IntEnum
        * int型とも比較可
        * Enum,Flag を強く推奨（IntFlag, IntEnumは非推奨）
            * 整数と比較でき、従って推移的に他の無関係な列挙型と比較できてしまうことにより) 列挙型の意味論的な約束に反するから
* サブクラス化はメンバが一つも定義されていない場合のみ可
    * 部分定義しておいて個別に派生させることができない（クラスの特性すら失っている）
* Enumはメンバ変数から別のメンバ変数が参照できてしまう（以下の理由で非推奨）
    * Enum既存メンバと名前重複すると期待通りに動かない（予約語が優先されユーザ定義は無視される）
        * `_xxx_`のように前後アンダーバーは予約語なので使わないこと
        * `value`, `name`はEnumの予約語なので使わないこと
* たまたま値が同値なだけで別名の別物として扱う手段がない
    * `@unique`としないと別名定義とされてしまう
    * `@unique`とすると別名定義でエラーになる
* 値が自動付与されない（C#, C/C++言語なら自動でインクリメント値付与）
    * `import enum`, `enum.auto()`と表記する必要がある（冗長）
        * それ以外で値を設定するには、1つずつ手入力 or `__new__`で生成する or `Enum('', {})`で生成する（手間）

