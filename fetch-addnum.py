#THIS PROGRAM HELPS WITH CHANGING THE METHOD (7 or 10) INSTEAD OF MANUALLY DOING IT
#Run it by doing the following:
# python fetch-addnum.py [7 or 10]
#Everything else is the same, it just helps with changing between the two

from ftplib import FTP
import sys

METHOD = int(sys.argv[1])

if METHOD not in [7, 10]:
    print("ADD A VALID BIT NUM FOR DECRYPTING")
    exit()

# FTP server details
IP = "138.47.161.43"
PORT = 21
# FTP server is configured to allow anonymous logons with
# blank password entry
USER = "jonastaylor"
PASSWORD = "megalodon"
FOLDER = "/files/" + str(METHOD)
USE_PASSIVE = True  # set to False if the connection times out

# connect and login to the FTP server
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

# navigate to the specified directory and list files
ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)
# exit the FTP server
ftp.quit()

# display the folder contents
result = ""
for f in files:
    if f[0] != "-" and f[1] != "-" and f[2] != "-":
        continue
    file_permissions = f[:10] if METHOD == 10 else f[3:10]
    for char in file_permissions:
        if char != '-':
            result += '1' # if permission exists add '1' to result
        else:
            result += '0' # if permission does not exit add '0' to result

output = ""
i=0
while(i<=len(result)):

    
    x = result[i:i+7] if i+7<len(result) else result[i:len(result)]
    if(x != ''):
        output = output + chr(int(x,2)) # Convert the binary to ASCII format
    i=i+7

print(output)