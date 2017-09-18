import weakref

class ExtendedRef(weakref.ref):
    def __init__(self, ob, callback=None, **annotations):
        super(ExtendedRef, self).__init__(ob, callback)
        self.__counter = 0
        for k, v in annotations.items():
            setattr(self, k, v)

    def __call__(self):
        """Return a pair containing the referent and the number of
        times the reference has been called.
        """
        ob = super(ExtendedRef, self).__call__()
        if ob is not None:
            self.__counter += 1
            ob = (ob, self.__counter)
        return ob

class Object: pass
o = Object()
r = ExtendedRef(o)

# r()で参照した回数を__counterにインクリメントする
print(r._ExtendedRef__counter)
r()
print(r._ExtendedRef__counter)
r()
print(r._ExtendedRef__counter)

# 参照が死んでいるならインクリメントしない
del o
r()
print(r._ExtendedRef__counter)

