# Team Algae
# Alekhya Kalidindi, Cole Sylvester, Connor Heard, Dominic Rosario
# Hailey Allmann, Jacob Von Tress, Spencer Rochel
# Program #7 - Steg

import sys

# Debug option for verbose output
DEBUG = False

# Sentinel bytes to tell end of hidden file
SENTINEL = bytearray([0x00, 0xff, 0x00, 0x00, 0xff, 0x00])


def function_debug(wrapper_array, hidden_array):
    print("Wrapper: " + str(wrapper_array), sys.stderr)
    print("Hidden " + str(hidden_array), sys.stderr)


def help():
    print("Example Usage: python(3) steg.py -s -b -o <val> - i <val> -w <file> -h <secret_file> > output_file")
    print("-s --> store")
    print("-r --> retrieve")
    print("-b --> bit mode")
    print("-B --> byte mode")
    print("-o <val> --> set file header offset")
    print("-i <val> set bit/byte interval")
    print("-w <val> --> set wrapper file")
    print("-h <val> set hidden file")
    exit()

def byte_method_store(wrapper_file, hidden_file, offset=0, interval=1):
    with open(wrapper_file, "rb") as wrapper:
        byte_wrapper_file = bytearray(wrapper.read())
    
    with open(hidden_file, "rb") as hidden:
        byte_hidden_file = bytearray(hidden.read())

    i = 0
    while (i < len(byte_hidden_file)):
        # overwrite actual bytes with hidden bytes
        byte_wrapper_file[offset] = byte_hidden_file[i]
        offset += interval
        i += 1



    j = 0
    while (j < len(SENTINEL)):
        byte_wrapper_file[offset] = SENTINEL[j]
        offset += interval
        j += 1

    return byte_wrapper_file


def byte_method_retrieve(wrapper_file, offset=0, interval=1):
    with open(wrapper_file, "rb") as wrapper:
        byte_wrapper_file = bytearray(wrapper.read())

    output_bytes = bytearray()
    
    # set an offset to keep track of our position
    # when tracing through the wrapper file
    while (offset < len(byte_wrapper_file)):
        b = byte_wrapper_file[offset]
        output_bytes.append(b)
        offset += interval
    
        # Check if we have reached the sentinel bytes
        if len(output_bytes) >= len(SENTINEL) and output_bytes[-len(SENTINEL):] == SENTINEL:
            break

    return output_bytes.rstrip(SENTINEL)


def bit_method_store(wrapper_file, hidden_file, offset=0, interval=1):
    with open(wrapper_file, "rb") as wrapper:
        wrapper_bytes = bytearray(wrapper.read())

    with open(hidden_file, "rb") as hidden:
        hidden_bytes = bytearray(hidden.read())

    i = 0
    while (i < len(hidden_bytes)):
        byte = hidden_bytes[i]
        for j in range(8):
            # Remove the lsb
            wrapper_bytes[offset] &= 0xFE
            wrapper_bytes[offset] |= (byte & 0x80) >> 7
            byte <<= 1 # perform a bit shift to left
            offset += interval
        i += 1


    i = 0
    while (i < len(SENTINEL)):
        byte = SENTINEL[i]
        for j in range(8):
            wrapper_bytes[offset] &= 0xFE
            wrapper_bytes[offset] |= (byte & 0x80) >> 7
            byte <<= 1
            offset += interval
        i += 1


def bit_method_retrieve(wrapper_file, offset=0, interval=1):
    with open(wrapper_file, "rb") as wrapper:
        wrapper_bytes = bytearray(wrapper.read())


    output_file = bytearray()

    b = 0
    count = 0

    for i in range(offset, len(wrapper_bytes), interval):
        if (count == 0):
            b = 0
        bit = wrapper_bytes[offset] & 0x01
        b |= (bit << count)
        count += 1
        offset += interval
        
        if (count == 8):
            output_file.append(b)
            count = 0

        # Check if we have reached the sentinel bytes
        if len(output_file) >= len(SENTINEL) and output_file[-len(SENTINEL):] == SENTINEL:
            break

    return output_file.rstrip(SENTINEL)

if __name__ == '__main__':
     
    if (DEBUG):
        try:
            print("Argument indices: ", end='')
            string = ""

            for i in range(len(sys.argv)):
                string += str(sys.argv[i]) + "[" + str(i) + "] " 
            print(string.rstrip(", "))
            exit()

        except Exception:
            print("Error with arguments.")
            help()
     
     # Run the bit store method based on user args
    if ("-b" in sys.argv and "-s" in sys.argv):
        output_file = bit_method_store(sys.argv[8], sys.argv[10], int(sys.argv[4]), int(sys.argv[6]))

    elif ("-b" in sys.argv and "-r" in sys.argv):
        output_file = bit_method_retrieve(sys.argv[8], int(sys.argv[4]), int(sys.argv[6]))

    elif ("-B" in sys.argv and "-s" in sys.argv):
        output_file = byte_method_store(sys.argv[8], sys.argv[10], int(sys.argv[4]), int(sys.argv[6]))

    elif ("-B" in sys.argv and "-r" in sys.argv):
        output_file = byte_method_retrieve(sys.argv[8], int(sys.argv[4]), int(sys.argv[6]))

    else:
        help()
        exit()

    
    sys.stdout.buffer.write(output_file)
    exit()