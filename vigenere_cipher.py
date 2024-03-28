# Vigenere Cipher
# Python 3

import sys

# Function to encrypt or decrypt the user text with the provided key

# Checking if the user gives correct number and types of arguments
if not((len(sys.argv) >= 2 and (sys.argv[1] == "-d" or sys.argv[1] == "-e"))):
    print("Please use the following syntax: python3 vigenere.py [arg] [key_string]")
    sys.exit()

else:
    user_text = input("\n")