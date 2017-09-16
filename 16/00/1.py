#!python3.6
#coding:utf-8
import array
a = array.array('h')
print(a)
print('----- append, byteswap -----')
a.append(256)
print(f'{a[0]:3d} {a[0]:#x}')
a.byteswap()
print(f'{a[0]:3d} {a[0]:#x}')
print('----- count -----', a.count(1))
a.extend([2,3])
print('----- extend -----', a)
a = array.array('b', b'\x01')
a.frombytes(b'\x0F')
print('----- frombytes -----', a)
#print('----- fromfile -----', a)
a = array.array('h')
a.fromlist([4,5])
print('----- fromlist -----', a)
#a.fromunicode('6')#ValueError: fromunicode() may only be called on unicode type arrays
#a.fromunicode(u'6')#ValueError: fromunicode() may only be called on unicode type arrays
#a.fromunicode(array.array('u', '6'))#TypeError: fromunicode() argument must be str, not array.array
a = array.array('u', 'A')
a.fromunicode('BC')
print('----- fromunicode -----', a)
print('----- index -----', a.index('C'))
a.insert(1, 'a')
print('----- insert -----', a)
print('----- pop -----', a.pop(1), a)
a.remove('A')
print('----- remove -----', a)
print('----- tobytes -----', a.tobytes())
#tofile()
print('----- tolist -----', a.tolist())
print('----- tostring -----', a.tostring())
print('----- tounicode -----', a.tounicode())

