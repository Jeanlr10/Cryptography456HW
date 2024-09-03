#********************************************************#
#***  _           _       __                          ***#
#*** | |         | |     /_ |                         ***#
#*** | |     __ _| |__    | |                         ***#
#*** | |    / _` | '_ \   | |                         ***#
#*** | |___| (_| | |_) |  | |                         ***#
#*** |______\__,_|_.__/   |_|                         ***#
#***                                                  ***#
#*** Lab 1: Symmetric encryption and decryption       ***#
#*** Due 09/07/2024                                   ***#
#*** By Jean-Luc Robitaille                           ***#
#***                                                  ***#
#*** Simple XOR encryption/decryption program         ***#
#*** V1 (Before it was modded to include bytearrays)  ***#
#********************************************************#
#
#
import binstr
message=''
message_bin=0
key=''
key_bin=0
#
#
#
#
#
def xor_cryptography(m_bin,k_bin): # m_bin is the message in binary     k_bin is the key in binary    
    key_count=0
    count=0
    output=''
    while count<len(m_bin):
            if len(k_bin)-1 <= key_count:       # Ensures the counter does not become greater than the length of the key in binary
                key_count=0                     #
            else:                               #
                key_count=key_count+1           #
            output=output+str(int(m_bin[count])^int(k_bin[key_count]))  # applies XOR to the current digit of each binary and appends it to output 
            count=count+1
    return output
#
#
#
#
#
def inputMessage():                                     # Function to minimize the amount of reused code when inputting the message
    print("\n\nPlease enter your Plaintext Message:")   #
    message=input('')                                   #
    message_bin=binstr.str_to_b(message)                #
    return message, message_bin                         #
#
#
#
#
#
def inputEncryptedbin():                                # Function to minimize the amount of reused code when inputting the encrypted binary
    print("\n\nPlease enter your Encrypted Message:")   #
    message_bin=input('')                               #
    message=binstr.b_to_str(message_bin)                #
    return message, message_bin                         #
#
#
#
#
#
def inputkey():                                         # Function to minimize the amount of reused code when inputting the key
    print("\n\nPlease enter your key:")                 #
    key=input('')                                       #
    key_bin=binstr.str_to_b(key)                        #
    return key,key_bin                                  #
#
#
#
#
#
def main():
    keepgoing=True
    while keepgoing:
        print("***************************************************************")
        print("*                                                             *")
        print("*       Welcome to Jean-Luc's Simple XOR Cipher Program       *")
        print("*                                                             *")
        print("*     Menu:                                                   *")
        print("*       1: Enter Plaintext Message                            *")
        print("*       2: View Message in Binary                             *")
        print("*       3: Enter Encrypted Message                            *")
        print("*       4: Attempt to View Encrypted Message in ASCII         *")
        print("*       5: Enter Key                                          *")
        print("*       6: View Key in Binary                                 *")
        print("*       7: Encrypt Message                                    *")
        print("*       8: Decrypt Message                                    *")
        print("*       9: Exit                                               *")
        print("*                                                             *")
        print("***************************************************************")
        choice=input()
        try:
            choice = int(choice)
        except:
            choice=0
        if choice == 1: # Enter Message
            message,message_bin=inputMessage()
            #
            #
            #
        elif choice == 2: # View Message as binary
            #
            if message=='': # Ensure the message is present
                message,message_bin=inputMessage()
            #
            print("\n\nMessage: ",message,"\nMessage Binary: ",message_bin)
            print("\n",bytearray(message,'utf-8'))
            input('\nPress Enter to continue')
            #
            #
        elif choice == 3: # Enter Encrypted binary
            #
            message,message_bin=inputEncryptedbin()
            #
            #
        elif choice == 4: # View Encrypted binary as ASCII
            #
            if message_bin==0: # Ensure the encrypted binary is present
                message,message_bin=inputEncryptedbin()
            #
            print("\nEncrypted Message binary: ",message_bin,"\nEncrypted Message in ASCII: ",message)
            input('\nPress Enter to continue')
            #
            #
        elif choice == 5: # Enter Key
            key,key_bin=inputkey()
            #
            #
        elif choice == 6: # View Key as Binary
            #
            if key=='': # Ensure the key is present
                key,key_bin=inputkey()
            #
            print("\nKey: ",key,"\nKey Binary: ",key_bin)
            input('\nPress Enter to continue')
            #
            #
        elif choice == 7: # Encrypt Message
            #
            if message_bin==0: # Ensure the message is present
                message,message_bin=inputMessage()
            #
            if key_bin==0: # Ensure the key is present
                key,key_bin=inputkey()
            print("Encoded Message: ",xor_cryptography(message_bin,key_bin))
            input('\nPress Enter to continue')
            #
            #
        elif choice == 8: # Decrypt Message
            #
            if message_bin==0:
                message,message_bin=inputEncryptedbin()
            if key_bin==0: # Ensure the key is present
                key,key_bin=inputkey()
            #
            print("Decoded Message: ",binstr.b_to_str(xor_cryptography(message_bin,key_bin)))
            input('\nPress Enter to continue')
            #
            #
        elif choice == 9: # Exit
            #
            print("Goodbye!")
            keepgoing=False
            #
            #
        else: # Invalid Choice
            #
            print("Please enter a valid choice")
            input('\nPress Enter to continue')
main()