# [8.9.2. 標準的なインタプリタ型](https://docs.python.jp/3/library/types.html#standard-interpreter-types)

< [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/weakref.py](https://github.com/python/cpython/tree/3.6/Lib/types.py)

## 概要

> このモジュールは、Python インタプリタを実装するために必要な多くの型に対して名前を提供します。それは、listiterator 型のような、単に処理中に付随的に発生するいくつかの型が含まれることを意図的に避けています。

> これらの名前は典型的に isinstance() や issubclass() によるチェックに使われます。

## 一覧

属性|説明
----|----
types.FunctionType, types.LambdaType|ユーザ定義の関数と lambda 式によって生成された関数の型です。
types.GeneratorType|ジェネレータ関数によって生成された ジェネレータ イテレータオブジェクトの型です。
types.CoroutineType|async def 関数に生成される コルーチン オブジェクトです。
types.AsyncGeneratorType|非同期ジェネレータ関数によって作成された 非同期ジェネレータ イテレータオブジェクトの型です。
types.CodeType|compile() 関数が返すようなコードオブジェクトの型です。
types.MethodType|ユーザー定義のクラスのインスタンスのメソッドの型です。
types.BuiltinFunctionType, types.BuiltinMethodType|len() や sys.exit() のような組み込み関数や、組み込み型のメソッドの型です。 (ここでは “組み込み” という単語を “Cで書かれた” という意味で使っています)
class types.ModuleType(name, doc=None)|module の型です。コンストラクタは生成するモジュールの名前と任意でその docstring を受け取ります。
types.TracebackType|sys.exc_info()[2] で得られるようなトレースバックオブジェクトの型です。
types.FrameType|フレームオブジェクトの型です。トレースバックオブジェクト tb の tb.tb_frame などです。
types.GetSetDescriptorType|FrameType.f_locals や array.array.typecode のような、拡張モジュールにおいて PyGetSetDef によって定義されたオブジェクトの型です。この型はオブジェクト属性のディスクリプタとして利用されます。 property 型と同じ目的を持った型ですが、こちらは拡張モジュールで定義された型のためのものです。
types.MemberDescriptorType|datetime.timedelta.days のような、拡張モジュールにおいて PyMemberDef によって定義されたオブジェクトの型です。この型は、標準の変換関数を利用するような、Cのシンプルなデータメンバで利用されます。 property 型と同じ目的を持った型ですが、こちらは拡張モジュールで定義された型のためのものです。
class types.MappingProxyType(mapping)|読み出し専用のマッピングのプロキシです。マッピングのエントリーに関する動的なビューを提供します。つまり、マッピングが変わった場合にビューがこれらの変更を反映するということです。


### class types.ModuleType(name, doc=None)

> インポートによりコントロールされる様々な属性を設定する場合、importlib.util.module_from_spec() を使用して新しいモジュールを作成してください。

属性|説明
----|----
__doc__|モジュールの docstring です。デフォルトは None です。
__loader__|モジュールをロードする loader です。デフォルトは None です。
__name__|モジュールの名前です。
__package__|モジュールがどの package に属しているかです。モジュールがトップレベルである (すなわち、いかなる特定のパッケージの一部でもない) 場合、この属性は '' に設定されます。そうでない場合、パッケージ名 (モジュールがパッケージ自身なら __name__) に設定されます。デフォルトは None です。

### class types.MappingProxyType(mapping)

操作|説明
----|----
key in proxy|元になったマッピングが key というキーを持っている場合 True を返します。そうでなければ False を返します。
proxy[key]|元になったマッピングの key というキーに対応するアイテムを返します。 key が存在しなければ、 KeyError が発生します。
iter(proxy)|元になったマッピングのキーを列挙するイテレータを返します。これは iter(proxy.keys()) のショートカットです。
len(proxy)|元になったマッピングに含まれるアイテムの数を返します。
copy()|元になったマッピングの浅いコピーを返します。
get(key[, default])|key が元になったマッピングに含まれている場合 key に対する値を返し、そうでなければ default を返します。もし default が与えられない場合は、デフォルト値の None になります。そのため、このメソッドが KeyError を発生させることはありません。
items()|元になったマッピングの items ((key, value) ペアの列) に対する新しいビューを返します。
keys()|元になったマッピングの keys に対する新しいビューを返します。
values()|元になったマッピングの values に対する新しいビューを返します。

