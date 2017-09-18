# [8.8.1. 弱参照オブジェクト](https://docs.python.jp/3/library/weakref.html#weak-reference-objects)

< [8.8. weakref — 弱参照](https://docs.python.jp/3/library/weakref.html) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/weakref.py](https://github.com/python/cpython/tree/3.6/Lib/weakref.py)

メモリ管理に関わる重要な項目。

## コード例

### __callback__

> Weak reference objects have no methods and no attributes besides ref.__callback__. A weak reference object allows the referent to be obtained, if it still exists, by calling it:

いきなり未翻訳文。[Google翻訳](https://translate.google.com/?hl=ja#en/ja/Weak%20reference%20objects%20have%20no%20methods%20and%20no%20attributes%20besides%20ref.__callback__.%20A%20weak%20reference%20object%20allows%20the%20referent%20to%20be%20obtained%2C%20if%20it%20still%20exists%2C%20by%20calling%20it%3A)すると以下。

> 弱い参照オブジェクトにはメソッドはなく、ref .__ callback__以外の属性もありません。 弱参照オブジェクトは、それがまだ存在する場合、それを呼び出すことによって、参照対象が得られるようにします：

```python
import weakref
class Object:
    pass
o = Object()
r = weakref.ref(o)
o2 = r()

print('o:', o)
print('r:', r)
print('o2:', o2)
print('o is o2:', o is o2)
```

Python文書のコード例にしてはめずらしく`import weakref`とインポート文が書いてあった。毎回そうしてくれると助かるのだが。

### r, r()

```python
o = Object()
r = weakref.ref(o)
o2 = r()
```

その前に、`r`と`r()`が別のものを指しているのが気になる。

インスタンス|指しているもの
------------|--------------
`r`|weakref.refインスタンス
`r()`|Objectインスタンス

弱参照しているインスタンスを取得するためには`r()`と`()`をつけねばならない。冗長で嫌だが、弱参照と参照先の両方に明示的にアクセスできる。

（`r()`の記法は`object.__call__()`のオーバーライド実装と思われる）

`weakref.proxy`クラスなら`r`で参照先が参照できる。こっちのほうが常用しやすそう。Python文書にコード例はない。[前回](https://github.com/pylangstudy/201709/tree/master/17/00)の[weakref.proxy.py](https://github.com/pylangstudy/201709/blob/master/17/00/weakref.proxy.py)参照。

### 削除後の参照

> リファレントがもはや存在しないならば、参照オブジェクトの呼び出しは None を返します:

```python
>>> del o, o2
>>> print(r())
None
```

上記だけではよくわからない。`o`, `r`, `o2`, `r()`の値について確認してみた。

まずは`o`削除。まだ`r`の参照が削除されない。`r`は`o`の弱参照だが、大本の`o`が削除しても`r`の参照が消えない。おそらく`o2`も`o`を参照しているから。

```python
del o
#print('o:', o)     #NameError: name 'o' is not defined
print('r:', r)      #<weakref at 0xb70bd324; to 'Object' at 0xb70fcdcc>
print('o2:', o2)    #<__main__.Object object at 0xb70fcdcc>
print('r():', r())  #<__main__.Object object at 0xb7199e2c>
```

つぎに`o2`削除。これで`r`の参照が死んだ。そのインスタンスを取得する`r()`は`None`を返す。

```python
del o2
print('r:', r)      #<weakref at 0xb70b3324; dead>
print('r():', r())  #None
```

### 弱参照しているオブジェクトの生存確認

```python
if r() is not None:
    print('生きてる！')
else:
    print('死んでる…')
```

```python
import weakref

class Object:
    def __del__(self): print('今まさに死亡中…')
def is_life(r:weakref.ref):
    if r() is not None:
        print('まだ生きてる！')
    else:
        print('もう死んでる（泣）')

#o = object()#TypeError: cannot create weak reference to 'object' object
o = Object()
r = weakref.ref(o)
is_life(r)
del o
is_life(r)
```
```sh
$ python 1.py 
まだ生きてる！
今まさに死亡中…
もう死んでる（泣）
```

> “生存性(liveness)”のテストを分割すると、スレッド化されたアプリケーションにおいて競合状態を作り出します。 (訳注:if r() is not None: r().do_something() では、2度目のr()がNoneを返す可能性があります) 弱参照が呼び出される前に、他のスレッドは弱参照が無効になる原因となり得ます。上で示したイディオムは、シングルスレッドのアプリケーションと同じくマルチスレッド化されたアプリケーションにおいても安全です。

### サブクラス化

> サブクラス化を行えば、 ref オブジェクトの特殊なバージョンを作成できます。これは WeakValueDictionary の実装で使われており、マップ内の各エントリによるメモリのオーバヘッドを減らしています。こうした実装は、ある参照に追加情報を関連付けたい場合に便利ですし、リファレントを取り出すための呼び出し時に何らかの追加処理を行いたい場合にも使えます。

> 以下の例では、 ref のサブクラスを使って、あるオブジェクトに追加情報を保存し、リファレントがアクセスされたときにその値に作用をできるようにするための方法を示しています:

```python
import weakref

class ExtendedRef(weakref.ref):
    def __init__(self, ob, callback=None, **annotations):
        super(ExtendedRef, self).__init__(ob, callback)
        self.__counter = 0
        for k, v in annotations.items():
            setattr(self, k, v)

    def __call__(self):
        """Return a pair containing the referent and the number of
        times the reference has been called.
        """
        ob = super(ExtendedRef, self).__call__()
        if ob is not None:
            self.__counter += 1
            ob = (ob, self.__counter)
        return ob

class Object: pass
o = Object()
r = ExtendedRef(o)

# r()で参照した回数を__counterにインクリメントする
print(r._ExtendedRef__counter)
r()
print(r._ExtendedRef__counter)
r()
print(r._ExtendedRef__counter)

# 参照が死んでいるならインクリメントしない
del o
r()
print(r._ExtendedRef__counter)
```
```sh
$ python 2.py 
0
1
2
2
```

