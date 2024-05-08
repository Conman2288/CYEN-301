# Team Algae
# Alekhya Kalidindi, Cole Sylvester, Connor Heard, Dominic Rosario
# Hailey Allmann, Jacob Von Tress, Spencer Rochel
# Program #7 - Steg
import sys

SENTINEL = bytearray([0, 0xff, 0, 0, 0xff, 0])

# This function parses the arguments passed by the user
# So that they can be passed into byte and bit function
def get_args():
    args = []
    for i in range(1,6):
        if (i - 2) < 1:
            args.append(sys.argv[i])
        else:
            args.append(sys.argv[i][2:])
    if args[0] == "-s":
        args.append(sys.argv[6][2:])
    return args

def help():
    print("Example Usage: python(3) steg.py -s -b -o<val> -i<val> -w<file> -h<secret_file> > output_file")
    print("-s --> store")
    print("-r --> retrieve")
    print("-b --> bit mode")
    print("-B --> byte mode")
    print("-o<val> --> set file header offset")
    print("-i<val> set bit/byte interval")
    print("-w<val> --> set wrapper file")
    print("-h<val> set hidden file")
    exit()

# This function iterates over an set interval of bytes and
# stores data between them; returns the combined file    
def byte_store(wrapper, hidden, offset=0, interval=1):
    with open(wrapper, "rb") as wrapper_file, open(hidden, "rb") as hidden_file:
        wrapper_bytes = bytearray(wrapper_file.read())
        hidden_bytes = bytearray(hidden_file.read())
    
    wrapper_size = len(wrapper_bytes)
    position = offset
    
    for i in range(len(hidden_bytes)):
        wrapper_bytes[position] = hidden_bytes[i]
        position += interval
        
    for byte in SENTINEL:
        wrapper_bytes[position] = byte
        position += interval
        
    return wrapper_bytes

# This function parses over the file and extracts a byte
# based every interval of bytes; it stops when it hits
# the sentinel bytes        
def byte_extract(wrapper, offset=0, interval=1):
    with open(wrapper, "rb") as wrapper_file:
        wrapper_bytes = bytearray(wrapper_file.read())
    
    output_bytes = bytearray()
    
    position = offset
    while position < len(wrapper_bytes):
        b = wrapper_bytes[position]
        if b == 0:
            look_ahead_pos = position + interval
            sent = True
            for i in range(5):
                if look_ahead_pos < len(wrapper_bytes):
                    if wrapper_bytes[look_ahead_pos] != SENTINEL[i + 1]:
                        sent = False
                        break
                    look_ahead_pos += interval
                else:
                    sent = False
                    break
            if sent:
                return output_bytes
        output_bytes.append(b)
        position += interval
        
    return output_bytes

# This function iterates through a wrapper file and
# hides data at a bit level by usiing bit-wise operators    
def bit_store(wrapper, hidden, offset=0, interval=1):
    with open(wrapper, "rb") as wrapper_file, open(hidden, "rb") as hidden_file:
        wrapper_bytes = bytearray(wrapper_file.read())
        hidden_bytes = bytearray(hidden_file.read())
    
    position = offset
    for i in range(len(hidden_bytes)):
        for j in range(8):
            wrapper_bytes[position] &= 0b11111110
            wrapper_bytes[position] |= ((hidden_bytes[i] & 0b10000000) >> 7)
            hidden_bytes[i] <<= 1
            position += interval
            
    position = offset
    for byte in SENTINEL:
        for j in range(8):
            wrapper_bytes[position] &= 0b11111110
            wrapper_bytes[position] |= ((byte & 0b10000000) >> 7)
            byte <<= 1
            position += interval
    
    return wrapper_bytes

# This function parses through the wrapper file and
# pulls out data using bitwise operators; it will stop
# once it hits the sentinel bytes
def bit_extract(wrapper, offset=0, interval=1):
    with open(wrapper, "rb") as wrapper_file:
        wrapper_bytes = bytearray(wrapper_file.read())
    
    output_bytes = bytearray()
    
    position = offset
    while (position + 7 * interval) < len(wrapper_bytes):
        b = 0
        for j in range(8):
            b |= (wrapper_bytes[position] & 0b00000001)
            if j < 7:
                b <<= 1
                position += interval
        if b == 0:
            look_ahead_pos = position + interval
            sent = True
            for i in range(5):
                if (look_ahead_pos + 7 * interval) < len(wrapper_bytes):
                    look_ahead_b = 0
                    for k in range(8):
                        look_ahead_b |= (wrapper_bytes[look_ahead_pos] & 0b00000001)
                        if k < 7:
                            look_ahead_b <<= 1
                            look_ahead_pos += interval
                    if look_ahead_b != SENTINEL[i + 1]:
                        sent = False
                        break
                else:
                    break
                look_ahead_b += interval
            if sent:
                return output_bytes
                
        output_bytes.append(b)
        position += interval
        
    return output_bytes
        
# Main command line program
if __name__ == '__main__':
    try:
        # Check for user input and use different function based on arguments passed
        args = get_args()
        if (args[0] == "-s"):
            if (args[1] == "-b"):
                output = bit_store(args[4], args[5], int(args[2]), int(args[3]))
            else:
                output = byte_store(args[4], args[5], int(args[2]), int(args[3]))

        elif (args[0] == "-r"):
            if (args[1] == "-b"):
                output = bit_extract(args[4], int(args[2]), int(args[3]))

            else:
                output = byte_extract(args[4], int(args[2]), int(args[3]))

        else:
            help()
            exit()

    except Exception:
        print("Error occured")
        for I in range (19):
            print("-", end='')
        help()
        

    sys.stdout.buffer.write(output)
