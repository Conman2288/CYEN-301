# Team Algae
# Alekhya Kalidindi, Cole Sylvester, Connor Heard, Dominic Rosario
# Hailey Allmann, Jacob Von Tress, Spencer Rochel
# Program #6 - XOR Crypto

import sys

def help():
    print("\nUsage: python3 xor.py [ciphertext] [key]")
    print("Example with ciphertext file named \"ciphertext\" and key file named \"key\".\nThe example also redirects to another file for ease of access:")
    print("\n\npython3 xor.py ciphertext key > example\n")
    exit()

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

    file_to_decrypt = sys.argv[1]
    
    if file_to_decrypt == "help":
        help()

    key_file_name = sys.argv[2]

    with open(file_to_decrypt, "rb") as data_file:
        data = bytearray(data_file.read())

    # Read from key file and create byte array
    with open(key_file_name, "rb") as key_file:
        key = bytearray(key_file.read())

    # Encrypt and decrpyt via XOR
    result = encrypt_decrypt(data, key)

    # write to standard output
    sys.stdout.buffer.write(result)