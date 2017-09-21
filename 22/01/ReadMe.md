# [8.9.4. コルーチンユーティリティ関数](https://docs.python.jp/3/library/types.html#coroutine-utility-functions)

< [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/weakref.py](https://github.com/python/cpython/tree/3.6/Lib/types.py)

## types.coroutine(gen_func)

> この関数は、 generator 関数を、ジェネレータベースのコルーチンを返す coroutine function に変換します。返されるジェネレータベースのコルーチンは依然として generator iterator ですが、同時に coroutine オブジェクトかつ awaitable であるとみなされます。ただし、必ずしも __await__() メソッドを実装する必要はありません。

> gen_func はジェネレータ関数で、インプレースに変更されます。

> gen_func がジェネレータ関数でない場合、この関数はラップされます。この関数が collections.abc.Generator のインスタンスを返す場合、このインスタンスは awaitable なプロキシオブジェクトにラップされます。それ以外のすべての型のオブジェクトは、そのまま返されます。

> バージョン 3.5 で追加.

いつも通り、Python文書だけでは使い方がわからなかった。以下参照。感謝。

* http://postd.cc/python-generators-coroutines-native-coroutines-and-async-await/

