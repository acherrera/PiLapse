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

camera = picamera.PiCamera()
delay_time = sys.argv[1] # delay time argument

# Create workspace if not made, move into space
capture_location = "captures"
if not os.path.exists(capture_location):
    os.mkdir(capture_location)

os.chdir(capture_location)

# Create new folder with unique name for data
folder_name = 0
new_file = True

while new_file:
    folder_name_string = str(folder_name)
    if not os.path.exists(folder_name_string):
        os.mkdir(folder_name_string)
        os.chdir(folder_name_string)
        new_file = False
    else:
        folder_name += 1

# Just run the crap out of this until Pi shuts down
name = 0
while True:
    camera.capture("{}.jpg".format(name))
    print("{}.jpg captured".format(name))
    time.sleep(5)
    name += 1

