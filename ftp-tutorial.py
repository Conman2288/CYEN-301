from ftplib import FTP

METHOD = 10
# FTP server details
IP = "138.47.165.156"
PORT = 21
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

# display the folder contents
result = ""
for f in files:
    file_permissions = f[:10] if METHOD == 10 else f[3:10]
    for char in file_permissions:
        if char != '-':
            result += '1'
        else:
            result += '0'

output = ""
i=0
while(i<=len(result)):
    x = result[i:i+7] if i+7<len(result) else result[i:len(result)]
    if(x != ''):
        output = output + chr(int(x,2))
    i=i+7

print(output)