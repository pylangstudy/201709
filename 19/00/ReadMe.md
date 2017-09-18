# [8.8.3. ファイナライザオブジェクト](https://docs.python.jp/3/library/weakref.html#example)

< [8.8. weakref — 弱参照](https://docs.python.jp/3/library/weakref.html) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/weakref.py](https://github.com/python/cpython/tree/3.6/Lib/weakref.py)

メモリ管理に関わる重要な項目。

## 概要

> The main benefit of using finalize is that it makes it simple to register a callback without needing to preserve the returned finalizer object. For instance

いきなり未翻訳文。[Google翻訳](https://translate.google.com/?hl=ja#en/ja/The%20main%20benefit%20of%20using%20finalize%20is%20that%20it%20makes%20it%20simple%20to%20register%20a%20callback%20without%20needing%20to%20preserve%20the%20returned%20finalizer%20object.%20For%20instance)すると以下。

> finalizeを使用する主な利点は、返されたファイナライザオブジェクトを保持せずにコールバックを簡単に登録できることです。 例えば

### 終了時に実行する

```python
import weakref
class Object: pass
kenny = Object()
weakref.finalize(kenny, print, "You killed Kenny!")  
del kenny
```

```sh
$ python 0.py 
You killed Kenny!
```

引数がわかりにくいし、1関数しか設定できない。1回しか実行されない（後述）。

クラスを継承して`__del__()`をカスタマイズすればもっと自由にできる。ただしクラスやメソッドの定義が必要なので面倒。

```python
import weakref
class Object:
    def __del__(self): print("You killed Kenny!")    
kenny = Object()
del kenny
```

継承クラスでの実装。`super()`の呼出が必要な分だけ面倒。

```python
class Object2(Object):
    def __del__(self):
        super().__del__()
        print("削除した！")
kenny = Object2()
del kenny
```

```sh
$ python 0_A.py 
You killed Kenny!

You killed Kenny!
削除した！
```

### 1回しか実行できない

`finalize`は1回目しか実行できない。1度実行されるとコールバック関数は解放される。ふつう`del`は1回しか実行しない。1回実行すれば終了を意味するので問題にはならないと思う。

以下はわざと`finalize`オブジェクトからコールバック関数を先に呼び出している。結果、`del`したときにコールバック関数が呼ばれない。

```python
import weakref
class Object: pass
def callback(x, y, z):
    print("CALLBACK")
    return x + y + z
obj = Object()
f = weakref.finalize(obj, callback, 1, 2, z=3)
assert f.alive
assert f() == 6
assert not f.alive
f()                     # callback not called because finalizer dead
del obj                 # callback not called because finalizer dead
```
```sh
$ python 1.py 
CALLBACK
```

### 解除

> You can unregister a finalizer using its detach() method. This kills the finalizer and returns the arguments passed to the constructor when it was created.

[翻訳](https://translate.google.com/?hl=ja#en/ja/You%20can%20unregister%20a%20finalizer%20using%20its%20detach()%20method.%20This%20kills%20the%20finalizer%20and%20returns%20the%20arguments%20passed%20to%20the%20constructor%20when%20it%20was%20created.%0A%3E%3E%3E)すると以下。

> ファイナライザの登録を解除するには、detach（）メソッドを使用します。 これはファイナライザを終了し、コンストラクタが作成されたときに渡された引数を返します。

```python
import weakref
class Object: pass
def callback(x, y, z):
    print("CALLBACK")
    return x + y + z
obj = Object()
f = weakref.finalize(obj, callback, 1, 2, z=3)
f_dead = f.detach()                                           
newobj, func, args, kwargs = f_dead
assert not f.alive
assert newobj is obj
assert func(*args, **kwargs) == 6 #ファイナライザ実行する
print('del直前')
del obj #ファイナライザ実行されない
```
```sh
$ python 2.py 
CALLBACK
del直前
```

### プログラム終了時に自動実行する

> Unless you set the atexit attribute to False, a finalizer will be called when the program exits if it is still alive. For instance

[翻訳](https://translate.google.com/?hl=ja#en/ja/Unless%20you%20set%20the%20atexit%20attribute%20to%20False%2C%20a%20finalizer%20will%20be%20called%20when%20the%20program%20exits%20if%20it%20is%20still%20alive.%20For%20instance)すると以下。

> atexit属性をFalseに設定しない限り、プログラムがまだ存在する場合に終了するときにファイナライザが呼び出されます。 例えば

```python
import weakref
class Object: pass
def callback(x, y, z):
    print("CALLBACK")
    return x + y + z
obj = Object()
f = weakref.finalize(obj, callback, 1, 2, z=3)
print('プログラム終了')
```

```sh
$ python 3.py 
プログラム終了
CALLBACK
```

これは期待通り。

### 複数のファイナライザ

同一オブジェクトに複数の`finalize`を設定してみた。実行順序がFILO(先入れ後出し)になっている。スタックと同様。予想通り。

```python
import weakref
class Object: pass
def callback(x, y, z):
    print(f"CALLBACK: {x + y + z}")
obj = Object()
f1 = weakref.finalize(obj, callback, 1, 2, z=3)
f2 = weakref.finalize(obj, callback, *[4, 5, 6])
f3 = weakref.finalize(obj, callback, **{'x':7, 'y':8, 'z':9})
del obj
print('プログラム終了')
```
```sh
$ python 4.py 
CALLBACK: 24
CALLBACK: 15
CALLBACK: 6
プログラム終了
```

