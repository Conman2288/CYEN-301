#UTILIZE A REDIRECTION INPUT THAT CONTAINS A CORRECTLY SIZED BINARY (same length as overt message)

# use Python 3
import socket
from time import sleep
import sys

binary_file = ""
for line in sys.stdin:
	binary_file += line

# set the port for client connections
port = 1338

# create the socket and bind it to the port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", port))

# listen for clients
# this is a blocking call
s.listen(0)
print("Server is listening...")

# a client has connected!
c, addr = s.accept()

# set the message
msg = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est lab\nEOF"

counter_for_binary = 0
length_of_message = len(msg)
EOF_position = length_of_message - 4
# send the message, one letter at a time
for i in range(0, length_of_message):

	if i < EOF_position:

		c.send(msg[i].encode())
		# delay a bit in between each letter
		if binary_file[counter_for_binary] == '1':
			sleep(0.1)
		else:
			sleep(0.025)
		counter_for_binary += 1
	
	else:
		c.send(msg[i].encode())

# send EOF and close the connection to the client
print("Message sent...")
c.close()

