# import libraries
import socket
from sys import stdout
from time import perf_counter

# debugging tools
debug = True
debugSignal = False

# set the server's IP address and port
ip = "138.47.165.156"
port = 31337

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
    signal = s.recv(4096).decode()
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

# Convert binary to ASCII
while len(binaryBuffer) >= 8:
    covertMessage += chr(int(binaryBuffer[:8], 2))
    binaryBuffer = binaryBuffer[8:]

# Print the covert message and received signals
stdout.write("Overt message:" + receivedSignals)
stdout.write("")
stdout.write("Covert message:" + covertMessage)
if (debug):
    print()
    print(delays)
    print(len(delays))
# close the connection to the server
s.close()
