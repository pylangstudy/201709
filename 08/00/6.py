import collections
class Counter:
    def __init__(self):
        self.__values = []
        self.IsSortByKey = False

    def count(self, key):
        if None is key or 0 == len(key.strip()): return
        i = self.__GetIndex(key)
        if -1 == i:
            self.__values.append([key, 1])
            self.sort()
        else: self.__values[i][1] += 1

    def __GetIndex(self, key):
        for i in range(len(self.__values)):
            if key == self.__values[i][0]: return i
        return -1

    def sort(self, isSortByKey=None):
        if None is isSortByKey: isSortByKey = self.IsSortByKey
        if isSortByKey: self.__values.sort(key=lambda x: x[0])
        else: self.__values.sort(key=lambda x: x[1], reverse=True)

    def get(self, key):
        i = self.__GetIndex(key)
        if -1 == i: return None
        else: return self.__values[i][1]

    @property
    def Counts(self):
        Counts = collections.namedtuple('Counts', [v[0] for v in self.__values])
        return Counts(**dict(self.__values))


if __name__ == '__main__':
    c = Counter()
    c.count('a')
    c.count('a')
    c.count('A')
    c.count('a')
    for v in 'a A a a'.split(): c.count(v)
    for v in 'a\nA\na\na'.split('\n'): c.count(v)
    for v in ['a','A','a','a']: c.count(v)

    #カウントを取得する
    print(c.Counts)
    print(c.Counts.a)
    print(c.Counts.A)
#    print(c.Counts.B)#AttributeError: 'Counts' object has no attribute 'B'

    c.sort(True)#キー名でソートする。
    print(c.Counts)
    c.sort()#カウント値でソートする。
    print(c.Counts)
    
    #キー別に取得する
    print(c.get('a'))
    print(c.get('A'))
    print(c.get('B'))#None `c.Counts.B`のときと挙動が異なる。統一性がない。
    
    # 以下の不足を解消した
    # * ソートがない（ソートキー＝キー名 or カウント値）
    # * 代入を禁止できない
    # 以下の不満がある
    # * `c.get('key')` でなく `c['key']` で参照したい。ただしsetは禁止したい。存在しない時はNoneを返したい。
    # * 一部挙動に統一性がない（`c.Counts.B`と`c.get('B')`で存在しないときの応答が異なる）
