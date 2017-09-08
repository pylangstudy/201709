import collections
class Counter:
    def __init__(self): self.__value = 0
    def count(self): self.__value += 1
    @property
    def Value(self): return self.__value
    # +c
    def __pos__(self): self.count()
    # c + other
    def __add__(self, other): return self.Value + self.__get(other)
    # c += element
    def __iadd__(self, element): self.__value += self.__get(element); return self
    def __get(self, v):
        if isinstance(v, int): return v
        elif isinstance(v, Counter): return v.Value
        else: raise Exception(f'intかCounter型のみ対応です。type(v):{type(v)}')

if __name__ == '__main__':
    c = Counter()
    print('-----', 'count()', '-----')
    print(c.Value)
    c.count()
    c.count()
    c.count()
    c.count()
    print(c.Value)
#    c.Value += 1#AttributeError: can't set attribute
#    c.Value = 1#AttributeError: can't set attribute

    #加算
    print('-----', 'c + 1, c + c', '-----')
    print(c + 100, c.Value)
    print(c + c, c.Value)
#    print(1 + c, c.Value)#TypeError: unsupported operand type(s) for +: 'int' and 'Counter'
    # c+1はできるが、1+cはできない。中途半端……

    #インクリメント略記
    print('-----', '+c', '-----')
    print(c.Value)
    +c
    print(c.Value)
    +c
    print(c.Value)
    #+cは本来の使い方と違う。正数化するのが本来の使い方。インクリメントではない。
    #C言語と統一するため`c++`にしたかったがPythonでは不可能……
#    c+#SyntaxError: invalid syntax
#    c++#SyntaxError: invalid syntax
    
    print('-----', 'c += 1, c += c', '-----')
    print(c.Value)
    c += 1
    print(c.Value)
    c += c
    print(c.Value)
    
