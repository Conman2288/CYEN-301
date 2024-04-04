# Team Algae
# Alekhya Kalidindi, Cole Sylvester, Connor Heard, Dominic Rosario
# Hailey Allmann, Jacob Von Tress, Spencer Rochel
# Program #2 - Vigenere Cipher

# import system library
import sys

# encryption function
def encryption(input, key):
    # initialize text string
    text = ""
    # iterate through each index of input
    for i in range(len(input)):
        # check if characer is in the alphabet
        if input[i].isalpha():
            # add values of input character and key, then mod 26
            encrypt_char = (ord(input[i].upper()) + ord(key[i])) % 26
            # raise value to ASCII range of lowercase letters
            encrypt_char += 97

            # change case to lower or upper depending on input, then append to output
            if input[i].islower():
                text += chr(encrypt_char)
            else:
                text += chr(encrypt_char).upper()
        else:
            # append any non-alphabet character to output
            text += input[i]
            # insert a space to acommodate non-alphabet characters in the input
            key = key[:i]+" "+key[i:]

    # output the encrypted string
    print(text)

# decryption function
def decryption(input, key):
    # initialize text string
    text = ""
    # iterate through each index of input
    for i in range(len(input)):
        # check if characer is in the alphabet
        if input[i].isalpha():
            # add 26 to the input character's value and then subtract by the key's value, mod 26
            decrypt_char = (26 + ord(input[i].upper()) - ord(key[i])) % 26
            # raise value to ASCII range of lowercase letters
            decrypt_char += 97

            # change case to lower or upper depending on input, then append to output
            if input[i].islower():
                text += chr(decrypt_char)
            else:
                text += chr(decrypt_char).upper()

        else:
            # append any non-alphabet character to output
            text += input[i]
            # insert a space to acommodate non-alphabet characters in the input
            key = key[:i] + " " + key[i:]

    # output the decrypted string
    print(text)

# determines if user is encrypting or decrypting
cryption_type = sys.argv[1]

# saves key in all caps without spaces
key = sys.argv[2].upper().replace(" ","")

# try clause to run program unless interrupted
try:
    # accesses every argument in standard input
    for input in sys.stdin:
        # input without any new line characters
        input = input.strip('\n')
        # while loop to repeat key over all characters in the input
        while(len(input) >= len(key)):
            key += key

        # if type is encryption, run the encryption function, otherwise run decryption function
        if(cryption_type == '-e'):
            encryption(input, key)
        else:
            decryption(input, key)

# abort program run
except KeyboardInterrupt:
    print()
    sys.exit(0)
