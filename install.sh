#!/bin/bash
# Created by: Anthony Herrera
# Purpose: Install needed files for GPS data capture
# Revisions:
#       2018.07.30 - Initial version
#       2018.08.01 - Updated with python smbus


sudo apt-get install exiftool imagemagick -y


# Download the files and make executable
wget ozzmaker.com/downloads/berryIMU.py
wget ozzmaker.com/downloads/LSM9DS0.py
wget ozzmaker.com/downloads/takephoto.sh

# Install python requirement
sudo apt-get install python-smbus

# Make executable
chmod +x takephoto.sh
