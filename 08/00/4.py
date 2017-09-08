import collections
class Counter:
    def __init__(self): self.__value = 0
    def count(self): self.__value += 1
    @property
    def Value(self): return self.__value


if __name__ == '__main__':
    c = Counter()
    print(c.Value)
    c.count()
    c.count()
    c.count()
    c.count()
    print(c.Value)
#    c.Value += 1#AttributeError: can't set attribute
#    c.Value = 1#AttributeError: can't set attribute

