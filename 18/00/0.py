import weakref
class Object:
    pass
o = Object()
r = weakref.ref(o)
o2 = r()

print('o:', o)  #<__main__.Object object at 0xb70fcdcc>
print('r:', r)  #<weakref at 0xb70bd324; to 'Object' at 0xb70fcdcc>
print('o2:', o2)#<__main__.Object object at 0xb70fcdcc>
print('o is o2:', o is o2)

print('----- delete o. -----')
del o
#print('o:', o)     #NameError: name 'o' is not defined
print('r:', r)      #<weakref at 0xb70bd324; to 'Object' at 0xb70fcdcc>
print('o2:', o2)    #<__main__.Object object at 0xb70fcdcc>
print('r():', r())  #<__main__.Object object at 0xb7199e2c>
print('----- delete o2. -----')
del o2
print('r:', r)      #<weakref at 0xb70b3324; dead>
print('r():', r())  #None
#print('o2:', o2)#o2: NameError: name 'o2' is not defined

