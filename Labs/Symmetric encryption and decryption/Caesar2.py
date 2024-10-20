letters = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ' # there is a space in front of letter A
KEY = 5
def caesar_encrypt(plain_text):
    cipher_text = ''
    plain_text = plain_text.upper()
    for l in plain_text:
        index = letters.find(l)
        index = (index + KEY) % len(letters)
        cipher_text = cipher_text + letters[index]
    return cipher_text
def caesar_decrypt(cipher_text):
    plain_text = ''
    for l in cipher_text:
        index = letters.find(l)
        index = (index - KEY) % len(letters)
        plain_text = plain_text + letters[index]
    return plain_text
if __name__ == '__main__':
    message = 'JKLMN'
    encrypted_message = caesar_encrypt(message)
    print(encrypted_message)
    print(caesar_decrypt(encrypted_message))