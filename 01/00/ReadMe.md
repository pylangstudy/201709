# < [7.1.2. 書式文字列](https://docs.python.jp/3/library/struct.html#format-strings)

< [7. バイナリデータ処理](https://docs.python.jp/3/library/binary.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## [7.1.2.1. バイトオーダ、サイズ、アラインメント](https://docs.python.jp/3/library/struct.html#byte-order-size-and-alignment)

文字|バイトオーダ|サイズ|アラインメント
----|------------|------|--------------
`@`|native|native|native
`=`|native|standard|none
`<`|リトルエンディアン|standard|none
`>`|ビッグエンディアン|standard|none
`!`|ネットワーク (= ビッグエンディアン)|standard|none

* [エンディアン](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%B3%E3%83%87%E3%82%A3%E3%82%A2%E3%83%B3)参照
* バイトオーダー=nativeは計算機に依存する（リトルorビッグ）
* サイズ=native, アラインメント=nativeは C コンパイラの sizeof 式で決定される
* サイズ=standardは[書式指定文字](https://docs.python.jp/3/library/struct.html#format-characters)で決定される

> '!' 表記は、ネットワークバイトオーダがビッグエンディアンかリトルエンディアンか忘れてしまったという不運な方のために用意されています。

とあるが、`!`の意味を覚えるほうが難しいと思う。

## [7.1.2.2. 書式指定文字](https://docs.python.jp/3/library/struct.html#format-characters)

書式文字|Cの型|Pythonの型|標準サイズ
--------|-----|----------|----------
`x`|パディングバイト|値なし| 
`c`|char|長さ 1 のバイト列|1
`b`|signed char|整数|1
`B`|unsigned char|整数|1
`?`|_Bool|真偽値型(bool)|1
`h`|short|整数|2
`H`|unsigned short|整数|2
`i`|int|整数|4
`I`|unsigned int|整数|4
`l`|long|整数|4
`L`|unsigned long|整数|4
`q`|long long|整数|8
`Q`|unsigned long long|整数|8
`n`|ssize_t|整数| 
`N`|size_t|整数| 
`e`|(7)|浮動小数点数|2
`f`|float|浮動小数点数|4
`d`|double|浮動小数点数|8
`s`|char[]|bytes| 
`p`|char[]|bytes| 
`P`|void *|整数| 

### 記法

項目|説明
----|----
繰り返し|`4h`は`hhhh`と同じ。short型4件分。
`s`の繰り返し|バイト長として解釈される。例えば`10s`は10バイトの文字列, `10c`は10個の文字。デフォルト値`1`。`0s`は単一の空文字列, `0c`は0個の文字。
無視|フォーマット文字間の空白文字は無視される（countとフォーマット文字の間にスペースを入れてはいけない）

## [7.1.2.3. 使用例](https://docs.python.jp/3/library/struct.html#examples)

### pack, unpack

Python文書の例はマシンがBigEndianの場合の結果。マシン依存にしたくないなら以下のようにリトル`<`かビッグ`>`のいずれかを明示すべき。

```python
import struct
print('----- Endian=Native -----')
print(struct.pack('hhl', 1, 2, 3))
print(struct.unpack('hhl', b'\x00\x01\x00\x02\x00\x00\x00\x03'))
print(struct.calcsize('hhl'))

print('----- Endian=Little -----')
print(struct.pack('<hhl', 1, 2, 3))
print(struct.unpack('<hhl', b'\x00\x01\x00\x02\x00\x00\x00\x03'))
print(struct.calcsize('<hhl'))

print('----- Endian=Big -----')
print(struct.pack('>hhl', 1, 2, 3))
print(struct.unpack('>hhl', b'\x00\x01\x00\x02\x00\x00\x00\x03'))
print(struct.calcsize('>hhl'))
```
```sh
$ python 0.py 
----- Endian=Native -----
b'\x01\x00\x02\x00\x03\x00\x00\x00'
(256, 512, 50331648)
8
----- Endian=Little -----
b'\x01\x00\x02\x00\x03\x00\x00\x00'
(256, 512, 50331648)
8
----- Endian=Big -----
b'\x00\x01\x00\x02\x00\x00\x00\x03'
(1, 2, 3)
8
```

### 名付け

```python
import struct
print('----- tuple -----')
record = b'raymond   \x32\x12\x08\x01\x08'
name, serialnum, school, gradelevel = struct.unpack('<10sHHb', record)
print(f'name={name}, serialnum={serialnum}, school={school}, gradelevel={gradelevel}')

print('----- namedtuple -----')
from collections import namedtuple
Student = namedtuple('Student', 'name serialnum school gradelevel')
s = Student._make(struct.unpack('<10sHHb', record))
print(s)
print(s.name)
print(s.serialnum)
print(s.school)
print(s.gradelevel)
```
```sh
$ python 1.py 
----- tuple -----
name=b'raymond   ', serialnum=4658, school=264, gradelevel=8
----- namedtuple -----
Student(name=b'raymond   ', serialnum=4658, school=264, gradelevel=8)
b'raymond   '
4658
264
8
```

* [collections.namedtuple](https://docs.python.jp/3/library/collections.html#collections.namedtuple)

### フォーマット文字の順序によってサイズが変わりうる

アラインメントが生じるから。

```python
import struct
print('ci:', struct.calcsize('ci'), struct.pack('ci', b'*', 0x12131415))
print('ic:', struct.calcsize('ic'), struct.pack('ic', 0x12131415, b'*'))
```
```sh
$ python 2.py 
ci: 8 b'*\x00\x00\x00\x15\x14\x13\x12'
ic: 5 b'\x15\x14\x13\x12*'
```

`c`=1字(char,1Byte), `i`=int(32bitマシンなら32bit(4Byte))。`ci`は1char+1int。`ic`は1int+1char。[アラインメント](https://ja.wikipedia.org/wiki/%E3%82%A2%E3%83%A9%E3%82%A4%E3%83%A1%E3%83%B3%E3%83%88)とは、メモリのアドレスが2,4,8の倍数などの丁度の位置くるよう調整すること。これによりアクセス速度が早くなる。反面メモリ領域が無駄になる。

たとえば、このプログラムを実行するコンピュータが32bitマシンなら、最低メモリ確保量は32bit(4Byte)となる。`c`は1Byteだが、アラインメントサイズが32bit(4Byte)なので、4Byte分のメモリ確保がされる。ただし、後続のデータが無い場合、アクセス位置を算出する必要はないためアラインメント領域を確保する必要がない。

固定長データ(2,4,8Byte等)はアラインメントの必要が無いためメモリの無駄が無い。しかし文字列のような可変長データはアラインメントサイズぴったりにならない分だけメモリの無駄使いが生じる。

#### マシン固有エンディアン

Python文書では以下のように書いてある。

> long 型が 4 バイトを境界としてそろえられていると仮定して、末端に 2 バイトをパディングします:

> ネイティブのサイズとアラインメントが使われているときだけ思った通りに動きます。

```
>>> pack('llh0l', 1, 2, 3)
b'\x00\x00\x00\x01\x00\x00\x00\x02\x00\x03\x00\x00'
```

私の環境では以下のようになった。

```python
import struct
print(' llh0l', struct.pack('llh0l', 1, 2, 3))
print('>llh0l', struct.pack('>llh0l', 1, 2, 3))
print('<llh0l', struct.pack('<llh0l', 1, 2, 3))
print('@llh0l', struct.pack('@llh0l', 1, 2, 3))
```
```sh
$ python 3.py 
 llh0l b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'
>llh0l b'\x00\x00\x00\x01\x00\x00\x00\x02\x00\x03'
<llh0l b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00'
@llh0l b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'
```

`llh0l`だとマシン固有のエンディアンになる。私のマシンはリトルエンディアン。対してPython文書の例にあるマシンはビッグエンディアン。同じフォーマット`llh0l`だが結果が違う。

結果が変わると困る場合がある。たとえばPNGなど何らかのバイナリデータ形式の場合、エンディアンも規格で決っているはずなのでマシン固有(native)ではなく規格に合わせて明示すべき。

