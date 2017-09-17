import gc
from pprint import pprint
import weakref
from Test_CircularReference import Graph, demo, collect_and_show_garbage

gc.set_debug(gc.DEBUG_LEAK)

print('Setting up the cycle')
print()
demo(Graph)

print()
print('Breaking the cycle and cleaning up garbage')
print()
gc.garbage[0].set_next(None)#IndexError: list index out of range
while gc.garbage:
    del gc.garbage[0]
print
collect_and_show_garbage()
