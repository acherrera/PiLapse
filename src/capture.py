#!/usr/bin/env python3

"""
Created by: Anthony Herrera
Purpose: Take images every X seconds
Notes: Input should be number of seconds between photos

Revisions:
            2018.07.17 - Initial Version
            2018.07.18 - folder creation method
"""

import picamera
import sys
import time
import os
import shutil

camera = picamera.PiCamera()

# Inputs
delay_time = sys.argv[1] # delay time argument
backup_location = sys.argv[2] # Where to save data

# Constants
capture_location = "captures"
last_backup_time = time.time()
back_up_interval=17  # backup time in seconds

# Create workspace if not made, move into space
if not os.path.exists(capture_location):
    os.mkdir(capture_location)

os.chdir(capture_location)

# Create new folder with unique name for data
folder_name = 0
new_file = True

while new_file:
    folder_name_string = backup_location + "/" + str(folder_name)
    if not os.path.exists(folder_name_string):
        os.mkdir(folder_name_string)
        os.chdir(folder_name_string)
        new_file = False
    else:
        folder_name += 1

# Just run the crap out of this until Pi shuts down
#TODO start timer - back up to flash drive every hour

current_dir = os.getcwd()

name = 1
while True:

    camera.capture("{:05}.jpg".format(name))
    print("{:05}.jpg captured".format(name))
    time.sleep(5)
    name += 1

