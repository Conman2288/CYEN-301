# Vigenere Cipher
# Python 3

import sys

# This function output a cyclic key used in Vigenere cipher
def cyclic_key_generation(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range (len(string) - len(key)):
            key.append(key[i % len(key)])
            return("" . join(key))


# Checking if the user gives correct number and types of arguments
if not((len(sys.argv) >= 2 and (sys.argv[1] == "-d" or sys.argv[1] == "-e"))):
    print("Please use the following syntax: python3 vigenere.py [arg] [key_string]")
    sys.exit()

else:
    print("Here is the given key " + sys.argv[2])

    user_text = input("")

    # Create a repeatable key with equal length to user provided string
    full_key = cyclic_key_generation(user_text, sys.argv[2])
    print("Here the full key based on length of given text: " + full_key)