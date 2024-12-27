def mixColumns(a, b, c, d, a1, b1, c1, d1):
    printHex(gmul(a, a1) ^ gmul(b, b1) ^ gmul(c, c1) ^ gmul(d, d1))
    print()

def gmul(a, b):
    if b == 1:
        return a
    tmp = (a << 1) & 0xff
    if b == 2:
        return tmp if a < 128 else tmp ^ 0x1b
    if b == 3:
        return gmul(a, 2) ^ a

def printHex(val):
    return print('{:02x}'.format(val), end=' ')


#Hex goes down
#Dec goes across
# example from question
mixColumns(0x2d, 0x6f, 0x9a, 0xb1, 2, 2, 2, 2) # 0x22 0x77 0x00 0x55 = 34 119 0 85
