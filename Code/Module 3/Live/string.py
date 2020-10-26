unic = "\N{LATIN SMALL LETTER O WITH DIAERESIS}"
print(unic)

b1 = b'\xd0\xb4\xd0\xb0'
b2 = b"\xd0\xb4\xd0\xb0"
b3 = b'''\xd0\xb4\xd0\xb0'''
bytes1 = b'hello'
print(b1, b2, b3, bytes1)

bts = bytearray(b'TEST')
bts[0] = 105
print(bts)