import binascii


def encrypt(plaintext, key):
    plainhex = binascii.hexlify(plaintext.encode())
    plainbin = bin(int(plainhex, 16))[2:].zfill(8 * ((len(plainhex) + 1) // 2))
    keyhex = binascii.hexlify(key.encode())
    keybin = bin(int(keyhex, 16))[2:].zfill(8 * ((len(keyhex) + 1) // 2))
    
    lefttext = plainbin[:32]
    righttext = plainbin[32:]
    keyleft = keybin[:32]
    keyright = keybin[32:]
    
    # Two rounds of encryption
    for i in range(2):
        if i % 2 != 0:
            lefttext, righttext, keyleft, keyright = leftroundencrypt(lefttext, righttext, keyleft, keyright)
        else:
            lefttext, righttext, keyleft, keyright = rightroundencrypt(lefttext, righttext, keyleft, keyright)

    cipherhex = binary_to_hex(lefttext + righttext)
    return cipherhex


def leftroundencrypt(plainl, plainr, keyl, keyr):
    right = ""
    for i in range(len(plainr)):
        right = right + str(int(plainr[i]) ^ int(keyl[i]))
    out = ""
    for i in range(len(right)):
        out = out + str(int(right[i]) ^ int(plainl[i]))
    keyl = keyl[4:] + keyl[:4]
    return plainr, out, keyl, keyr


def rightroundencrypt(plainl, plainr, keyl, keyr):
    right = ""
    for i in range(len(plainr)):
        right = right + str(int(plainr[i]) ^ int(keyr[i]))
    out = ""
    for i in range(len(right)):
        out = out + str(int(right[i]) ^ int(plainl[i]))
    keyr = keyr[4:] + keyr[:4]
    return plainr, out, keyl, keyr


def decrypt(ciphertext, key):
    cipherhex = hex_to_binary(ciphertext)
    keyhex = binascii.hexlify(key.encode())
    keybin = bin(int(keyhex, 16))[2:].zfill(8 * ((len(keyhex) + 1) // 2))
    lefttext = cipherhex[:32]
    righttext = cipherhex[32:]
    keyleft = keybin[:32]
    keyright = keybin[32:]

    # Reverse the two rounds of encryption
    for i in range(1, -1, -1):
        if i % 2 != 0:
            lefttext, righttext, keyleft, keyright = reverse_leftroundencrypt(lefttext, righttext, keyleft, keyright)
        else:
            lefttext, righttext, keyleft, keyright = reverse_rightroundencrypt(lefttext, righttext, keyleft, keyright)

    plainbin = lefttext + righttext
    plainhex = hex(int(plainbin, 2))[2:].zfill(len(plainbin) // 4)
    plaintext = binascii.unhexlify(plainhex).decode()
    
    return plaintext


def reverse_leftroundencrypt(plainl, plainr, keyl, keyr):
    # Reverse key rotation
    keyl = keyl[-4:] + keyl[:-4]
    
    right = ""
    for i in range(len(plainr)):
        right = right + str(int(plainr[i]) ^ int(plainl[i]))
        
    out = ""
    for i in range(len(right)):
        out = out + str(int(right[i]) ^ int(keyl[i]))
        
    return out, plainl, keyl, keyr


def reverse_rightroundencrypt(plainl, plainr, keyl, keyr):
    # Reverse key rotation
    keyr = keyr[-4:] + keyr[:-4]
    
    right = ""
    for i in range(len(plainr)):
        right = right + str(int(plainr[i]) ^ int(plainl[i]))
        
    out = ""
    for i in range(len(right)):
        out = out + str(int(right[i]) ^ int(keyr[i]))
        
    return out, plainl, keyl, keyr


def binary_to_hex(binary_str):
    # Convert binary string to an integer, then to hexadecimal
    hex_str = hex(int(binary_str, 2))[2:]  # Remove '0x' prefix
    return hex_str


def hex_to_binary(hex_str):
    # Convert hexadecimal string to an integer, then to binary
    binary_str = bin(int(hex_str, 16))[2:]  # Remove '0b' prefix
    return binary_str


def main():
    count = 0
    input_file = open("Cryptography456HW/plaintext.txt", "r")
    output_file = open("Cryptography456HW/ciphertext.txt", "a")
    key = "12345678"
    
    for line in input_file:
        count += 1
        if count % 10000 == 0:
            print(count)
        encrypted = encrypt(line[:8], key)
        output_file.write(encrypted + "\n")

    input_file.close()
    output_file.close()


main()
