import tempfile
import shutil
class TempDir:
    def __init__(self):
        self.name = tempfile.mkdtemp()
        print(self.name)

    def remove(self):
        if self.name is not None:
            shutil.rmtree(self.name)
            self.name = None
            print('削除した！')

    @property
    def removed(self):
        return self.name is None

    def __del__(self):
        self.remove()

td = TempDir()
del td
print('プログラム終了')
