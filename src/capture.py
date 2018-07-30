#!/usr/bin/env python3

"""
Created by: Anthony Herrera
Purpose: Take images every X seconds
Notes: Input should be number of seconds between photos

Revisions:
            2018.07.17 - Initial Version
            2018.07.18 - folder creation method
            2018.07.18 - Restructured program for def / main sections

"""

import picamera
import sys
import os
import shutil
import logging
from time import sleep


############## Function Definitions ###################

# Create new folder with unique name for data

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
            logging.info("Created unique file {}".format(folder_name))
            new_file = False
        else:
            start_number += 1

    return folder_name


def ContinousCapture(interval):
    """
    Captures images every "x" seconds
    """

    camera = picamera.PiCamera()
    camera.resolution = (3280, 2464)

    for filename in camera.capture_continuous('{counter:05d}.jpg'):
        logging.info("Caputred {}".format(filename))
        sleep(int(interval))


################## Main Loop #########################

if __name__=="__main__":

    # Basic Setup
    log_name = "image_log.log"

    # Create logging file if needed
    try:
        os.remove(log_name)
        logging.basicConfig(filename=log_name, level=logging.INFO)
    except FileNotFoundError:
        logging.basicConfig(filename=log_name, level=logging.INFO)
        logging.error("{} not removed - does not exist".format(log_name))


    # Inputs
    delay_time = sys.argv[1] # delay time argument
    backup_location = sys.argv[2] # Where to save data

    # Constants
    capture_location = "captures"

    # Create unique file and get filename
    folder_name = CreateUniqueFile(backup_location)

    # Go to directory
    os.chdir(folder_name)

    # Caputure data continuously
    ContinousCapture(delay_time)
