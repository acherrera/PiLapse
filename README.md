# PiLapse - the program for making time lapse videos with your Raspberry Pi and
a Pi camera!


# How to use

Run the install script in the main folder to install the prerequistes, then run
the runme.py file to save data. To change the time interval of capture the the
value in the runme.py file. Change the save_location variable to a location on
your computer. The program will go to that location, make a unique file name -
just a number - and then start saving images!

Currently this is mounting an external hard drive because this running in a
Raspberry Pi. Because of this:
* External drive must be located at /dev/sda1. 
* External drive must be FAT or exFAT. See runme to choose which file to use.
  Need to change which command is commented out. Or just need to reformat flash
  drive

If the external hard drive is not needed, comment out the lines that create the
mount point and mount the drive in the runme.py file

The install scripts just install libraries and packages that I did not have or
needed. Some of these are pretty simple (pip3) but are included because it
doesn't hurt as far as I know. If you run into dependancy issues, I guess let
me know and I can add it.


# Future work:
* Make better documentation
* runme.py should just call the main program. Could pretty easily combine the
  two into one file. This might make everything a little easier to maintain
* ~~Timelapse creation script should take a location as an argument and create
  the timelapse from the images at that location.~~ **May be working, needs
  testing**


# Changelog

## 2018.07.19 - script was run all day. Appears to be working
