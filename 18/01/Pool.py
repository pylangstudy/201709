import weakref
import csv

class ConstMeta(type):
    class ConstError(TypeError): pass        
    def __init__(self, name, bases, dict):
        super(ConstMeta, self).__init__(name, bases, dict)
        import sys
        sys.modules[name]=self()#ConstMetaを継承したクラスのモジュールに、そのクラスのインスタンスを代入する        
    def __setattr__(self, name, value):
        if name in self.__dict__.keys(): raise self.ConstError('readonly。再代入禁止です。')
        super(ConstMeta, self).__setattr__(name, value)

class Pool:
    def __new__(cls):
        cls.__Pool = {}
        cls.__WeakPool = weakref.WeakValueDictionary(cls.__Pool)
        print(dir(cls))
        return super().__new__(cls)
        
    @classmethod
    def Get(cls, _id):
        if _id in cls.__WeakPool: return cls.__WeakPool[_id]
        else:
            target = cls.__Read(_id)
            if None is target: raise ValueError('指定したidのデータが存在しませんでした。: _id={_id}')
            cls.__Pool[target.Id] = target
            return cls.__WeakPool[_id]
    
    @classmethod
    def Release(cls, _id):
        if _id in cls.__Pool: del cls.__Pool[_id]

    @classmethod
    def __Read(cls, _id):
        with csv.read('Humans.csv') as f:
            reader = csv.reader(f)
            header = next(reader)  # ヘッダーを読み飛ばしたい時
            print(header)
            Human = collections.namedtuple('Humans', header)
            for row in reader:
                if 0 == len(row.strip()): continue
#                print row          # 1行づつ取得できる
                if row[0] == _id: return Human(','.split(row))
        return None


if __name__ == '__main__':
    h0 = Pool.Get(0)
    print(h0)
