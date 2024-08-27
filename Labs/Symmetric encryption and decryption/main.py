# UNFINISHED
import binascii
def strtobin(string):
    return int(''.join(format(ord(x), 'b') for x in string))
def bintostr(binary):
    for i in range(binary):
        byte = 
        return ''.join([chr(int(i, 2)) for i in binary])



plaintext="Hello World"
key="Iamhere"
# XOR can be simplified as a!=b

plaintext_bin=str(strtobin(plaintext))
key_bin=str(strtobin(key))
print(plaintext_bin)
print(bintostr(plaintext_bin))
output =''
i_bin=0
print(plaintext_bin)
print(key_bin)
for i in plaintext_bin:
    i=int(i)
    if len(key_bin) < i_bin:
        i_bin+=1
    else:
        i_bin=0
    if bin(i)!=bin(int(key_bin[i_bin])):
        output=output+"1"
    else:
        output=output+"0"
print("\n\n\n\n\n\nEncoded:")
print(output)
print(bintostr(output))
for i in output:
    i=int(i)
    if len(key_bin) < i_bin:
        i_bin+=1
    else:
        i_bin=0
    if bin(i)!=bin(int(key_bin[i_bin])):
        output=output+"1"
    else:
        output=output+"0"
print("\n\n\n\n\n\nDecoded:")
print(output)
print(bintostr(output))