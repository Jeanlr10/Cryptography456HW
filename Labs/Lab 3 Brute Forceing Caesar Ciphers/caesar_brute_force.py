#  _           _       ____       _____                              _____            _                 ____             _         ______             _             
# | |         | |     |___ \ _   / ____|                            / ____|          | |               |  _ \           | |       |  ____|           (_)            
# | |     __ _| |__     __) (_) | |     __ _  ___  ___  __ _ _ __  | |    _   _ _ __ | |__   ___ _ __  | |_) |_ __ _   _| |_ ___  | |__ ___  _ __ ___ _ _ __   __ _ 
# | |    / _` | '_ \   |__ <    | |    / _` |/ _ \/ __|/ _` | '__| | |   | | | | '_ \| '_ \ / _ \ '__| |  _ <| '__| | | | __/ _ \ |  __/ _ \| '__/ __| | '_ \ / _` |
# | |___| (_| | |_) |  ___) |_  | |___| (_| |  __/\__ \ (_| | |    | |___| |_| | |_) | | | |  __/ |    | |_) | |  | |_| | ||  __/ | | | (_) | | | (__| | | | | (_| |
# |______\__,_|_.__/  |____/(_)  \_____\__,_|\___||___/\__,_|_|     \_____\__, | .__/|_| |_|\___|_|    |____/|_|   \__,_|\__\___| |_|  \___/|_|  \___|_|_| |_|\__, |
#                                                                          __/ | |                                                                             __/ |
#                                                                         |___/|_|                                                                            |___/ 
# By Jean-Luc Robitaille
mostcommonwords=[" the "," be "," to "," of "," and "," a "," in "," that "," have "," i "]
cipherfile = open("Labs\Lab 3 Brute Forceing Caesar Ciphers\cipher string.txt","r")
ciphertext=cipherfile.read()
i= False
j=0
while(i==False):
    if j%1000==0 and j!=0:
        print(j)
    possible=False
    plain_text = ''
    for l in ciphertext:
        index = ord(l)
        index = (index - j) % 1114111
        plain_text = plain_text + chr(index)
    #The only problem with this method is that it doesn't work if
    #the plaintext does not have one of the 10 most common words
    # However, it is very hard to write without any word in the 
    # given mostcommonwords array
    for word in mostcommonwords:
            if word in plain_text.lower():
                possible=True
                break
    if possible==True:
        print("\n\n",plain_text,"\n\nDoes this look like plaintext? (Y/N)\n")
        correct=input()
        if correct=='Y' or correct=='y':
            i=True
            break
    j=j+1
print("Plain Text: ",plain_text,"\nKey: ",j-1)

