import tempfile
import shutil
import weakref
class TempDir:
    def __init__(self):
        self.name = tempfile.mkdtemp()
#        self._finalizer = weakref.finalize(self, shutil.rmtree, self.name)
        self._finalizer = weakref.finalize(self, self.remove)
        print(self.name)

    def remove(self):
        if self.name is not None:
            shutil.rmtree(self.name)
            self.name = None
            print('削除した！')
#    def remove(self):
#        self._finalizer()

    @property
    def removed(self):
        return not self._finalizer.alive

td = TempDir()
del td
print('プログラム終了')
