# UNFINISHED
import binascii
def strtobin(string):
    return bin(int(binascii.hexlify(string.encode()), 16)) 
def bintostr(binary):
    n = int(binary, 2)
    return str(binascii.unhexlify('%x' % n))



plaintext="Hello World"
key="Iamhere"
# XOR can be simplified as a!=b

plaintext_bin=str(strtobin(plaintext))
plaintext_bin=plaintext_bin[3:]
key_bin=str(strtobin(key))
key_bin=key_bin[3:]

print("Plaintext is: "+plaintext+"\nPlaintext in binary is: "+plaintext_bin)
print("Key is: "+key+"\nKey in binary is: "+key_bin)


output_encoded =''
i_bin=0
i=0
while i<len(plaintext_bin):
    i=int(i)
    if len(key_bin) < i_bin:
        i_bin+=1
    else:
        i_bin=0
    if bin(int(plaintext_bin[i]))!=bin(int(key_bin[i_bin])):
        output_encoded=output_encoded+"1"
    else:
        output_encoded=output_encoded+"0"
    i+=1
print("\n\n\n\n\n\nEncoded:")
print(output_encoded)
print(bintostr(output_encoded))
i_bin=0
i=0
output_decoded=''
while i<len(output_encoded):
    i=int(i)
    if len(key_bin) < i_bin:
        i_bin+=1
    else:
        i_bin=0
    if bin(int(output_encoded[i]))!=bin(int(key_bin[i_bin])):
        output_decoded=output_decoded+"1"
    else:
        output_decoded=output_decoded+"0"
    i+=1
print("\n\n\nDecoded:")
print(output_decoded)
print(bintostr(output_decoded))