def caesar_encrypt(plain_text,KEY):
    cipher_text = ''
    for l in plain_text:
        index = ord(l)
        index = (index + KEY) % 1114111
        cipher_text = cipher_text + chr(index)
    return cipher_text
def caesar_decrypt(cipher_text,KEY):
    plain_text = ''
    for l in cipher_text:
        index = ord(l)
        index = (index - KEY) % 1114111
        plain_text = plain_text + chr(index)
    return plain_text
if __name__ == '__main__':
    message = 'Welcome to my Cryptography class'
    KEY=3
    encrypted_message = caesar_encrypt(message,KEY)
    print(encrypted_message)
    print(caesar_decrypt(encrypted_message,KEY))