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

def bit_method_store():
   pass

def bit_method_retrieve():
    pass

def byte_method_store():
    pass

def byte_method_store():
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
         
    else:
        exit()