# import libraries
import socket
from sys import stdout
from time import perf_counter

# debugging tools
debug = False
debugSignal = False

# set the server's IP address and port
ip = ""
port = 1338

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

#initialize variables
covertMessage = ""
binaryBuffer = ""
receivedSignals = ""
delays = []

while (receivedSignals[-3:] != "EOF"):
    # start the "timer"
    t0 = perf_counter()
    # get the signal
    signal = s.recv(1).decode()
    # end the "timer"
    t1 = perf_counter()
    # calculate the time delta
    delta = round(t1 - t0, 3)
    # Append the signal to the string
    receivedSignals += signal
    if (debugSignal):
        print(signal)
    # Add the delay to the list
    delays.append(delta)

# Convert delays to binary
binaryBuffer = ''.join('1' if delay >= 0.05 else '0' for delay in delays)
if (debug):
    print("Binary:", binaryBuffer)
    print()

#The first bit of binary is incorrect. More than likely this is because of it being the connection being established, then sending the regular message.
binaryBuffer = binaryBuffer[1:]

# Convert binary to ASCII
while len(binaryBuffer) >= 8:
    covertMessage += chr(int(binaryBuffer[:8], 2))
    binaryBuffer = binaryBuffer[8:]

# Print the covert message and received signals
stdout.write("Overt message:" + receivedSignals)
stdout.write("\n")

#End file here (covert) as EOF defines when it stops
counter_for_start = 0
for i in range(3, len(covertMessage) + 1):
    if covertMessage[counter_for_start:i] == "EOF":
        covertMessage = covertMessage[:counter_for_start]
    counter_for_start += 1

stdout.write("Covert message:" + covertMessage)
if (debug):
    print()
    print(delays)
    print(len(delays))
# close the connection to the server
s.close()