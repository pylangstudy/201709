import weakref, sys

class Object: pass
obj = Object()
def unloading_module():
    # implicit reference to the module globals from the function body
    global obj
    del obj
    print('unloading_module() !!')
weakref.finalize(sys.modules[__name__], unloading_module)
#del sys.modules[__name__]#実行されない。むしろ実行されたらまずい。
print('プログラム終了')
