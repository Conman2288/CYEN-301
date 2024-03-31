import sys
def encryption(input, key):
    text = ""
    for i in range(len(input)):
        if input[i].isalpha():
            encrypt_char = (ord(input[i].upper()) + ord(key[i])) % 26
            encrypt_char += 97
            if input[i].islower():
                text += chr(encrypt_char)
            else:
                text += chr(encrypt_char).upper()
        else:
            text += input[i]
            key = key[:i]+" "+key[i:]
    print( text)
def decryption(input, key):

    text = ""
    for i in range(len(input)):

        if input[i].isalpha():

            decrypt_char = (26 + ord(input[i].upper()) - ord(key[i])) % 26
            decrypt_char += 97

            if input[i].islower():
                text += chr(decrypt_char)
            else:
                text += chr(decrypt_char).upper()

        else:
            text += input[i]
            key = key[:i] + " " + key[i:]

    print(text)


cryption_type = sys.argv[1]
key = sys.argv[2].upper().replace(" ","")

try:
    for input in sys.stdin:
        input = input.strip('\n')
        while(len(input) >= len(key)):
            key += key

        if(cryption_type == '-e'):
            encryption(input, key)
        else:
            decryption(input, key)

except KeyboardInterrupt:
    print()
    sys.exit(0)
