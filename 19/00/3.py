import weakref
class Object: pass
def callback(x, y, z):
    print("CALLBACK")
    return x + y + z
obj = Object()
f = weakref.finalize(obj, callback, 1, 2, z=3)
print('プログラム終了')

