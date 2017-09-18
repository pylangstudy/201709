import weakref
class Object: pass
def callback(x, y, z):
    print(f"CALLBACK: {x + y + z}")
obj = Object()
f1 = weakref.finalize(obj, callback, 1, 2, z=3)
f2 = weakref.finalize(obj, callback, *[4, 5, 6])
f3 = weakref.finalize(obj, callback, **{'x':7, 'y':8, 'z':9})
del obj
print('プログラム終了')
