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
import logging


# Basic Setup
log_name = "image_log.log"
os.remove(log_name)
camera = picamera.PiCamera()
logging.basicConfig(filename=log_name, level=logging.INFO)

# Inputs
delay_time = sys.argv[1] # delay time argument
backup_location = sys.argv[2] # Where to save data

# Constants
capture_location = "captures"
last_backup_time = time.time()
back_up_interval=17  # backup time in seconds

# Create new folder with unique name for data
folder_name = 0


def CreateUniqueFile(start_location, start_number=0):
    """
    This will create a unique file at the backup location
    param start_location: locaton to put files
    param start_number: number to start file naming
    """
    new_file = True
    while new_file:
        folder_name = start_location + "/" + str(start_number)
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            new_file = False
        else:
            start_number += 1

        return folder_name


def ContinousCapture(interval):
    """
    Captures images every "x" seconds
    """
    name = 1
    while True:
        camera.capture("{:05}.jpg".format(name))
        logging.info("{:05}.jpg captured".format(name))
        time.sleep(int(interval))
        name += 1


folder_name = CreateUniqueFile(backup_location)
os.chdir(folder_name)
ContinousCapture(delay_time)
