import weakref
import csv
import collections
from ConstMeta import ConstMeta

class Pool(metaclass=ConstMeta):
    def __new__(cls):
        cls.__Pool = {}
        cls.__WeakPool = weakref.WeakValueDictionary(cls.__Pool)
#        return super().__new__(cls)
#        print(cls.__Pool)
#        print(cls.__WeakPool, dict(cls.__WeakPool))
        
    @classmethod
    def Get(cls, _id):
        if _id in cls.__WeakPool: return cls.__WeakPool[_id]
        else:
            print('ファイル読込。')
            target = cls.__Read(_id)
            if None is target: raise ValueError('指定したidのデータが存在しませんでした。: _id={_id}')
            cls.__Pool[target.Id] = target
            cls.__WeakPool[target.Id] = cls.__Pool[target.Id]
#            print(cls.__Pool)
#            print(cls.__WeakPool, dict(cls.__WeakPool))
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
#            print(header)
            Human = collections.namedtuple('Humans', header)
            for row in reader:
                if 0 == len(row): continue
                human = cls.__ConvertType('Human', header, row)
#                print(human.Id, human)
                if int(row[0]) == human.Id: return human
                """
#                h = cls.__ConvertType(row)
                print(row)
                human = Human(*cls.__ConvertType(row))
                print(row)
                if row[0] == human.Id: return human
                """
        return None
    
    @classmethod
    def __ConvertType(cls, name, header, row):
        #http://www.freia.jp/taka/blog/734/
        RowType = type(name, (object,), dict(zip(header, row)))
        i = RowType()
        i.Id = int(i.Id)
        i.Age = int(i.Age)
        return i
        """
        row[0] = int(row[0])
        row[2] = int(row[2])
        print(row)
        return row
        """
        """
        h = ','.split(row)
        h[0] = int(h[0])
        h[2] = int(h[2])
        return h
        """


if __name__ == '__main__':
    h0 = Pool.Get(0)
    print(h0.Id, h0.Name, h0.Age, h0)
    h0 = Pool.Get(0)
    print(h0.Id, h0.Name, h0.Age, h0)

    del h0
#    print(h0.Id, h0.Name, h0.Age, h0)#NameError: name 'h0' is not defined
    h0 = Pool.Get(0)
    print(h0.Id, h0.Name, h0.Age, h0)

    Pool.Release(0)
    print(h0.Id, h0.Name, h0.Age, h0)

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
    
