import pickle
from Crypto.Cipher import DES
import time
import binascii
print("Starting")
start = time.time()


textlist=[["niceword","f912c5dcf6719e7d"]]
f=open("decryptionresults.txt","a")
#for i in range(100):
#    start=time.time()
for text in textlist:
    #print(f"Starting Bruteforce\nPlaintext: {text[0]}\nCiphertext: {text[1]}")
    ciphertext = binascii.unhexlify(text[1])
    for key in range(0, 100000000):
        if(key%100000==0):
            print(key)
        key=f"{key:08}"
        key = key.encode('utf-8')
        des = DES.new(key, DES.MODE_ECB)  # Create a DES cipher
        try:
            plain_text = des.decrypt(ciphertext)
            plain_text_str = plain_text.decode('utf-8', errors='ignore').rstrip('\x00')
            try:
                f.write(f"{key.decode('utf-8')} {plain_text_str}\n")
            except:
                continue
            if(plain_text_str==text[0]):
                print(f"{key.decode('utf-8')} {plain_text_str}")
                print()
                end=time.time()
                print(end-start)
                #start=end
                break
            
        except Exception as e:
            print(e)
            print(key)
            continue

end = time.time()
keygentime=start
print(f"Time Taken for Brute Force: {end-start} seconds")
