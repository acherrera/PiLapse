# PiLapse - the program for making time lapse videos with your Raspberry Pi! 


# How to use
Right now this system is just getting started. It will capture images and will
save them to an external drive but there are a couple caveats. Because this
project is just beginning and is kind of my free time project,getting it to
work for you might require a bit of programming

    * External drive must be located at /dev/sda1. 
    * External drive must be FAT or exFAT. See runme to choose which file to
      use
    * Timelapse creation script must be run from the folder containing the
      images. It's a dumb program for now

The install scripts just install libraries and packages that I did not have or
needed. Some of these are pretty simple (pip3) but are included because it
doesn't hurt as far as I know. If you run into dependancy issues, I guess let
me know and I can add it.


# Future work:
* Make better documentation
* Block out capture.py into funnctions. Have functions run in main loop 
* runme.py should just call the main program. Could pretty easily combine the
  two into one file. This might make everything a little easier to maintain
* Timelapse creation script should take a location as an argument and create
  the timelapse from the images at that location. 
    Basically, move to location, create movie, copy movie back



### Current State: Image capturing is good. Working on testing and improvements
