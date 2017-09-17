import weakref

class ExpensiveObject(object):
    def __init__(self, name): self.name = name
    def __del__(self): print('Deleting ... %s' % self)
#class ExpensiveObject(object):
#    def __del__(self): print('Deleting ... %s' % self)
def callback(reference): print('callback(', reference, ')')

obj = ExpensiveObject('MyName')
r = weakref.ref(obj, callback)
p = weakref.proxy(obj, callback)

print('obj:', obj)  # <__main__.ExpensiveObject object at 0xb710adac>
print('ref:', r)    # <weakref at 0xb70cb414; to 'ExpensiveObject' at 0xb710adac>
print('r():', r())  # <__main__.ExpensiveObject object at 0xb710adac>
print('p  :', p)  # <__main__.ExpensiveObject object at 0xb710adac>
print('obj.name:', obj.name)  # <__main__.ExpensiveObject object at 0xb710adac>
print('r().name:', r().name)  # <__main__.ExpensiveObject object at 0xb710adac>
print('p.name  :', p.name)  # <__main__.ExpensiveObject object at 0xb710adac>

del obj
print('Deleted obj !')
#print('p:', p)              #ReferenceError: weakly-referenced object no longer exists
#print('p.name:', p.name)    #ReferenceError: weakly-referenced object no longer exists
print('r():', r())  #None
#print('r().name:', r().name)  #AttributeError: 'NoneType' object has no attribute 'name'
print('ref:', r)    #<weakref at 0xb70cb414; dead>
#print('obj:', obj)  #NameError: name 'obj' is not defined
#print('obj.name:', obj.name)  #NameError: name 'obj' is not defined


