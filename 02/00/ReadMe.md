# [7.2. codecs — codec レジストリと基底クラス](https://docs.python.jp/3/library/codecs.html)

< [7. バイナリデータ処理](https://docs.python.jp/3/library/binary.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/codecs.py](https://github.com/python/cpython/tree/3.6/Lib/codecs.py)

> このモジュールは、標準的な Python codec (エンコーダとデコーダ) 用の基底クラスを定義し、codec とエラー処理検索プロセスを管理する内部の Python codec レジストリへのアクセスを提供します。多くの codec はテキストをバイト形式にエンコードする テキストエンコーディング ですが、テキストをテキストに、またはバイトをバイトにエンコードする codec も提供されています。カスタムの codec は任意の型間でエンコードとデコードを行えますが、一部のモジュール機能は テキストエンコーディング か bytes へのエンコードのみに制限されています。

文字コードの相互変換ができる、ということでいいのか？

> このモジュールでは、任意の codec でエンコードやデコードを行うための、以下の関数が定義されています。

## codecsモジュール

メソッド|説明
--------|----
codecs.encode(obj, encoding='utf-8', errors='strict')|encoding に記載された codec を使用して obj をエンコードします。
codecs.decode(obj, encoding='utf-8', errors='strict')|encoding に記載された codec を使用して obj をデコードします。
codecs.lookup(encoding)|Python codec レジストリから codec 情報を探し、以下で定義するような CodecInfo オブジェクトを返します。
codecs.getencoder(encoding)|与えられたエンコーディングに対する codec を検索し、エンコーダ関数を返します。
codecs.getdecoder(encoding)|与えられたエンコーディングに対する codec を検索し、デコーダ関数を返します。
codecs.getincrementalencoder(encoding)|与えられたエンコーディングに対する codec を検索し、インクリメンタル・エンコーダクラスまたはファクトリ関数を返します。
codecs.getincrementaldecoder(encoding)|与えられたエンコーディングに対する codec を検索し、インクリメンタル・デコーダクラスまたはファクトリ関数を返します。
codecs.getreader(encoding)|与えられたエンコーディングに対する codec を検索し、StreamReader クラスまたはファクトリ関数を返します。
codecs.getwriter(encoding)|与えられたエンコーディングに対する codec を検索し、StreamWriter クラスまたはファクトリ関数を返します。
codecs.register(search_function)|codec 検索関数を登録します。検索関数は第 1 引数にすべてアルファベットの小文字から成るエンコーディング名を取り、CodecInfo オブジェクトを返します。
codecs.open(filename, mode='r', encoding=None, errors='strict', buffering=1)|エンコードされたファイルを mode を使って開き、透過的なエンコード/デコードを提供する StreamReaderWriter のインスタンスを返します。
codecs.EncodedFile(file, data_encoding, file_encoding=None, errors='strict')|透過的なエンコード変換を行うファイルのラップされたバージョンである、StreamRecoder インスタンスを返します。
codecs.iterencode(iterator, encoding, errors='strict', **kwargs)|インクリメンタル・エンコーダを使って、 iterator から供給される入力を反復的にエンコードします。
codecs.iterdecode(iterator, encoding, errors='strict', **kwargs)|インクリメンタル・デコーダを使って、 iterator から供給される入力を反復的にデコードします。このモジュールは以下のような定数も定義しています。プラットフォーム依存なファイルを読み書きするのに役立ちます:

### 定数

* codecs.BOM
* codecs.BOM_BE
* codecs.BOM_LE
* codecs.BOM_UTF8
* codecs.BOM_UTF16
* codecs.BOM_UTF16_BE
* codecs.BOM_UTF16_LE
* codecs.BOM_UTF32
* codecs.BOM_UTF32_BE
* codecs.BOM_UTF32_LE

> これらの定数は、いくつかのエンコーディングの Unicode のバイトオーダマーク (BOM) で、様々なバイトシーケンスを定義します。これらは、UTF-16 と UTF-32 のデータストリームで使用するバイトオーダを指定したり、 UTF-8 で Unicode シグネチャとして使われます。 BOM_UTF16 は、プラットフォームのネイティブバイトオーダによって BOM_UTF16_BE または BOM_UTF16_LE です。 BOM は BOM_UTF16 のエイリアスです。同様に、 BOM_LE は BOM_UTF16_LE の、 BOM_BE は BOM_UTF16_BE のエイリアスです。その他の定数は UTF-8 と UTF-32 エンコーディングの BOM を表します。

## CodecInfoクラス

属性|説明
----|----
name|エンコーディングの名前です。
encode, decode|ステートレスなエンコーディングとデコーディングの関数です。
incrementalencoder, incrementaldecoder|インクリメンタル・エンコーダとデコーダのクラスまたはファクトリ関数です。
streamwriter, streamreader|ストリームライターとリーダーのクラスまたはファクトリ関数です。

### codecs.open()

> 注釈

> 下層のエンコードされたファイルは、常にバイナリモードで開きます。読み書き時に、 '\n' の自動変換は行われません。mode 引数は、組み込みの open() 関数が受け入れる任意のバイナリモードにすることができます。'b' が自動的に付加されます。

> encoding は、そのファイルに対して使用されるエンコーディングを指定します。バイトにエンコードする、あるいはバイトからデコードするすべてのエンコーディングが許可されます。ファイルメソッドがサポートするデータ型は、使用される codec によって異なります。

> エラーハンドリングのために errors を渡すことができます。これはデフォルトでは 'strict' で、エンコード時にエラーがあれば ValueError を送出します。

> buffering は組み込み関数 open() の場合と同じ意味を持ちます。デフォルトでは行バッファリングです。





