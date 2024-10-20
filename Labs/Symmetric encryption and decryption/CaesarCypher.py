def caesar_decrypt(cipher_text,key):
    plain_text = ''
    print(cipher_text)
    for l in cipher_text:
        index = (ord(l) - key)
        index=max(index,32)
        plain_text = plain_text + chr(index)
    return plain_text
if __name__ == '__main__':
    input="ÕÞÓâéàäÙßÞ Ùã åãÕÔ äß àâßäÕÓä ÔÑäÑ ÖâßÝ ÒÕÙÞ× ãäßÜÕÞ ÓØÑÞ×ÕÔ ßâ ÓßÝàâßÝÙãÕÔ ÑÞÔ çßâÛã Òé ãÓâÑÝÒÜÙÞ× ÔÑäÑ ÙÞäß Ñ ãÕÓâÕä ÓßÔÕ äØÑä ÓÑÞ ßÞÜé ÒÕ åÞÜßÓÛÕÔ çÙäØ Ñ åÞÙáåÕ ÔÙ×ÙäÑÜ ÛÕé z"
    print(caesar_decrypt(input,112))

