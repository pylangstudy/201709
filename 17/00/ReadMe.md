# [8.8. weakref — 弱参照](https://docs.python.jp/3/library/weakref.html)

< [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/weakref.py](https://github.com/python/cpython/tree/3.6/Lib/weakref.py)

メモリ管理に関わる重要な項目。

## 弱参照

* https://ja.wikipedia.org/wiki/%E5%BC%B1%E3%81%84%E5%8F%82%E7%85%A7

> 弱い参照は、不要となったオブジェクトが循環参照によって解放されないという問題を防ぐために用いられる。

Wikipediaはわかりやすい。Python文書は意味不明。

## 概要

> weakref モジュールは、Pythonプログラマがオブジェクトへの弱参照 (weak refarence)を作成できるようにします。

> 以下では、用語リファレント(referent) は弱参照が参照するオブジェクトを意味します。

> オブジェクトへの弱参照があることは、そのオブジェクトを生かしておくのには不十分です。リファレントへの参照が弱参照しか残っていない場合、 garbage collection はリファレントを自由に破棄し、メモリを別のものに再利用することができます。しかし、オブジェクトへの強参照がなくても、オブジェクトが実際に破棄されるまでは、弱参照はオブジェクトを返す場合があります。

> 弱参照の主な用途は、巨大なオブジェクトを保持するキャッシュやマッピングを実装することです。ここで、キャッシュやマッピングに保持されているからという理由だけで、巨大なオブジェクトが生き続けることは望ましくありません。

> 例えば、巨大なバイナリ画像のオブジェクトがたくさんあり、それぞれに名前を関連付けたいとします。 Python の辞書型を使って名前を画像に対応付けたり画像を名前に対応付けたりすると、画像オブジェクトは辞書内のキーや値に使われているため存続しつづけることになります。 weakref モジュールが提供している WeakKeyDictionary や WeakValueDictionary クラスはその代用で、対応付けを構築するのに弱参照を使い、キャッシュやマッピングに存在するという理由だけでオブジェクトを存続させないようにします。例えば、もしある画像オブジェクトが WeakValueDictionary の値になっていた場合、最後に残った画像オブジェクトへの参照を弱参照マッピングが保持していれば、ガーベジコレクションはこのオブジェクトを再利用でき、画像オブジェクトに対する弱参照内の対応付けは削除されます。

> WeakKeyDictionary と WeakValueDictionary はその実装に弱参照を使用しており、キーや値がガーベジコレクションによって回収されたことを弱参照辞書に通知するコールバック関数を設定しています。 WeakSet は set インターフェースを実装していますが、 WeakKeyDictionary のように要素への弱参照を持ちます。

* [weakref](https://docs.python.jp/3/library/weakref.html#module-weakref)
    * [WeakKeyDictionary](https://docs.python.jp/3/library/weakref.html#weakref.WeakKeyDictionary)
    * [WeakValueDictionary](https://docs.python.jp/3/library/weakref.html#weakref.WeakValueDictionary)
    * [WeakSet](https://docs.python.jp/3/library/weakref.html#weakref.WeakSet)

> finalize は、オブジェクトのガベージコレクションの実行時にクリーンアップ関数が呼び出されるように登録する、単純な方法を提供します。これは、未加工の弱参照上にコールバック関数を設定するよりも簡単です。なぜなら、オブジェクトのコレクションが完了するまでファイナライザが生き続けることを、モジュールが自動的に保証するからです。

* [finalize](https://docs.python.jp/3/library/weakref.html#weakref.finalize)

> ほとんどのプログラムでは弱参照コンテナまたは finalize のどれかを使えば必要なものは揃うはずです。通常は直接自前の弱参照を作成する必要はありません。低レベルな機構は、より進んだ使い方をするために weakref モジュールとして公開されています。

> 全てのオブジェクトが弱参照で参照できるわけではありません; 弱参照で参照できるのは、クラスインスタンス、(C ではなく) Python で書かれた関数、インスタンスメソッド、set オブジェクト、frozenset オブジェクト、 file オブジェクト 、 generator 型のオブジェクト、socket オブジェクト、array オジェクト、deque オブジェクト、正規表現パターンオブジェクト、code オブジェクトです。

> バージョン 3.2 で変更: thread.lock, threading.Lock, code オブジェクトのサポートが追加されました。

> list や dict など、いくつかの組み込み型は弱参照を直接サポートしませんが、以下のようにサブクラス化を行えばサポートを追加できます:

```python
class Dict(dict):
    pass

obj = Dict(red=1, green=2, blue=3)   # this object is weak referenceable
```

> tuple と int のような他の組み込み型はサブクラス化しても弱参照はサポートしません。(これは実装詳細であり、他の様々な Python 実装では異なる可能性があります。)。

> 拡張型は、簡単に弱参照をサポートできます。詳細については、 弱参照(Weak Reference)のサポート を参照してください。

* [弱参照(Weak Reference)のサポート](https://docs.python.jp/3/extending/newtypes.html#weakref-support)

## 一覧

クラス|概要
------|----
class weakref.ref(object[, callback])|object への弱参照を返します。
class weakref.WeakKeyDictionary([dict])|キーを弱参照するマッピングクラス。
class weakref.WeakValueDictionary([dict])|値を弱参照するマッピングクラス。
class weakref.WeakSet([elements])|要素への弱参照を持つ集合型。
class weakref.WeakMethod(method)|ref のサブクラス
class weakref.finalize(obj, func, *args, **kwargs)|obj がガベージコレクションで回収されるときに呼び出される、呼び出し可能なファイナライザオブジェクトを返します。
exception weakref.ReferenceError|ReferenceError 例外と同じです。 

属性|説明
----|----
class weakref.ref(object[, callback])|object への弱参照を返します。リファレントがまだ生きているならば、元のオブジェクトは参照オブジェクトの呼び出しで取り出せす。リファレントがもはや生きていないならば、参照オブジェクトを呼び出したときに None を返します。 callback に None 以外の値を与えた場合、オブジェクトをまさに後始末処理しようとするときに呼び出します。このとき弱参照オブジェクトは callback の唯一のパラメタとして渡されます。リファレントはもはや利用できません。
__callback__|この読み込み専用の属性は、現在弱参照に関連付けられているコールバックを返します。コールバックが存在しないか、弱参照のリファレントが生きていない場合、この属性の値は None になります。
weakref.proxy(object[, callback])|弱参照を使う object へのプロキシを返します。弱参照オブジェクトを明示的な参照外しをしながら利用する代わりに、多くのケースでプロキシを利用することができます。返されるオブジェクトは、 object が呼び出し可能かどうかによって、 ProxyType または CallableProxyType のどちらかの型を持ちます。プロキシオブジェクトはリファレントに関係なくハッシュ可能(hashable)ではありません。これによって、それらの基本的な変更可能という性質による多くの問題を避けています。そして、辞書のキーとしての利用を妨げます。 callback は ref() 関数の同じ名前のパラメータと同じものです。(— 訳注: リファレントが変更不能型であっても、プロキシはリファレントが消えるという状態の変更があるために、変更可能型です。—)
weakref.getweakrefcount(object)|object を参照する弱参照とプロキシの数を返します。
weakref.getweakrefs(object)|object を参照するすべての弱参照とプロキシオブジェクトのリストを返します。

属性|説明
----|----
class weakref.WeakKeyDictionary([dict])|キーを弱参照するマッピングクラス。キーへの強参照がなくなったときに、辞書のエントリは捨てられます。アプリケーションの他の部分が所有するオブジェクトへ属性を追加することもなく、それらのオブジェクトに追加データを関連づけるために使うことができます。これは属性へのアクセスをオーバーライドするオブジェクトに特に便利です。警告: WeakKeyDictionary は Python 辞書型の上に作られているので、反復処理を行うときにはサイズ変更してはなりません。
WeakKeyDictionary.keyrefs()|キーへの弱参照を持つ iterable オブジェクトを返します。

属性|説明
----|----
class weakref.WeakValueDictionary([dict])|値を弱参照するマッピングクラス。値への強参照が存在しなくなったときに、辞書のエントリは捨てられます。警告: WeakValueDictionary は Python 辞書型の上に作られているので、反復処理を行うときにはサイズ変更してはなりません。
WeakValueDictionary.valuerefs()|値への弱参照を持つ iterable オブジェクトを返します。

属性|説明
----|----
class weakref.WeakSet([elements])|要素への弱参照を持つ集合型。要素への強参照が無くなったときに、その要素は削除されます。

属性|説明
----|----
class weakref.WeakMethod(method)|拡張された ref のサブクラスで、束縛されたメソッドへの弱参照をシミュレートします (つまり、クラスで定義され、インスタンスにあるメソッド)。 束縛されたメソッドは短命なので、標準の弱参照では保持し続けられません。 WeakMethod には、オブジェクトと元々の関数が死ぬまで束縛されたメソッドを再作成する特別なコードがあります:

属性|説明
----|----
class weakref.finalize(obj, func, *args, **kwargs)|obj がガベージコレクションで回収されるときに呼び出される、呼び出し可能なファイナライザオブジェクトを返します。 通常の弱参照とは異なり、ファイナライザは参照しているオブジェクトが回収されるまで必ず生き残り、そのおかげでライフサイクル管理が大いに簡単になります。
__call__()|If self is alive then mark it as dead and return the result of calling func(*args, **kwargs). If self is dead then return None.
detach()|If self is alive then mark it as dead and return the tuple (obj, func, args, kwargs). If self is dead then return None.
peek()|If self is alive then return the tuple (obj, func, args, kwargs). If self is dead then return None.
alive|ファイナライザが生きている場合には真、そうでない場合には偽のプロパティです。
atexit|A writable boolean property which by default is true. When the program exits, it calls all remaining live finalizers for which atexit is true. They are called in reverse order of creation.注釈 It is important to ensure that func, args and kwargs do not own any references to obj, either directly or indirectly, since otherwise obj will never be garbage collected. In particular, func should not be a bound method of obj.
weakref.ReferenceType|弱参照オブジェクトのための型オブジェクト。
weakref.ProxyType|呼び出し可能でないオブジェクトのプロキシのための型オブジェクト。
weakref.CallableProxyType|呼び出し可能なオブジェクトのプロキシのための型オブジェクト。
weakref.ProxyTypes|プロキシのためのすべての型オブジェクトを含むシーケンス。これは両方のプロキシ型の名前付けに依存しないで、オブジェクトがプロキシかどうかのテストをより簡単にできます。

属性|説明
----|----
exception weakref.ReferenceError|プロキシオブジェクトが使われても、元のオブジェクトがガベージコレクションされてしまっているときに発生する例外。これは標準の ReferenceError 例外と同じです。

## 参考

[PEP 205](https://www.python.org/dev/peps/pep-0205) - 弱参照

> この機能の提案と理論的根拠。初期の実装と他の言語における類似の機能についての情報へのリンクを含んでいます。

## 外部参考

* http://ja.pymotw.com/2/weakref/

感謝。

