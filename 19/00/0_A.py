import weakref
class Object:
    def __del__(self): print("You killed Kenny!")    
kenny = Object()
del kenny
print()

class Object2(Object):
    def __del__(self):
        super().__del__()
        print("削除した！")
kenny = Object2()
del kenny

