# [8.8.2. 使用例](https://docs.python.jp/3/library/weakref.html#example)

< [8.8. weakref — 弱参照](https://docs.python.jp/3/library/weakref.html) < [8. データ型](https://docs.python.jp/3/library/datatypes.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/weakref.py](https://github.com/python/cpython/tree/3.6/Lib/weakref.py)

メモリ管理に関わる重要な項目。

## 概要

の前に、[8.8.2. 使用例](https://docs.python.jp/3/library/weakref.html#example)のタイトルに目的語がないので補足。この章は`weakref.WeakValueDictionary`クラスの使用例である。

> この簡単な例では、アプリケーションが以前に参照したオブジェクトを取り出すためにオブジェクトIDを利用する方法を示します。オブジェクトに生きたままであることを強制することなく、オブジェクトの IDを他のデータ構造の中で使うことができ、必要に応じてIDからオブジェクトを取り出せます。

```python
import weakref

_id2obj_dict = weakref.WeakValueDictionary()

def remember(obj):
    oid = id(obj)
    _id2obj_dict[oid] = obj
    return oid

def id2obj(oid):
    return _id2obj_dict[oid]
```

## 削除される経緯の比較

`WeakValueDictionary`と`dict`型でどのような違いがあるのか確認した。

```python
import weakref

print('----- weakref.WeakValueDictionary -----')
_id2obj_dict = weakref.WeakValueDictionary()

def remember(obj):
    oid = id(obj)
    _id2obj_dict[oid] = obj
    return oid

def id2obj(oid):
    return _id2obj_dict[oid]

class Object:
    def __del__(self): print('オブジェクトは死んだのだ…')
print(dict(_id2obj_dict))
o1 = Object()
o1_id = remember(o1)
print(dict(_id2obj_dict))
del o1
print(dict(_id2obj_dict))
#WeakValueDictionaryは元オブジェクトを削除すれば辞書側も消える。dict型は辞書で参照している限り削除されない。


print('----- dict clear()にて削除 -----')
d = dict()
print(d)
o1 = Object()
d.update({id(o1): o1})
print(d)
del o1
print(d)
d.clear()
print(d)


print('----- dict 放置。プログラム終了後に自動削除（終了せねば解放されない。メモリリーク） -----')
d = dict()
print(d)
o1 = Object()
d.update({id(o1): o1})
print(d)
del o1
print(d)
print('***** プログラム終了 *****')
```

```sh
 $ python 0.py 
----- weakref.WeakValueDictionary -----
{}
{3070924044: <__main__.Object object at 0xb70a950c>}
オブジェクトは死んだのだ…
{}
----- dict clear()にて削除 -----
{}
{3070924044: <__main__.Object object at 0xb70a950c>}
{3070924044: <__main__.Object object at 0xb70a950c>}
オブジェクトは死んだのだ…
{}
----- dict 放置。プログラム終了後に自動削除（終了せねば解放されない。メモリリーク） -----
{}
{3070924044: <__main__.Object object at 0xb70a950c>}
{3070924044: <__main__.Object object at 0xb70a950c>}
***** プログラム終了 *****
オブジェクトは死んだのだ…
```

できるかぎり弱参照したほうがメモリリークの危険を避けられる。

## 使えない型

int型、namedtuple型を弱参照にしようとしたが、エラーが出て使えなかった。

```sh
TypeError: cannot create weak reference to 'int' object
TypeError: cannot create weak reference to 'Humans' object
```
```python
import weakref
w = weakref.WeakValueDictionary()
v = 100
w[id(v)] = v #TypeError: cannot create weak reference to 'int' object
print(dict(w))

import collections
Human = collections.namedtuple('Humans', 'Id,Name,Age')
w = weakref.WeakValueDictionary()
w['a'] = Human(0, 'Yamada', 11)#TypeError: cannot create weak reference to 'Humans' object
print(dict(w))
```

よくわからなかったが以下参照。今の所ユーザ定義クラスでしか使えることを確認できていない。

* http://qiita.com/pashango2/items/fb1e5e79589279c5a861
* http://qiita.com/yoichi22/items/ebf6ab3c6de26ddcc09a


## ユースケース

遅延読込。

data.csv
```csv
id,name,age
0,Yamada,11
1,Tanaka,22
2,Sanada,33
```

Pool.py
```python
import weakref
class Pool:
    __Pool = weakref.WeakValueDictionary()
    @classmethod
    def Get(cls, _id):
    @classmethod
    def Release(cls, _id):
```

* Get()
    * メモリプールに存在する
        * 取得対象のインスタンスを返す
    * メモリプールに存在しない
        * メモリプールに読み込む
            * ファイルから対象のみを読込
        * 取得対象のインスタンスを返す
* Release()
    * メモリプールに存在しない
        * 何もしない
    * メモリプールに存在する
        * 解放対象を削除する（Getで他の変数に代入されていても、それは弱参照にすぎない。ここで大本を削除すれば弱参照しているインスタンスは削除される）
        
みたいなことをしたかった。

/example/Pool.py
```python
import weakref
import csv
import collections
from ConstMeta import ConstMeta

class Pool(metaclass=ConstMeta):
    def __new__(cls):
        cls.__Pool = {}
        cls.__WeakPool = weakref.WeakValueDictionary(cls.__Pool)
        
    @classmethod
    def Get(cls, _id):
        if _id in cls.__WeakPool: return cls.__WeakPool[_id]
        else:
            print('ファイル読込。')
            target = cls.__Read(_id)
            if None is target: raise ValueError('指定したidのデータが存在しませんでした。: _id={_id}')
            cls.__Pool[target.Id] = target
            cls.__WeakPool[target.Id] = cls.__Pool[target.Id]
            return cls.__WeakPool[_id]
    
    @classmethod
    def Release(cls, _id):
        if _id in cls.__Pool: del cls.__Pool[_id]
        else: print('存在しないIDです。')
        
    @classmethod
    def __Read(cls, _id):
        with open('Humans.csv') as f:
            reader = csv.reader(f)
            header = next(reader)  # ヘッダーを読み飛ばしたい時
            Human = collections.namedtuple('Humans', header)
            for row in reader:
                if 0 == len(row): continue
                human = cls.__ConvertType('Human', header, row)
                if int(row[0]) == human.Id: return human
        return None
    
    @classmethod
    def __ConvertType(cls, name, header, row):
        #http://www.freia.jp/taka/blog/734/
        RowType = type(name, (object,), dict(zip(header, row)))
        i = RowType()
        i.Id = int(i.Id)
        i.Age = int(i.Age)
        return i


if __name__ == '__main__':
    # ローカル変数とPoolクラス内変数の両方の参照を削除しないと消えない。（ローカル変数側を常に弱参照したかったのだが…）
    del h0
    Pool.Release(0)
    h0 = Pool.Get(0)
    print(h0.Id, h0.Name, h0.Age, h0)
    del h0
    Pool.Release(0)
    
    #こうするとGet,Releaseのみで管理できる。ローカル変数に代入しないことが重要。（ただしインスタンスに別名が付与できず可読性が低い…）
    print('----- Get, Release のみで管理 -----')
    print(Pool.Get(0).Id, Pool.Get(0).Name, Pool.Get(0).Age, Pool.Get(0))
    print(Pool.Get(0).Id, Pool.Get(0).Name, Pool.Get(0).Age, Pool.Get(0))
    print(Pool.Get(0).Id, Pool.Get(0).Name, Pool.Get(0).Age, Pool.Get(0))
    Pool.Release(0)
    print(Pool.Get(0).Id, Pool.Get(0).Name, Pool.Get(0).Age, Pool.Get(0))
```

### 設計できなかった

本当は以下のようにしたかったのだが…。ローカル変数に代入してしまうと、それも`del`せねばならない。面倒。（すぐに終了する関数内ローカル変数なら問題ない）

```python
yamada = Pool.Get(0)    # 取得
yamada.Name             # 参照
Pool.Release(0)         # 解放
```

```python
yamada = Pool.Get(0)    # 取得
yamada.Name             # 参照
del yamada              # 解放
```

IdでなくNameをキーにすれば少し改善するか？
```python
Pool.Get('Yamada').Name # 取得、参照
Pool.Release('Yamada')  # 解放
```

でも別名には他の名前にしたい時もあるかもしれない。

```python
雇用主 = Pool.Get('Yamada')
奴隷 = Pool.Get('Tanaka')
```

こうしてしまった場合、ローカル変数とPool側変数の両方を`del`せねばならない。

```python
del 雇用主
Pool.Release('Yamada')

del 奴隷
Pool.Release('Tanaka')
```

しかし、雇用主とYamada、奴隷とTanaka、がそれぞれ同じインスタンスを指しているという関連付けがないのでミスが生じうる。

奴隷を示すインスタンスを削除しよう思い、間違って以下のようにしたとする。この場合、どのインスタンスも削除されない。

```python
del 奴隷
Pool.Release('Yamada')
```

2回も削除するのが面倒なだけでなく、関連付けも意識せねばならない。

こういう場合、どう実装するのがいいのか。わからなかった。

