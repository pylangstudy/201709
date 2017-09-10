from collections import namedtuple
Employee = namedtuple('Employee', 'name,age')
print(Employee._make(['Yamada',10]))
