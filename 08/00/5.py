class Counter:
    def __init__(self):
        self.__values = {}
    def count(self, name):
        if name not in self.__values: self.__values[name] = 0
        self.__values[name] += 1
    @property
    def Values(self): return self.__values

if __name__ == '__main__':
    c = Counter()
    c.count('a')
    c.count('a')
    c.count('A')
    c.count('a')
    for v in 'a A a a'.split(): c.count(v)
    for v in 'a\nA\na\na'.split('\n'): c.count(v)
    for v in ['a','A','a','a']: c.count(v)
    print(c.Values)
    print(c.Values['a'])
    c.Values['a'] = 0
    print(c.Values)
    # 以下の不足がある
    # * ソートがない（ソートキー＝キー名 or カウント値）
    # * 代入を禁止できない
