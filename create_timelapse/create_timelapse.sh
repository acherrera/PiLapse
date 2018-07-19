#!/bin/bash
# Purpose: Can't remember this command
# Created by: Anthony Herrera
# Notes: $1 is the output file name
# Revisions
#           2018.07.18 - Initial version


ffmpeg -r 30 -start_number 00001 -i %05d.jpg -s 1280x720 -vcodec libx264 $1


# -r: FPS
# -start_number: file number to start at
# -i: input filename
# 1280x720: output resolution
# $1: Output name
