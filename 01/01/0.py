import struct

#Unicode文字列をbytesに変換する
def U2B(unistr, maxlen):
    bytstr = unistr.encode()
    print(unistr, bytstr)
    len_diff = maxlen - len(bytstr)
    if len_diff < 0: raise Exception(f'最大バイト長を超えています。:unistr={unistr}, maxlen={maxlen}, len(bytstr)={len(bytstr)}, bytstr={bytstr}')
    else: return bytstr + struct.pack(f'{len_diff}B', *([0]*len_diff))
#    if maxlen < len(bytstr): raise Exception(f'最大バイト長を超えています。:unistr={unistr}, maxlen={maxlen}')
#    else: return bytstr + struct.pack(f'{maxlen - len(bytstr)}B', *([0]*(maxlen - len(bytstr))))
#    else: return bytstr + b''.join(['\x00' for i in range(maxlen - len(bytstr))])
#    else: return bytstr + ('\x00' * maxlen - len(bytstr))

studentStruct = struct.Struct('<10sHHb')
for record in [
        b'raymond   \x32\x12\x08\x01\x08',
        b'Taniguchi \x01\x00\x08\x01\x04', 
        b'Yamada    \x01\x01\x08\x01\x02',
        U2B('真田', 10) + b'\x01\x01\x08\x01\x02']:
        # b'真田      \x01\x01\x08\x01\x02' #SyntaxError: bytes can only contain ASCII literal characters.
    name, serialnum, school, gradelevel = studentStruct.unpack(record)
    print(f'name={name}, serialnum={serialnum}, school={school}, gradelevel={gradelevel}')

