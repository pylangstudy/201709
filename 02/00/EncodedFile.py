import codecs

file_path = 'test_files/EncodedFile.txt'
data_enc = 'shift-jis'
file_enc = 'euc-jp'
ef = codecs.EncodedFile(file_path, data_enc, file_enc)
#ef = codecs.EncodedFile(file_path, codecs.lookup(data_enc), codecs.lookup(file_enc))#TypeError: lookup() argument must be str, not CodecInfo
print(type(ef))

data = '日本語'
print(data)
print('EncodedFile.encode():', ef.encode(data))
print('EncodedFile.decode():', ef.decode(ef.encode(data)[0]))
#ef.write(data)#TypeError: a bytes-like object is required, not 'str'
#ef.write(ef.encode(data)[0])#AttributeError: 'str' object has no attribute 'write'
#ef.write(ef.decode(ef.encode(data)[0])[0])#TypeError: a bytes-like object is required, not 'str'
#ef.write(b'\x93\xfa\x96{\x8c\xea')#AttributeError: 'str' object has no attribute 'write'
#print('EncodedFile.read():', ef.read(data))#TypeError: arg 1 must be an integer
#print('EncodedFile.read():', ef.read())#AttributeError: 'str' object has no attribute 'read'

