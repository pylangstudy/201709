import struct
print('----- tuple -----')
record = b'raymond   \x32\x12\x08\x01\x08'
name, serialnum, school, gradelevel = struct.unpack('<10sHHb', record)
print(f'name={name}, serialnum={serialnum}, school={school}, gradelevel={gradelevel}')

print('----- namedtuple -----')
from collections import namedtuple
Student = namedtuple('Student', 'name serialnum school gradelevel')
s = Student._make(struct.unpack('<10sHHb', record))
print(s)
print(s.name)
print(s.serialnum)
print(s.school)
print(s.gradelevel)

