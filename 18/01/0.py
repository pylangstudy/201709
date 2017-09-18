import weakref

print('----- weakref.WeakValueDictionary -----')
_id2obj_dict = weakref.WeakValueDictionary()

def remember(obj):
    oid = id(obj)
    _id2obj_dict[oid] = obj
    return oid

def id2obj(oid):
    return _id2obj_dict[oid]

class Object:
    def __del__(self): print('オブジェクトは死んだのだ…')
print(dict(_id2obj_dict))
o1 = Object()
o1_id = remember(o1)
print(dict(_id2obj_dict))
del o1
print(dict(_id2obj_dict))
#WeakValueDictionaryは元オブジェクトを削除すれば辞書側も消える。dict型は辞書で参照している限り削除されない。


print('----- dict clear()にて削除 -----')
d = dict()
print(d)
o1 = Object()
d.update({id(o1): o1})
print(d)
del o1
print(d)
d.clear()
print(d)


print('----- dict 放置。プログラム終了後に自動削除（終了せねば解放されない。メモリリーク） -----')
d = dict()
print(d)
o1 = Object()
d.update({id(o1): o1})
print(d)
del o1
print(d)
print('***** プログラム終了 *****')

