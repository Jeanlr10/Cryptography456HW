
import binstr
def xor_cryptography(m_bin,k_bin): # m_bin is the message in binary     k_bin is the key in binary
    key_count=0
    count=0
    output=''
    while count<len(m_bin):
            if len(k_bin)-1 <= key_count:       # Ensures the counter does not become greater than the length of the key in binary
                key_count=0                     #
            else:                               #
                key_count=key_count+1           #
            if bin(int(m_bin[count]))!=bin(int(k_bin[key_count])):      # outputs the logical equivelant of XOR between the 
                output=output+"1"                                       # current digit of the message binary and the current 
            else:                                                       # digit of the key binary
                output=output+"0"                                       #
            count=count+1
    return output
keepgoing=True
message=''
message_bin=0
key=''
key_bin=0
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
        print("\n\nPlease enter your Plaintext Message:")
        message=input('')
        message_bin=binstr.str_to_b(message)
        #
        #
        #
    elif choice == 2: # View Message as binary
        if message=='' and message_bin==0:
            print("\n\nPlease enter your Message:")
            message=input('')
        elif message_bin!=0:
            message=binstr.b_to_str(message_bin)
        print("\n\nMessage: ",message,"\nMessage Binary: ",message_bin)
        input('\nPress Enter to continue')
        #
        #
        #
    elif choice == 3: # Enter Encrypted binary
        print("\n\nPlease enter your Encrypted Message:")
        message_bin=input('')
        message=binstr.b_to_str(message_bin)
        #
        #
        #
    elif choice == 4: # View Encrypted binary as ASCII
        if message_bin==0:
            print("\n\nPlease enter your Encrypted Message:")
            message_bin=input('')
            message=binstr.b_to_str(message_bin)
        print("\nEncrypted Message binary: ",message_bin,"\nEncrypted Message in ASCII: ",message)
        input('\nPress Enter to continue')
        #
        #
        #
    elif choice == 5: # Enter Key
        print("\n\nPlease enter your key:")
        key=input('')
        key_bin=binstr.str_to_b(key)
    elif choice == 6: # View Key as Binary
        if key=='':
            print("\n\nPlease enter your Message:")
            key=input('')
        print("\nKey: ",key,"\nKey Binary: ",key_bin)
        input('\nPress Enter to continue')
    elif choice == 7: # Encrypt Message
        print("Encoded Message: ",xor_cryptography(message_bin,key_bin))
        input('\nPress Enter to continue')
    elif choice == 8: # Decrypt Message
        print("Decoded Message: ",binstr.b_to_str(xor_cryptography(message_bin,key_bin)))
        input('\nPress Enter to continue')
    elif choice == 9: # Exit
        print("Goodbye!")
        keepgoing=False
    else: # Invalid Choice
        print("Please enter a valid choice")
        input('\nPress Enter to continue')
