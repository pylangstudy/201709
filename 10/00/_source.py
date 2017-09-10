from collections import namedtuple
Employee = namedtuple('Employee', 'name,age')
e1 = Employee('Yamada',10)
print(e1)
print(e1._source)
#exec(e1._source)
