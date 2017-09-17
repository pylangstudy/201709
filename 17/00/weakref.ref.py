import weakref

class ExpensiveObject(object):
    def __del__(self): print('Deleting ... %s' % self)

obj = ExpensiveObject()
r = weakref.ref(obj)

print('obj:', obj)  # <__main__.ExpensiveObject object at 0xb710adac>
print('ref:', r)    # <weakref at 0xb70cb414; to 'ExpensiveObject' at 0xb710adac>
print('r():', r())  # <__main__.ExpensiveObject object at 0xb710adac>

del obj
print('Deleted obj !')
print('r():', r())  #None
print('ref:', r)    #<weakref at 0xb70cb414; dead>
print('obj:', obj)  #NameError: name 'obj' is not defined

