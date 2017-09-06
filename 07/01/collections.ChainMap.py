import collections

cm = collections.ChainMap()
print(cm.maps)
print(cm.new_child({'a':'A'}))#インスタンスに変更なし
print(cm.maps)

print(cm.maps[0].update({'b':'B'}))#更新
print(cm.maps.append({'c':'C'}))#追加
print(cm.maps.append({'d':'D'}))
print(cm.maps)

print(cm.parents)#最初の項目を飛ばす
