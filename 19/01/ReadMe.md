# [8.8.4. ファイナライザと __del__() メソッドとの比較](https://docs.python.jp/3/library/weakref.html#comparing-finalizers-with-del-methods)

< [8.8. weakref — 弱参照](https://docs.python.jp/3/library/weakref.html) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/weakref.py](https://github.com/python/cpython/tree/3.6/Lib/weakref.py)

メモリ管理に関わる重要な項目。

## 概要

> インスタンスが一時ディレクトリを表す、クラスを作成するとします。そのディレクトリは、次のイベントのいずれかが起きた時に、そのディレクトリの内容とともに削除されるべきです。

* オブジェクトのガベージコレクションが行われた場合
* オブジェクトの remove() メソッドが呼び出された場合
* プログラムが終了した場合

### __del__()

> ここでは、 __del__() メソッドを使用して次のようにクラスを実装します:

```python
import tempfile
import shutil
class TempDir:
    def __init__(self):
        self.name = tempfile.mkdtemp()
        print(self.name)

    def remove(self):
        if self.name is not None:
            shutil.rmtree(self.name)
            self.name = None
            print('削除した！')

    @property
    def removed(self):
        return self.name is None

    def __del__(self):
        self.remove()

td = TempDir()
del td
print('プログラム終了')
```
```sh
$ python 0.py 
/tmp/tmpdw42tozg
削除した！
プログラム終了
```

### finalize

> Starting with Python 3.4, __del__() methods no longer prevent reference cycles from being garbage collected, and module globals are no longer forced to None during interpreter shutdown. So this code should work without any issues on CPython.

> However, handling of __del__() methods is notoriously implementation specific, since it depends on internal details of the interpreter’s garbage collector implementation.

> A more robust alternative can be to define a finalizer which only references the specific functions and objects that it needs, rather than having access to the full state of the object:

[翻訳](https://translate.google.com/?hl=ja#en/ja/Starting%20with%20Python%203.4%2C%20__del__()%20methods%20no%20longer%20prevent%20reference%20cycles%20from%20being%20garbage%20collected%2C%20and%20module%20globals%20are%20no%20longer%20forced%20to%20None%20during%20interpreter%20shutdown.%20So%20this%20code%20should%20work%20without%20any%20issues%20on%20CPython.%0A%0AHowever%2C%20handling%20of%20__del__()%20methods%20is%20notoriously%20implementation%20specific%2C%20since%20it%20depends%20on%20internal%20details%20of%20the%20interpreter%E2%80%99s%20garbage%20collector%20implementation.%0A%0AA%20more%20robust%20alternative%20can%20be%20to%20define%20a%20finalizer%20which%20only%20references%20the%20specific%20functions%20and%20objects%20that%20it%20needs%2C%20rather%20than%20having%20access%20to%20the%20full%20state%20of%20the%20object%3A)すると以下。

> Python 3.4以降、__del __（）メソッドは参照サイクルがガベージコレクションされるのを防ぐことができなくなりました。インタプリタのシャットダウン中に、モジュールのグローバルはNoneに強制されなくなりました。 したがって、このコードはCPythonに問題なく動作します。

> しかし、__del __（）メソッドの処理は、インタープリタのガベージコレクタ実装の内部的な詳細に依存するため、実装固有のものであることはよく知られています。

> オブジェクトの完全な状態にアクセスするのではなく、必要な特定の関数とオブジェクトだけを参照するファイナライザを定義することが、より堅牢な方法です。

```python
class TempDir:
    def __init__(self):
        self.name = tempfile.mkdtemp()
        self._finalizer = weakref.finalize(self, shutil.rmtree, self.name)

    def remove(self):
        self._finalizer()

    @property
    def removed(self):
        return not self._finalizer.alive
```

[__del__()](https://docs.python.jp/3/reference/datamodel.html#object.__del__)は環境次第で実行されないかもしれない、ということか？`__del__()`より`finalize()`を使うべきと。

メンバ変数が増えて邪魔になる。

* http://atsuoishimoto.hatenablog.com/entry/2013/12/06/000000

どうやら`__del__`は使わないほうが良さそう。確実な終了処理の実行には以下の方法があると思う。

* 呼出元で`obj.remove()`を実行する（他の関数呼出と見分けがつかず、呼び忘れに気づきにくい）
* 上記例のように自分のクラス内で`finalize`を使い、呼出元で `del obj` を実行する
* 自分のクラス内でwith句メソッドを実装し、呼出元で `with TempDir() as obj:` を実行する


### 

> Defined like this, our finalizer only receives a reference to the details it needs to clean up the directory appropriately. If the object never gets garbage collected the finalizer will still be called at exit.

> The other advantage of weakref based finalizers is that they can be used to register finalizers for classes where the definition is controlled by a third party, such as running code when a module is unloaded:

[翻訳](https://translate.google.com/?hl=ja#en/ja/Defined%20like%20this%2C%20our%20finalizer%20only%20receives%20a%20reference%20to%20the%20details%20it%20needs%20to%20clean%20up%20the%20directory%20appropriately.%20If%20the%20object%20never%20gets%20garbage%20collected%20the%20finalizer%20will%20still%20be%20called%20at%20exit.%0A%0AThe%20other%20advantage%20of%20weakref%20based%20finalizers%20is%20that%20they%20can%20be%20used%20to%20register%20finalizers%20for%20classes%20where%20the%20definition%20is%20controlled%20by%20a%20third%20party%2C%20such%20as%20running%20code%20when%20a%20module%20is%20unloaded%3A)すると以下。

> このように定義されたファイナライザは、ディレクトリを適切に整理するために必要な詳細だけを参照します。 オブジェクトがガベージコレクションされない場合、終了時にファイナライザが呼び出されます。

> weakrefベースのファイナライザのもう1つの利点は、モジュールがアンロードされたときにコードを実行するなど、第三者によって定義が制御されるクラスのファイナライザを登録するために使用できることです。

意味不明。

```python
import weakref, sys
def unloading_module():
    # implicit reference to the module globals from the function body
weakref.finalize(sys.modules[__name__], unloading_module)
```

```python
import weakref, sys
def unloading_module():
    # implicit reference to the module globals from the function body
    print('unloading_module() !!')
weakref.finalize(sys.modules[__name__], unloading_module)
```

以下のようにする必要はあるのか？たぶん必要ない。モジュールが解放されたら自動的に`del`されると思う。

```python
import weakref, sys

class Object: pass
obj = Object()
def unloading_module():
    # implicit reference to the module globals from the function body
    global obj
    del obj
    print('unloading_module() !!')
weakref.finalize(sys.modules[__name__], unloading_module)
```
```sh
import weakref, sys

class Object: pass
obj = Object()
def unloading_module():
    # implicit reference to the module globals from the function body
    global obj
    del obj
    print('unloading_module() !!')
weakref.finalize(sys.modules[__name__], unloading_module)
print('プログラム終了')
```

