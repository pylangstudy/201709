# [9.1. numbers — 数の抽象基底クラス](https://docs.python.jp/3/library/numbers.html)

< [9. 数値と数学モジュール](https://docs.python.jp/3/library/numeric.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/numbers.py](https://github.com/python/cpython/tree/3.6/Lib/numbers.py)

> numbers モジュール (PEP 3141) は数の 抽象基底クラス の階層を定義します。この階層では、さらに多くの演算が順番に定義されます。このモジュールで定義される型はどれもインスタンス化できません。

> class numbers.Number

>    数の階層の根。引数 x が、種類は何であれ、数であるということだけチェックしたい場合、isinstance(x, Number) が使えます。

数学がわからない。どうやって使えばいいのか…。

意味|クラス
----|------
整数|class numbers.Integral
分数(有理数)|class numbers.Rational
虚数(複素数)|class numbers.Complex

## [9.1.1. 数値塔](https://docs.python.jp/3/library/numbers.html#the-numeric-tower)

### class numbers.Complex

属性|説明
----|----
class numbers.Complex|この型のサブクラスは複素数を表し、組み込みの complex 型を受け付ける演算を含みます。それらは: complex および bool への変換、 real, imag, +, -, *, /, abs(), conjugate(), ==, != です。 - と != 以外の全てのものは抽象メソッドや抽象プロパティです。
real|抽象プロパティ。この数の実部を取り出します。
imag|抽象プロパティ。この数の虚部を取り出します。

### class numbers.Rational

属性|説明
----|----
class numbers.Rational|Real をサブタイプ化し numerator と denominator のプロパティを加えたものです。これらは既約分数のものでなければなりません。この他に float() のデフォルトも提供します。
numerator|抽象プロパティ。
denominator|抽象プロパティ。

### ほか

属性|説明
----|----
abstractmethod conjugate()|抽象プロパティ。複素共役を返します。たとえば、(1+3j).conjugate() == (1-3j) です。
class numbers.Real|Real は、Complex 上に、 実数に対して行える演算を加えます。簡潔に言うとそれらは: float への変換, math.trunc(), round(), math.floor(), math.ceil(), divmod(), //, %, <, <=, > および >= です。Real はまた complex(), real, imag および conjugate() のデフォルトを提供します。
class numbers.Integral|Rational をサブタイプ化し int への変換が加わります。 float(), numerator, denominator のデフォルトを提供します。 ** に対する抽象メソッドと、ビット列演算 <<, >>, &, ^, |, ~ を追加します。

## [9.1.2. 型実装者のための注意事項](https://docs.python.jp/3/library/numbers.html#notes-for-type-implementors)

> 実装する人は等しい数が等しく扱われるように同じハッシュを与えるように気を付けねばなりません。これは二つの異なった実数の拡張があるような場合にはややこしいことになるかもしれません。たとえば、 fractions.Fraction は hash() を以下のように実装しています:

```python
def __hash__(self):
    if self.denominator == 1:
        # Get integers right.
        return hash(self.numerator)
    # Expensive check, but definitely correct.
    if self == float(self):
        return hash(float(self))
    else:
        # Use tuple's hash to avoid a high collision rate on
        # simple fractions.
        return hash((self.numerator, self.denominator))
```

## [9.1.2.1. さらに数のABCを追加する](https://docs.python.jp/3/library/numbers.html#adding-more-numeric-abcs)

> 数に対する ABC が他にも多く存在しうることは、言うまでもありません。それらの ABC を階層に追加する可能性が閉ざされるとしたら、その階層は貧相な階層でしかありません。たとえば、 MyFoo を Complex と Real の間に付け加えるには、次のようにします:

```python
class MyFoo(Complex): ...
MyFoo.register(Real)
```

## [9.1.2.2. 算術演算の実装](https://docs.python.jp/3/library/numbers.html#implementing-the-arithmetic-operations)

> 算術演算を実装する際には、型混合(mixed-mode)演算を行うと、作者が両方の引数の型について知っているような実装を呼び出すか、両方の引数をそれぞれ最も似ている組み込み型に変換してその型で演算を行うか、どちらになるのが望ましい実装です。つまり、 Integral のサブタイプに対しては __add__() と __radd__() を次のように定義するべきです:

```python
class MyIntegral(Integral):

    def __add__(self, other):
        if isinstance(other, MyIntegral):
            return do_my_adding_stuff(self, other)
        elif isinstance(other, OtherTypeIKnowAbout):
            return do_my_other_adding_stuff(self, other)
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, MyIntegral):
            return do_my_adding_stuff(other, self)
        elif isinstance(other, OtherTypeIKnowAbout):
            return do_my_other_adding_stuff(other, self)
        elif isinstance(other, Integral):
            return int(other) + int(self)
        elif isinstance(other, Real):
            return float(other) + float(self)
        elif isinstance(other, Complex):
            return complex(other) + complex(self)
        else:
            return NotImplemented
```

> ここには5つの異なる Complex のサブクラス間の混在型の演算があります。上のコードの中で MyIntegral と OtherTypeIKnowAbout に触れない部分を “ボイラープレート” と呼ぶことにしましょう。 a を Complex のサブタイプである A のインスタンス (a : A <: Complex)、同様に b : B <: Complex として、 a + b を考えます:

>         A が b を受け付ける __add__() を定義している場合、何も問題はありません。

>         A でボイラープレート部分に落ち込み、その結果 __add__() が値を返すならば、 B に良く考えられた __radd__() が定義されている可能性を見逃してしまいますので、ボイラープレートは __add__() から NotImplemented を返すのが良いでしょう。(若しくは、 A はまったく __add__() を実装すべきではなかったかもしれません。)

>         そうすると、 B の __radd__() にチャンスが巡ってきます。ここで a が受け付けられるならば、結果は上々です。

>         ここでボイラープレートに落ち込むならば、もう他に試すべきメソッドはありませんので、デフォルト実装の出番です。

>         もし B <: A ならば、Python は A.__add__ の前に B.__radd__ を試します。これで良い理由は、 A についての知識を持って実装しており、 Complex に委ねる前にこれらのインスタンスを扱えるはずだからです。

> もし A <: Complex かつ B <: Real で他に共有された知識が無いならば、適切な共通の演算は組み込みの complex を使ったものになり、どちらの __radd__() ともそこに着地するでしょうから、 a+b == b+a です。

> ほとんどの演算はどのような型についても非常に良く似ていますので、与えられた演算子について順結合(forward)および逆結合(reverse)のメソッドを生成する支援関数を定義することは役に立ちます。たとえば、 fractions.Fraction では次のようなものを利用しています:

```python
def _operator_fallbacks(monomorphic_operator, fallback_operator):
    def forward(a, b):
        if isinstance(b, (int, Fraction)):
            return monomorphic_operator(a, b)
        elif isinstance(b, float):
            return fallback_operator(float(a), b)
        elif isinstance(b, complex):
            return fallback_operator(complex(a), b)
        else:
            return NotImplemented
    forward.__name__ = '__' + fallback_operator.__name__ + '__'
    forward.__doc__ = monomorphic_operator.__doc__

    def reverse(b, a):
        if isinstance(a, Rational):
            # Includes ints.
            return monomorphic_operator(a, b)
        elif isinstance(a, numbers.Real):
            return fallback_operator(float(a), float(b))
        elif isinstance(a, numbers.Complex):
            return fallback_operator(complex(a), complex(b))
        else:
            return NotImplemented
    reverse.__name__ = '__r' + fallback_operator.__name__ + '__'
    reverse.__doc__ = monomorphic_operator.__doc__

    return forward, reverse

def _add(a, b):
    """a + b"""
    return Fraction(a.numerator * b.denominator +
                    b.numerator * a.denominator,
                    a.denominator * b.denominator)

__add__, __radd__ = _operator_fallbacks(_add, operator.add)

# ...
```


