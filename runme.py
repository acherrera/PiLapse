#!/usr/bin/env python3
# Purpose: Run photo capture for an amount of time
# Created by: Anthony Herrera
# Notes: 
# Revisions:
#               2018.07.18 - Initial version
#               2018.07.18 - Made python script because file listing is hard
#               2018.07.19 - Updated for exfat systems



import os

# Constants
trigger_interval=2
save_location = "/media/usb"


# Mount flash drive for backing up
os.system("sudo mkdir /media/usb")

# This is for fat file system
os.system("sudo mount -t vfat /dev/sda1 /media/usb -o uid=1000,gid=1000,utf8,dmask=027,fmask=137")

# Use this if  exfat flash drive is used
# os.system("sudo mount /dev/sda1 /media/usb")

# Main program that is run. Captures every 
file_location = __file__.split("/")[0:-1]
file_location = "/".join(file_location) + "/"
os.system("{}/src/capture.py {} {}".format(file_location,
           trigger_interval, save_location))

# Note - final implementation needs the above running in background
