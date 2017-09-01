import struct
from collections import namedtuple

#Unicode文字列をbytesに変換する
def U2B(unistr, maxlen):
    bytstr = unistr.encode()
    len_diff = maxlen - len(bytstr)
    if len_diff < 0: raise Exception(f'最大バイト長を超えています。:unistr={unistr}, maxlen={maxlen}, len(bytstr)={len(bytstr)}, bytstr={bytstr}')
    else: return bytstr + struct.pack(f'{len_diff}B', *([0]*len_diff))

maxlen = 10
studentStruct = struct.Struct(f'<{maxlen}sHHb')
studentTuple = namedtuple('Student', 'name serialnum school gradelevel')

for record in [
        b'raymond   \x32\x12\x08\x01\x08',
        b'Taniguchi \x01\x00\x08\x01\x04', 
        b'Yamada    \x01\x01\x08\x01\x02',
        U2B('真田', maxlen) + b'\x01\x01\x08\x01\x02']:
    s = studentTuple._make(studentStruct.unpack(record))
    print('name:', s.name.decode(), s.name)
    print('  serialnum :', s.serialnum)
    print('  school    :', s.school)
    print('  gradelevel:', s.gradelevel)
