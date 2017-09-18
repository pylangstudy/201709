import weakref
class Object: pass
def callback(x, y, z):
    print("CALLBACK")
    return x + y + z
obj = Object()
f = weakref.finalize(obj, callback, 1, 2, z=3)
f_dead = f.detach()
newobj, func, args, kwargs = f_dead
assert not f.alive
assert newobj is obj
assert func(*args, **kwargs) == 6 #ファイナライザ実行する
print('del直前')
del obj #ファイナライザ実行されない
