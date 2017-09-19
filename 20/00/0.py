import types
import abc
Object = types.new_class('Object', (object,), {}, lambda ns: print('ns:', ns))
o = Object()
print(o)

#第3引数に何を渡せばいいか不明！メンバ変数辞書じゃないの？
#https://docs.python.jp/3/library/types.html#dynamic-type-creation
# > 最初の3つの引数はクラス定義ヘッダーを構成する—クラス名、基底クラス (順番に)、キーワード引数 (例えば metaclass)—です。
#Human = types.new_class('Human', (object,), **{'name':'', 'age':0})#TypeError: new_class() got multiple values for argument 'name'
#Human = types.new_class('Human', (object,), {'name':'', 'age':0})#TypeError: __init_subclass__() takes no keyword arguments
#Human = types.new_class('Human', (object,), {'Name':''})#TypeError: __init_subclass__() takes no keyword arguments
#Human = types.new_class('Human', bases=(object,), kwds={'name':'', 'age':0}, exec_body=None)#TypeError: __init_subclass__() takes no keyword arguments

#「(例えば metaclass)」とあるのでクラスを入れてみたがエラー
#Paisonia = types.new_class('Paisonia', (object,), Human)#TypeError: 'type' object is not iterable
#p = Paisonia()
#print(p)

#a = types.new_class('Some', (object,), ['A','B'])#ValueError: dictionary update sequence element #0 has length 1; 2 is required

#Noneなら動作する
Human = types.new_class('Human', (object,), None)
print(Human())#<types.Human object at 0xb70a614c>
#GitHub検索で動作するコードを見つけた。
#https://github.com/search?utf8=%E2%9C%93&q=types.new_class+extension%3Apy&type=Code&ref=advsearch&l=&l=
#https://github.com/Alonsovau/sketches/blob/b3ec7284226ebb6aebe5fa644f0a04e0e2e99ff5/chapter9/st18.py
Human = types.new_class('Human', (object,), {'metaclass': abc.ABCMeta})
print(Human())#<abc.Human object at 0xb70a628c>
#キーワード引数のキーと値は上記しか認めないということか？仕様がわからない。Python文書に詳しい説明もコード例もない。
#ソースコードを見たほうが早い
#https://github.com/python/cpython/blob/3.6/Lib/types.py#L79

#types()ならできる
Human = type('Human', (object,), {'name':'', 'age':0})
print(Human)

