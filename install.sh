#!/bin/bash
# Created by: Anthony Herrera
# Purpose: Install needed files for GPS data capture
# Revisions:
#       2018.07.30 - Initial version
#       2018.08.01 - Updated with python smbus
#       2018.08.03 - Added fswebcam


sudo apt-get install exiftool imagemagick -y
sudo apt-get install fswebcam


# Download the files and make executable
# wget ozzmaker.com/downloads/berryIMU.py
# wget ozzmaker.com/downloads/LSM9DS0.py
# wget ozzmaker.com/downloads/takephoto.sh

# Install python requirement
sudo apt-get install python-smbus

# Make executable
chmod +x takephoto.sh
