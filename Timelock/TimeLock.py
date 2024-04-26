import time
import hashlib
import sys

# A function to find the elapsed time between a given epoch time and the current time
def findElapsedTime(epTime, currentTime):

    # Convert the strings given into a form that can be manipulated
    epTime1 = time.strptime(str(epTime), "%Y %m %d %H %M %S")
    #epTime2 = time.strptime(currentTime, "%Y %m %d %H %M %S")
    
    # Calculates the time since 1970 01 01 00 00 00 for each of the two times given
    elapsed1 = time.mktime(epTime1)
    elapsed2 = time.mktime(currentTime)

    # Finds the difference in the two times since epoch to find the actual time elapsed between them
    elapsedTime = elapsed2-elapsed1

    # If we have to deal with a DST 
    # timeIfDST = elapsedTime + 3600
    # timeIfNotDST = elapsedTime - 3600

    return int(elapsedTime)

# A function to compute MD5(MD5(total seconds))
def doubleMD5(seconds_to_hash):
    # Rounds the seconds down to the nearest multiple of 60
    roundedSeconds = str(seconds_to_hash - (seconds_to_hash % 60))

    # Computes MD5 of the rounded seconds string, then the MD5 of that output
    myCode = hashlib.md5( hashlib.md5( roundedSeconds.encode() ).hexdigest().encode() ).hexdigest()

    return myCode

# A function to extract and concatenate the first two letters and last two integers from a hashed string
def exCon(code):
    i = 0
    secretCode = ""
    # Until we have the first two letters
    while len(secretCode) < 2:
        # Add the character from the hashed string if it is NOT a number
        if (str(code[i]).isnumeric() == False):
            secretCode += code[i]
        i += 1
    # Reset iterating variable so we can start at the end of the string
    i = -1
    # Until we have the last two numbers
    while len(secretCode) < 4:
        # Add the character (going backwards) from the hashed string if it IS a number
        if str(code[i]).isnumeric():
            secretCode += code[i]
        i-=1
    return secretCode


def main():
    # for i in range(1,11):
    #     DEBUG = i
    #     if DEBUG == 1:
    #         epTimeString = "1999 12 31 23 59 59"
    #         currentTime = "2013 05 06 07 43 25"
    #     if DEBUG == 2:
    #         epTimeString = "2017 01 01 00 00 00"
    #         currentTime = "2017 03 23 18 02 06"
    #     if DEBUG == 3:
    #         epTimeString = "1999 12 31 23 59 59" 
    #         currentTime = "2017 04 23 18 02 30"
    #     if DEBUG == 4:
    #         epTimeString = "2001 02 03 04 05 06"
    #         currentTime = "2010 06 13 12 55 34"
    #     if DEBUG == 5:
    #         epTimeString = "2015 01 01 00 00 00"
    #         currentTime = "2015 05 15 14 00 00"
    #     if DEBUG == 6:
    #         epTimeString = "2014 12 31 00 00 00"
    #         currentTime = "2015 01 01 00 00 00"
    #     if DEBUG == 7:
    #         epTimeString = "2014 12 31 00 00 00"
    #         currentTime = "2015 01 01 00 00 30"
    #     if DEBUG == 8:
    #         epTimeString = "2014 12 31 00 00 00"
    #         currentTime = "2015 01 01 00 01 00"
    #     if DEBUG == 9:
    #         epTimeString = "2014 12 31 00 00 00"
    #         currentTime = "2015 01 01 00 01 30"
    #     if DEBUG == 10:
    #         epTimeString = "1974 06 01 08 57 23"
    #         currentTime = "2017 04 26 15 14 30"

    currentTime = time.localtime()

    epochList = sys.argv[1:7]
    epochTime = ""
    for item in epochList:
        epochTime += item + " "

    a = findElapsedTime(epochTime, currentTime)
    msgA = exCon(doubleMD5(a))
    #print(f"Sample {DEBUG}")
    print(msgA)
    

main()
