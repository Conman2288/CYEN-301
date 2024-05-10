# Team Algae
# Alekhya Kalidindi, Cole Sylvester, Connor Heard, Dominic Rosario
# Hailey Allmann, Jacob Von Tress, Spencer Rochel
# Program #6 - XOR Crypto

import sys

key_file_name = "k3y"

# Function to encrypt and decrypt ciphertext/plaintext
# Logic of function gotten from https://www.geeksforgeeks.org/xor-cipher/
def encrypt_decrypt(input, xor_key):

    # Length of key argument
    key_length = len(xor_key)

    encrypted_data = bytearray()


    # We want to do XOR operation of key
    # against every character in the string
    for i in range (len(input)):
        encrypted_data.append(input[i] ^ xor_key[i % key_length])

    return encrypted_data    

# Main program
if __name__ == '__main__':

    # Read from stdin and create bytearray from contents
    data = bytearray(sys.stdin.buffer.read())

    # Read from key file and create byte array
    with open(key_file_name, "rb") as key_file:
        key = bytearray(key_file.read())

    # Encrypt and decrpyt via XOR
    result = encrypt_decrypt(data, key)

    # write to standard output
    sys.stdout.buffer.write(result)