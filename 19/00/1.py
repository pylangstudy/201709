import weakref
class Object: pass
def callback(x, y, z):
    print("CALLBACK")
    return x + y + z
obj = Object()
f = weakref.finalize(obj, callback, 1, 2, z=3)
assert f.alive
assert f() == 6
assert not f.alive
f()                     # callback not called because finalizer dead
del obj                 # callback not called because finalizer dead
