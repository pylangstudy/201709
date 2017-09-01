# < [7.1.3. クラス](https://docs.python.jp/3/library/struct.html#classes)

< [7. バイナリデータ処理](https://docs.python.jp/3/library/binary.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

コンストラクタ|説明
--------------|----
class struct.Struct(format)|フォーマット文字列 format に従ってバイナリデータを読み書きする、新しい Struct オブジェクトを返します。 Struct オブジェクトを一度作ってからそのメソッドを使うと、フォーマット文字列のコンパイルが一度で済むので、 struct モジュールの関数を同じフォーマットで何度も呼び出すよりも効率的です。

メソッド|説明
--------|----
pack(v1, v2, ...)|pack() 関数と同じ、コンパイルされたフォーマットを利用するメソッドです。 (len(result) は size と等しいでしょう)
pack_into(buffer, offset, v1, v2, ...)|pack_into() 関数と同じ、コンパイルされたフォーマットを利用するメソッドです。
unpack(buffer)|unpack() 関数と同じ、コンパイルされたフォーマットを利用するメソッドです。 (buffer のバイト数は size と等しくなければなりません)。
unpack_from(buffer, offset=0)|unpack_from() 関数と同じ、コンパイルされたフォーマットを利用するメソッドです。 (buffer のバイト数 - offset は少なくとも size 以上でなければなりません)。
iter_unpack(buffer)|iter_unpack() 関数と同じ、コンパイルされたフォーマットを利用するメソッドです。 (buffer のバイト数は size の倍数でなければなりません)。バージョン 3.4 で追加.

属性|説明
----|----
format|この Struct オブジェクトを作成する時に利用されたフォーマット文字列です。
size|format 属性に対応する構造体の (従って pack() メソッドによって作成されるバイト列オブジェクトの) サイズです。


```python
import struct
from collections import namedtuple

#Unicode文字列をbytesに変換する
def U2B(unistr, maxlen):
    bytstr = unistr.encode()
    len_diff = maxlen - len(bytstr)
    if len_diff < 0: raise Exception(f'最大バイト長を超えています。:unistr={unistr}, maxlen={maxlen}, len(bytstr)={len(bytstr)}, bytstr={bytstr}')
    else: return bytstr + struct.pack(f'{len_diff}B', *([0]*len_diff))

maxlen = 10
studentStruct = struct.Struct(f'<{maxlen}sHHb')
studentTuple = namedtuple('Student', 'name serialnum school gradelevel')

for record in [
        b'raymond   \x32\x12\x08\x01\x08',
        b'Taniguchi \x01\x00\x08\x01\x04', 
        b'Yamada    \x01\x01\x08\x01\x02',
        U2B('真田', maxlen) + b'\x01\x01\x08\x01\x02']:
    s = studentTuple._make(studentStruct.unpack(record))
    print('name:', s.name.decode(), s.name)
    print('  serialnum :', s.serialnum)
    print('  school    :', s.school)
    print('  gradelevel:', s.gradelevel)
```
```sh
$ python 1.py 
name: raymond    b'raymond   '
  serialnum : 4658
  school    : 264
  gradelevel: 8
name: Taniguchi  b'Taniguchi '
  serialnum : 1
  school    : 264
  gradelevel: 4
name: Yamada     b'Yamada    '
  serialnum : 257
  school    : 264
  gradelevel: 2
name: 真田 b'\xe7\x9c\x9f\xe7\x94\xb0\x00\x00\x00\x00'
  serialnum : 257
  school    : 264
  gradelevel: 2
```

ポイントは、Unicode文字列をバイト列に変換して固定長にすること。

