import random

#format the date and time
from datetime import datetime
now = datetime.now() # current date and time
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
time = now.strftime("%H:%M:%S")
date_time = now.strftime("%Y%m%d_%H%M%S")
print(date_time)

#write to the file
with open(date_time+'.txt', 'w') as f:  #create the txt file
    f.write(date_time)
    f.write("   -   Do not reuse.  Destroy after encoding/decoding.\n")
    for number in range(15):  #number of rows
        f.write("\n\n\n")
        for number in range(12): #digits per row
            shift_val = str(random.randint(0, 25))
            f.write(shift_val.zfill(2))
            f.write("     ")

print("finished")