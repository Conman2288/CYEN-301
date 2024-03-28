import sys

binary_input = sys.stdin.read()
binary_input = binary_input.replace("\r","").replace("\n", "").replace("\b","")

if len(binary_input) % 8 == 0:
    mod = 8
else:
    mod = 7

output = ''
i=0
while(i<len(binary_input)):
    div_bin = binary_input[i:i+mod] if i+8<len(binary_input) else binary_input[i:len(binary_input)]
    output += chr(int(div_bin,2))
    i +=mod


print(output)
