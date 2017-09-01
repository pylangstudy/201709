import struct
print(' llh0l', struct.pack('llh0l', 1, 2, 3))
print('>llh0l', struct.pack('>llh0l', 1, 2, 3))
print('<llh0l', struct.pack('<llh0l', 1, 2, 3))
print('@llh0l', struct.pack('@llh0l', 1, 2, 3))
