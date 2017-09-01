import struct

studentStruct = struct.Struct('<10sHHb')
print('format', studentStruct.format)
print('size', studentStruct.size)#`s`は可変長なので0として無視されるらしい

