from Crypto.Cipher import DES
import binascii
import time


plaintext = 'niceword'


start = time.time()

key = "00004000" # key should be 8 characters.

key = key.encode('utf-8')


# create a DES instance

des = DES.new(key, DES.MODE_ECB)


# encrypt the plaintext

encrypted_text = des.encrypt(plaintext.encode('utf-8')) # encryption

print("The cipher text: ", encrypted_text.hex())
ciphertext_hex = "f912c5dcf6719e7d"  # DES Ciphertext
encrypted_text = binascii.unhexlify(ciphertext_hex)  # Convert hex to bytes
# print(type(encrypted_text))

end = time.time()

print("Time consumption of encryption process", end - start, " Second")


#decrypt the cipher text.

plain_text = des.decrypt(encrypted_text).decode().rstrip('@') # decryption

print("The plain text: ", plain_text)