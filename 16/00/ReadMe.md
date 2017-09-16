# [8.7. array — 効率のよい数値アレイ](https://docs.python.jp/3/library/array.html#module-array)

< [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## 概要

> このモジュールでは、基本的な値 (文字、整数、浮動小数点数) のアレイ (array、配列) をコンパクトに表現できるオブジェクト型を定義しています。アレイはシーケンス (sequence) 型であり、中に入れるオブジェクトの型に制限があることを除けば、リストとまったく同じように振る舞います。オブジェクト生成時に一文字の 型コード を用いて型を指定します。次の型コードが定義されています:

型コード|C の型|Python の型|最小サイズ (バイト単位)|注釈
--------|------|-----------|-----------------------|----
'b'|signed char|int|1| 
'B'|unsigned char|int|1| 
'u'|Py_UNICODE|Unicode文字(unicode型)2|(1)
'h'|signed short|int|2| 
'H'|unsigned short|int|2| 
'i'|signed int|int|2| 
'I'|unsigned int|int|2| 
'l'|signed long|int|4| 
'L'|unsigned long|int|4| 
'q'|signed long long|int|8|(2)
'Q'|unsigned long long|int|8|(2)
'f'|float|float|4| 
'd'|double|float|8| 

`float`は日本語版では`浮動小数点数`とあったが英語版(原文)では`float`とあった。

## 注釈

> 1. タイプコード 'u' は Python の古い Unicode 文字 (Py_UNICODE あるいは wchar_t) を表します。プラットフォームに依存して、これは 16bit か 32bit になります。

> 'u' は将来的に他の Py_UNICODE API と一緒に削除されるでしょう。

> 3.3 より非推奨となりました。4.0 では削除される予定です。

> 2. タイプコード 'q' と 'Q' は Python をビルドしたプラットフォームのCコンパイラーが C言語の long long に対応しているか、 Windows で __int64 に対応している場合に利用可能です。

> バージョン 3.3 で追加.

> 値の実際の表現はマシンアーキテクチャ (厳密に言うとCの実装) によって決まります。値の実際のサイズは itemsize 属性から得られます。

## 一覧

このモジュールでは次の型を定義しています:

class array.array(typecode[, initializer])|要素のデータ型が typecode に限定される新しいアレイで、 オプションの値 initializer を渡すと初期値になりますが、 リスト、 bytes-like object または適当な型のイテレーション可能オブジェクトでなければなりません。
array.typecodes|すべての利用可能なタイプコードを含む文字列
array.typecode|アレイを作るときに使う型コード文字です。
array.itemsize|アレイの要素 1 つの内部表現に使われるバイト長です。
array.append(x)|値 x の新たな要素をアレイの末尾に追加します。
array.buffer_info()|アレイの内容を記憶するために使っているバッファの、現在のメモリアドレスと要素数の入ったタプル (address, length) を返します。


### 注釈

> C やC++ で書いたコードからアレイオブジェクトを使う場合 (buffer_info() の情報を使う意味のある唯一の方法です) は、アレイオブジェクトでサポートしているバッファインタフェースを使う方がより理にかなっています。このメソッドは後方互換性のために保守されており、新しいコードでの使用は避けるべきです。バッファインタフェースの説明は バッファプロトコル (buffer Protocol) にあります。

array.byteswap()|アレイのすべての要素に対して「バイトスワップ」 (リトルエンディアンとビッグエンディアンの変換) を行います。
array.count(x)|シーケンス中の x の出現回数を返します。
array.extend(iterable)|iterable から要素を取り出し、アレイの末尾に要素を追加します。
array.frombytes(s)|文字列から要素を追加します。バージョン 3.2 で追加: 明確化のため fromstring() の名前が frombytes() に変更されました。
array.fromfile(f, n)|ファイルオブジェクト f から (マシンのデータ形式そのままで) n 個の要素を読み出し、アレイの末尾に要素を追加します。
array.fromlist(list)|リストから要素を追加します。型に関するエラーが発生した場合にアレイが変更されないことを除き、 for x in list: a.append(x) と同じです。
array.fromstring()|frombytes() に対する廃止予定のエイリアス
array.fromunicode(s)|指定した Unicode 文字列のデータを使ってアレイを拡張します。
array.index(x)|アレイ中で x が出現するインデクスのうち最小の値 i を返します。
array.insert(i, x)|アレイ中の位置 i の前に値 x をもつ新しい要素を挿入します。 i の値が負の場合、アレイの末尾からの相対位置として扱います。
array.pop([i])|アレイからインデクスが i の要素を取り除いて返します。オプションの引数はデフォルトで -1 になっていて、最後の要素を取り除いて返すようになっています。
array.remove(x)|アレイ中の x のうち、最初に現れたものを取り除きます。
array.reverse()|アレイの要素の順番を逆にします。
array.tobytes()|array をマシンの値の array に変換して、 bytes の形で返します (tofile() メソッドを使ってファイルに書かれるバイト列と同じです)。バージョン 3.2 で追加: 明確化のため tostring() の名前が tobytes() に変更されました。
array.tofile(f)|すべての要素を (マシンの値の形式で) file object f に書き込みます。
array.tolist()|アレイを同じ要素を持つ普通のリストに変換します。
array.tostring()|tobytes() に対する廃止予定のエイリアス
array.tounicode()|アレイを Unicode 文字列に変換します。

## 参考

項目|概要
----|----
[struct](https://docs.python.jp/3/library/struct.html#module-struct) モジュール|異なる種類のバイナリデータのパックおよびアンパック。
[xdrlib](https://docs.python.jp/3/library/xdrlib.html#module-xdrlib) モジュール|遠隔手続き呼び出しシステムで使われる外部データ表現仕様 (External Data Representation, XDR) のデータのパックおよびアンパック。
[Numerical Python ドキュメント](https://docs.scipy.org/doc/)|Numeric Python 拡張モジュール (NumPy) では、別の方法でシーケンス型を定義しています。 Numerical Python に関する詳しい情報は [http://www.numpy.org/](http://www.numpy.org/) を参照してください。

## ソースコード

```python
import array
types = list(array.typecodes)
type_values = [bytes(b'\xFF'), bytes(b'\xFF'), 'A', [(2**15)-1], [(2**16)-1], [(2**15)-1], [(2**16)-1], [(2**31)-1], [(2**32)-1], [(2**63)-1], [(2**64)-1], [1.2], [1.2]]
type_dic = zip(types, type_values)
for k,v in type_dic:
    a = array.array(k,v)
    print(a.typecode, a.itemsize, a)
```
```sh
$ python 0.py 
b 1 array('b', [-1])
B 1 array('B', [255])
u 4 array('u', 'A')
h 2 array('h', [32767])
H 2 array('H', [65535])
i 4 array('i', [32767])
I 4 array('I', [65535])
l 4 array('l', [2147483647])
L 4 array('L', [4294967295])
q 8 array('q', [9223372036854775807])
Q 8 array('Q', [18446744073709551615])
f 4 array('f', [1.2000000476837158])
d 8 array('d', [1.2])
```

```python
import array
a = array.array('h')
print(a)
print('----- append, byteswap -----')
a.append(256)
print(f'{a[0]:3d} {a[0]:#x}')
a.byteswap()
print(f'{a[0]:3d} {a[0]:#x}')
print('----- count -----', a.count(1))
a.extend([2,3])
print('----- extend -----', a)
a = array.array('b', b'\x01')
a.frombytes(b'\x0F')
print('----- frombytes -----', a)
a = array.array('h')
a.fromlist([4,5])
print('----- fromlist -----', a)
a = array.array('u', 'A')
a.fromunicode('BC')
print('----- fromunicode -----', a)
print('----- index -----', a.index('C'))
a.insert(1, 'a')
print('----- insert -----', a)
print('----- pop -----', a.pop(1), a)
a.remove('A')
print('----- remove -----', a)
print('----- tobytes -----', a.tobytes())
#tofile()
print('----- tolist -----', a.tolist())
print('----- tostring -----', a.tostring())
print('----- tounicode -----', a.tounicode())
```
```sh
$ python 1.py 
array('h')
----- append, byteswap -----
256 0x100
  1 0x1
----- count ----- 1
----- extend ----- array('h', [1, 2, 3])
----- frombytes ----- array('b', [1, 15])
----- fromlist ----- array('h', [4, 5])
----- fromunicode ----- array('u', 'ABC')
----- index ----- 2
----- insert ----- array('u', 'AaBC')
----- pop ----- a array('u', 'ABC')
----- remove ----- array('u', 'BC')
----- tobytes ----- b'B\x00\x00\x00C\x00\x00\x00'
----- tolist ----- ['B', 'C']
----- tostring ----- b'B\x00\x00\x00C\x00\x00\x00'
----- tounicode ----- BC
```

