# Team Algae
# Alekhya Kalidindi, Cole Sylvester, Connor Heard, Dominic Rosario
# Hailey Allmann, Jacob Von Tress, Spencer Rochel
# Program #7 - Steg
import sys
import os
SENTINEL = bytearray([0, 0xff, 0, 0, 0xff, 0])
# This function parses the arguments passed by the user
# So that they can be passed into byte and bit function

def help():
    print("Usage Error - In order to use, the format must be 'py steg-brute.py [b or B] [wrapper file]")
    print("For [b or B], b is for bit and B is for byte")
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

def file_creator(bit_or_byte, offset_val, interval_val, folder_name, output):

    os.makedirs(folder_name, exist_ok=True)
    filename = f"{bit_or_byte}_Off({offset_val})_Int({interval_val}).jpg"
    file_path = os.path.join(folder_name, filename)
    with open(file_path, "wb") as file:
        file.write(output)

# Main command line program
if __name__ == '__main__':

    # Check for user input and use different function based on arguments passed
    try:
        bit_or_byte = sys.argv[1]
        wrapper_file = sys.argv[2]
        if (bit_or_byte == "b" and len(sys.argv) == 3):
            offset = 512
            while offset < 1025:
                interval = 1
                while interval < 257:
                    output = bit_extract(wrapper_file, offset, interval)
                    folder_name = "Bit-Method"
                    file_creator("Bit", offset, interval, folder_name, output)
                    interval = interval *2  # Square interval after printing
                offset = offset * 2

        elif (bit_or_byte == "B" and len(sys.argv) == 3):
            offset = 512
            while offset < 1025:
                interval = 1
                while interval < 257:
                    output = bit_extract(wrapper_file, offset, interval)
                    folder_name = "Byte-Method"
                    file_creator("Bit", offset, interval, folder_name, output)
                    interval = interval *2  # Square interval after printing
                offset = offset * 2

        else:
            help()

    except Exception:
        help()