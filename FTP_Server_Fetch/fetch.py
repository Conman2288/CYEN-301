# Team Algae
# Alekhya Kalidindi, Cole Sylvester, Connor Heard, Dominic Rosario
# Hailey Allmann, Jacob Von Tress, Spencer Rochel
# Program #3 - FTP Permission Decode

from ftplib import FTP

METHOD = 10
# FTP server details
IP = "138.47.99.64"
PORT = 1221
# FTP server is configured to allow anonymous logons with
# blank password entry
USER = "anonymous"
PASSWORD = ""
FOLDER = "/" + str(METHOD)
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

# converting file permissions to binary
result = ""
for f in files:
    # input file permissions based on the METHOD
    if METHOD == 7 and f[0:3] == "---":
        file_permissions = f[3:10]
    else:
        file_permissions = ""
    if METHOD == 10:
        file_permissions = f[:10]
    
    #converting file permissions to binary
    for char in file_permissions:
        if char != '-':
            result += '1' # if permission exists add '1' to result
        else:
            result += '0' # if permission does not exist add '0' to result

output = ""
i=0
while(i<=len(result)):
    x = result[i:i+7] if i+7<len(result) else result[i:len(result)]
    if(x != ''):
        output = output + chr(int(x,2)) # Convert the binary to ASCII format
    i=i+7

print(output)
