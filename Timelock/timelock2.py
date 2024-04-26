from datetime import datetime, timezone, timedelta
import sys
import hashlib
import pytz

def is_dst(dt,timeZone):
   aware_dt = timeZone.localize(dt)
   return aware_dt.dst() != timedelta(0,0)

#starts here!!
us_central_timezone = pytz.timezone('US/Central')
epoch_time = sys.stdin.readline().replace('"','')
current_time = "2017 03 23 18 02 06"

epoch_time = datetime.strptime(epoch_time, "%Y %m %d %H %M %S")
current_time = datetime.strptime(str(current_time), "%Y %m %d %H %M %S")

# Check if daylight saving time is currently in effect
dst_now = is_dst(current_time, us_central_timezone)

# Check if daylight saving time was in effect for the epoch time
dst_epoch = is_dst(epoch_time, us_central_timezone)

#print(dst_now, dst_epoch)
# # Adjust epoch time and current time if there's a difference in DST
if dst_now != dst_epoch:
    # Add/subtract 1 hour to adjust for DST difference
    epoch_time += timedelta(hours=1) if dst_now > dst_epoch else timedelta(hours=-1)

# Calculate the time difference in seconds
time_difference = current_time - epoch_time

# Get the total elapsed time in seconds
elapsed_seconds = time_difference.total_seconds()
#print(elapsed_seconds)
# Adjust for the 60-second interval
elapsed_seconds -= elapsed_seconds % 60
#print(elapsed_seconds)
# Compute MD5 hash of the elapsed time
elapsed_seconds_md5 = hashlib.md5(str(int(elapsed_seconds)).encode()).hexdigest()

# Compute MD5 hash of the MD5 hash
elapsed_seconds_md5_md5 = hashlib.md5(elapsed_seconds_md5.encode()).hexdigest()
#print(elapsed_seconds_md5_md5)
# Extract and concatenate the specified code
code = ""
for char in elapsed_seconds_md5_md5:
    if(char.isalpha()):
        code+=char
    if len(code)==2:
        break
for char in elapsed_seconds_md5_md5[::-1]:
    if(char.isnumeric()):
        code+=char
    if len(code)==4:
        break

print(code)
