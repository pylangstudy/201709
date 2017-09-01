import struct
print('ci:', struct.calcsize('ci'), struct.pack('ci', b'*', 0x12131415))
print('ic:', struct.calcsize('ic'), struct.pack('ic', 0x12131415, b'*'))
