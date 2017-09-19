import types
import abc
Object = types.prepare_class('Object', (object,), {})
print(Object)#(<class 'type'>, {}, {})

Human = types.prepare_class('Human', (object,), None)
print(Human)#(<class 'type'>, {}, {})

Human = types.prepare_class('Human', (object,), {'metaclass': abc.ABCMeta})
print(Human)#(<class 'abc.ABCMeta'>, {}, {})

#types()
Human = type('Human', (object,), {'name':'', 'age':0})
print(Human)

