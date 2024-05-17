# Team Algae
# Alekhya Kalidindi, Cole Sylvester, Connor Heard, Dominic Rosario
# Hailey Allmann, Jacob Von Tress, Spencer Rochel
# Program #1 - Binary Decoder

# import system library
import sys
def help():
    print("\nUsage: python3 Binary_decoder.py < [file_with_binary]")
    print("\nTo ensure no problems, make sure all of the binary (1's and 0's)\nare on one single line in the file.")
    print("\nExample with a binary file named \"binary.txt\":")
    print("\npython3 Binary_decoder.py < binary.txt\n")
    exit()
    
if len(sys.argv) >= 2 and sys.argv[1] == "help":
    help()

# read input from terminal
binary_input = sys.stdin.read()
# remove all spacing
binary_input = binary_input.replace("\r","").replace("\n", "").replace("\b","")

# check if the length of the input is divisible by 8
if len(binary_input) % 8 == 0:
    mod = 8
else:
    mod = 7

# initialize output string
output = ''
# initialize counter for while loop
i=0

# iterate through binary
while(i<len(binary_input)):
    # extract portion of binary depending on mod variable
    div_bin = binary_input[i:i+mod] if i+8<len(binary_input) else binary_input[i:len(binary_input)]
    # convert binary to ASCII
    output += chr(int(div_bin,2))
    # increment counter
    i +=mod

# print output
print(output)
