import weakref
class Object: pass
kenny = Object()
weakref.finalize(kenny, print, "You killed Kenny!")  
del kenny
