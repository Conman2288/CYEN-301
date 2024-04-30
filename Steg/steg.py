# Team Algae
# Alekhya Kalidindi, Cole Sylvester, Connor Heard, Dominic Rosario
# Hailey Allmann, Jacob Von Tress, Spencer Rochel
# Program #7 - Steg

import sys

# Debug option for verbose output
DEBUG = True

# Sentinel bytes to tell end of hidden file
SENTINEL = bytearray([0x00, 0xff, 0x00, 0x00, 0xff, 0x00])
REVERSE_SENTINEL = bytearray([0x00, 0xff, 0x00, 0x00, 0xff, 0x00])



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
    # We need to read the hidden and wrapper files
    # as byte arrays
    byte_wrapper_file = bytearray(wrapper_file.read())
    byte_hidden_file = bytearray(hidden_file.read())

    count = 0

    while (i < len(byte_wrapper_file)):
        # overwrite actual bytes with hidden bytes
        byte_wrapper_file[offset] = byte_hidden_file[i]
        
        # move our location in byte array by interval value
        offset += interval
        i += 1

        # insert a series of bytes to denote end
        # of hidden file in byte array
        for j in range(len(SENTINEL)):
            byte_wrapper_file[offset] = SENTINEL[i]
            offset += interval
            i += 1

        wrapper_file.close()
        hidden_file.close()

        return byte_wrapper_file


def byte_method_retrieve(wrapper_file, hidden_file, offset=0):
    pass


def bit_method_store():
    pass

def bit_method_store():
    pass


if __name__ == '__main__':
     
    if (DEBUG):
        try:
            print("Argument indices: ", end='')
            string = ""

            for i in range(len(sys.argv)):
                string += str(sys.argv[i]) + "[" + str(i) + "] " 
            print(string.rstrip(", "))

        except Exception:
            print("Error with arguments.")
            help()
     
     # Run the bit store method based on user args
    if ("-b" in sys.argv and "-s" in sys.argv):
        pass
        #output_file = bit_method_store(int(sys.argv[2]), sys.argv[4], sys.argv[5])

    elif ("-b" in sys.argv and "-r" in sys.argv):
        pass

    elif ("-B" in sys.argv and "-s" in sys.argv):
        output_file = byte_method_store(sys.argv[8], sys.argv[10], int(sys.argv[4]), int(sys.argv[6]))

    elif ("-B" in sys.argv and "-r" in sys.argv):
        pass

    else:
        exit()

    sys.stdout.buffer.write(output_file)
    exit()