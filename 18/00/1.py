import weakref

class Object:
    def __del__(self): print('今まさに死亡中…')
def is_life(r:weakref.ref):
    if r() is not None:
        print('まだ生きてる！')
    else:
        print('もう死んでる（泣）')

#o = object()#TypeError: cannot create weak reference to 'object' object
o = Object()
r = weakref.ref(o)
is_life(r)
del o
is_life(r)

