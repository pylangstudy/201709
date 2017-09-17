import gc
from pprint import pprint
import weakref

class Graph(object):
    def __init__(self, name):
        self.name = name
        self.other = None
    def set_next(self, other):
        print('%s.set_next(%s (%s))' % (self.name, other, type(other)))
        self.other = other
    def all_nodes(self):
        "Generate the nodes in the graph sequence."
        yield self
        n = self.other
        while n and n.name != self.name:
            yield n
            n = n.other
        if n is self:
            yield n
        return
    def __str__(self):
        return '->'.join([n.name for n in self.all_nodes()])
    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.name)
    def __del__(self):
        print('(Deleting %s)' % self.name)
        self.set_next(None)

class WeakGraph(Graph):
    def set_next(self, other):
        if other is not None:
            # 弱参照をもつ他の参照に置き換えるべきかを調べる
            if self in other.all_nodes():
                other = weakref.proxy(other)
        super(WeakGraph, self).set_next(other)
        return

def collect_and_show_garbage():
    "Show what garbage is present."
    print('Collecting...')
    n = gc.collect()
    print('Unreachable objects:', n)
    print('Garbage:', )
    pprint(gc.garbage)

def demo(graph_factory):
    print('Set up graph:')
    one = graph_factory('one')
    two = graph_factory('two')
    three = graph_factory('three')
    one.set_next(two)
    two.set_next(three)
    three.set_next(one)
    
    print()
    print('Graphs:')
    print(str(one))
    print(str(two))
    print(str(three))
    collect_and_show_garbage()

    print()
    three = None
    two = None
    print('After 2 references removed:')
    print(str(one))
    collect_and_show_garbage()

    print()
    print('Removing last reference:')
    one = None
    collect_and_show_garbage()

demo(WeakGraph)
# 以下のような循環参照になっている。
#┌→１→２→３→┐
#↑              ↓
#└───←───┘
# 2, 3を削除しても何一つ消えない。1が2を参照して、2が3を参照しているから。
# しかし、根本の1を削除するとすべて消える。
# 
# もし弱参照でなく通常の変数ならプログラム終了まで解放されずメモリリークとなる可能性がある。
# 削除したつもりでも循環参照ゆえ削除できないから。
