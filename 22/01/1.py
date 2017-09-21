from types import DynamicClassAttribute

# Metaclass
class Funny(type):
    def __getattr__(self, value):
        print('search in meta')
        # Normally you would implement here some ifs/elifs or a lookup in a dictionary
        # but I'll just return the attribute
        return Funny.dynprop
    # Metaclasses dynprop:
    dynprop = 'Meta'

class Fun(metaclass=Funny):
    def __init__(self, value):
        self._dynprop = value
    @DynamicClassAttribute
    def dynprop(self):
        return self._dynprop

print('-------クラス変数---------')
print(Fun.dynprop)#Meta
print('-------インスタンス変数---------')
fun = Fun('Not-Meta')
print(fun)
print(fun.dynprop)#Not-Meta
