from collections import namedtuple
Employee = namedtuple('Employee', 'name,age')
e1 = Employee('Yamada',10)
print(e1)
print(e1._replace(age=22))#新しいインスタンスを返す。元インスタンスの変更ではない（tupleはimmutable(変更不可)）
print(e1)
