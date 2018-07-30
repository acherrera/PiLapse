#!/usr/bin/env python3
# Purpose: Run photo capture for an amount of time
# Created by: Anthony Herrera
# Notes: 
# Revisions:
#               2018.07.18 - Initial version
#               2018.07.18 - Made python script because file listing is hard
#               2018.07.19 - Updated for exfat systems
#               2018.07.23 - Added delay time


import os
import time

# Constants
trigger_interval=2
save_location = "/media/usb"

# Delay setup 
time_to_run = 600 # minutes to run program
time_to_sleep = 600 # minutes to wait
time_to_sleep = time_to_sleep*60
time.sleep(time_to_sleep)

# Send shutdown command 
# os.system("shutdown -h {}".format(time_to_run))

# Mount flash drive for backing up
os.system("sudo mkdir /media/usb")

# This is for fat file system
os.system("sudo mount -t vfat /dev/sda1 /media/usb -o uid=1000,gid=1000,utf8,dmask=027,fmask=137")

# Use this if  exfat flash drive is used
# os.system("sudo mount /dev/sda1 /media/usb")

# Get file location
file_location = __file__.split("/")[0:-1]
file_location = "/".join(file_location) + "/"

# Run the program!
os.system("{}/src/capture.py {} {}".format(file_location,
           trigger_interval, save_location))

