# Team Algae: Vigenere Cipher
# Python 3

import sys

DEBUG = False

# This function outputs a cyclic key used in Vigenere cipher
def cyclic_key_generation(string, key):
    if len(string) == len(key):
        return key
    else:
        cyclic_key = ''
        for i in range (len(string) - len(key)):
            cyclic_key += key[i % len(key)]
        return cyclic_key
    

# This function returns an Vigenere encrypted string
# We get the unicode value for each value in the given string
# and add it to the equivalent unicode value for the cyclic_key
# We then mod it by 26 to peform the alphabetic shift in each iteration
def encrypt_string(string, key):
    new_string = ''
    key_index = 0
    for char in string:
        if char.isupper():
            x = (ord(char) + ord(key[key_index].upper()) - 2 * ord('A')) % 26 + ord('A')
        elif char.islower():
            x = (ord(char) + ord(key[key_index].lower()) - 2 * ord('a')) % 26 + ord('a')
        else:
            x = ord(char)
        new_string += chr(x)
        if char.isalpha():
            key_index = (key_index + 1) % len(key)
    return new_string
    
# This function does the mathematical inverse of the encrypt
# function to return the plaintext string, given a key
def decrypt_string(string, key):
    new_string = ''
    key_index = 0
    for char in string:
        if char.isupper():
            x = (ord(char) - ord(key[key_index].upper()) + 26) % 26 + ord('A')
        elif char.islower():
            x = (ord(char) - ord(key[key_index].lower()) + 26) % 26 + ord('a')
        else:
            x = ord(char)
        new_string += chr(x)
        if char.isalpha():
            key_index = (key_index + 1) % len(key)
    return new_string

# Checking if the user gives correct number and types of arguments
if not((len(sys.argv) >= 2 and (sys.argv[1] == "-d" or sys.argv[1] == "-e"))):
    print("Please use the following syntax: python3 vigenere.py [arg] [key_string]")
    sys.exit()

else:
    try:
        while True:
            if (DEBUG):
                print("Here is the given key " + sys.argv[2])

            user_text = input("")

            # Create a repeatable key with equal length to user provided string
            full_key = cyclic_key_generation(user_text, sys.argv[2])

            if (DEBUG):
                print("Here the full key based on length of given text: " + full_key)

            # Decryption
            if (sys.argv[1] == "-d"):
                decrypted_string = decrypt_string(user_text, full_key)
                print(decrypted_string)

            # Encryption
            if (sys.argv[1] == "-e"):
                encrypted_string = encrypt_string(user_text, full_key)
                print(encrypted_string)

    except KeyboardInterrupt:
        print()
        sys.exit()