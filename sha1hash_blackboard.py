import hashlib

sha1hash = input("[*] Enter sh1 Hash Value: ")
print(sha1hash)
f = open("10-million-password-list-top-1000000.txt", 'r')
passlist = f.read()
for password in passlist.split('\n'):
    hashguess = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
    #print(hashguess)
    if hashguess == sha1hash:
        print("[+] The Password is: " + str(password))
        quit()
    #else:
        #print("[-] Password guess" + str(password) + " does not match, trying next...")
    #
    hashguess = hashlib.sha224(bytes(password, 'utf-8')).hexdigest()
    #print(hashguess)
    if hashguess == sha1hash:
        print("[+] The Password is: " + str(password))
        quit()
    #else:
        #print("[-] Password guess" + str(password) + " does not match, trying next...")
    #
    hashguess = hashlib.sha256(bytes(password, 'utf-8')).hexdigest()
    #print(hashguess)
    if hashguess == sha1hash:
        print("[+] The Password is: " + str(password))
        quit()
    #else:
        #print("[-] Password guess" + str(password) + " does not match, trying next...")
    #
    hashguess = hashlib.sha512(bytes(password, 'utf-8')).hexdigest()
    #print(hashguess)
    if hashguess == sha1hash:
        print("[+] The Password is: " + str(password))
        quit()
    #else:
        #print("[-] Password guess" + str(password) + " does not match, trying next...")
    #
    hashguess = hashlib.md5(bytes(password, 'utf-8')).hexdigest()
    #print(hashguess)
    if hashguess == sha1hash:
        print("[+] The Password is: " + str(password))
        quit()
    #else:
        #print("[-] Password guess" + str(password) + " does not match, trying next...")
        
    
print("Password not in passwordlist")
