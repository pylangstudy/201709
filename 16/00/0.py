import array
#types = ['b','B','u','h','H','i','I','l','L','q','Q','f','d']
types = list(array.typecodes)
type_values = [bytes(b'\xFF'), bytes(b'\xFF'), 'A', [(2**15)-1], [(2**16)-1], [(2**15)-1], [(2**16)-1], [(2**31)-1], [(2**32)-1], [(2**63)-1], [(2**64)-1], [1.2], [1.2]]
type_dic = zip(types, type_values)
for k,v in type_dic:
    a = array.array(k,v)
    print(a.typecode, a.itemsize, a)
    
    
