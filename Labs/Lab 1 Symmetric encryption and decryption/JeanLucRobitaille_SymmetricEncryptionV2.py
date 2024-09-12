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
#*** V2 (After it was modded to include bytearrays)  ***#
#********************************************************#
#
#
#
#
#
def tobinary(input):
    byte_data=bytearray(input,'utf-8') # Converts input to byte array
    bits=bin(int.from_bytes(byte_data,'big')) # Converts byte array to bits
    return bits;
#
#
#
#
#
def tostring(input):
    input = input[2:] # Strips 0b from the input
    print(input)
    #
    padded_length = (len(input) + 7) // 8 * 8 # Calculate the length needed to Ensure the binary data's length is a multiple of 8
    byte_length = (padded_length // 8) #Determine the length of the integer in bytes
    #
    input = input.zfill(padded_length)  # Fills in the string with leading zeroes to make its length a multiple of 8
    integer = int(input, 2) #Convert the padded string back to an integer
    #
    #
    print(integer)
    byte_data = integer.to_bytes(byte_length, 'big')    #Converts the integer to a bytearray
    #
    print(byte_data)
    result = byte_data.decode('utf-8')  #Decodes the byte array into a UTF-8 String
    return result
#
#
#
#
#
def xor_cryptography(m_bin,k_bin): # m_bin is the message in binary     k_bin is the key in binary    
    key_count=2     # Starts looping through the binaries after 0b
    count=2         #
    output=''   #Initializes output as a blank array
    while count<len(m_bin):
            if len(k_bin)-1 <= key_count:       # Ensures the counter does not become greater than the length of the key in binary
                key_count=2                     #
            else:                               #
                key_count=key_count+1           #
            output=output+str(int(m_bin[count])^int(k_bin[key_count]))  # applies XOR to the current digit of each binary and appends it to output 
            count=count+1
    output="0b"+output
    return output
#
#
#
#
#
def inputMessage():                                     # Function to minimize the amount of reused code when inputting the message
    print("\n\nPlease enter your Plaintext Message:")   #
    message=input('')                                   #
    message_bin=tobinary(message)                       #
    print(tostring(message_bin))
    return message, message_bin                         #
#
#
#
#
#
def inputEncryptedbin():                                # Function to minimize the amount of reused code when inputting the encrypted binary
    print("\n\nPlease enter your Encrypted Message:")   #
    message_bin=input('')                               #
    message="Unable to display, Message Encrypted"
    return message, message_bin                         #
#
#
#
#
#
def inputkey():                                         # Function to minimize the amount of reused code when inputting the key
    print("\n\nPlease enter your key:")                 #
    key=input('')                                       #
    key_bin=tobinary(key)                        #
    return key,key_bin                                  #
#
#
#
#
#
def main():
    message=''
    message_bin=0
    key=''
    key_bin=0
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
        print("*       4: Enter Key                                          *")
        print("*       5: View Key in Binary                                 *")
        print("*       6: Encrypt Message                                    *")
        print("*       7: Decrypt Message                                    *")
        print("*       8: Exit                                               *")
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
            input('\nPress Enter to continue')
            #
            #
        elif choice == 3: # Enter Encrypted binary
            #
            message,message_bin=inputEncryptedbin()
            #
            #
        elif choice == 4: # Enter Key
            key,key_bin=inputkey()
            #
            #
        elif choice == 5: # View Key as Binary
            #
            if key=='': # Ensure the key is present
                key,key_bin=inputkey()
            #
            print("\nKey: ",key,"\nKey Binary: ",key_bin)
            input('\nPress Enter to continue')
            #
            #
        elif choice == 6: # Encrypt Message
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
        elif choice == 7: # Decrypt Message
            #
            if message_bin==0:
                message,message_bin=inputEncryptedbin()
            if key_bin==0: # Ensure the key is present
                key,key_bin=inputkey()
            #
            print("Decoded Message: ",tostring(xor_cryptography(message_bin,key_bin)))
            input('\nPress Enter to continue')
            #
            #
        elif choice == 8: # Exit
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