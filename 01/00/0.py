import struct
print('----- Endian=Native -----')
print(struct.pack('hhl', 1, 2, 3))
print(struct.unpack('hhl', b'\x00\x01\x00\x02\x00\x00\x00\x03'))
print(struct.calcsize('hhl'))

print('----- Endian=Little -----')
print(struct.pack('<hhl', 1, 2, 3))
print(struct.unpack('<hhl', b'\x00\x01\x00\x02\x00\x00\x00\x03'))
print(struct.calcsize('<hhl'))

print('----- Endian=Big -----')
print(struct.pack('>hhl', 1, 2, 3))
print(struct.unpack('>hhl', b'\x00\x01\x00\x02\x00\x00\x00\x03'))
print(struct.calcsize('>hhl'))

