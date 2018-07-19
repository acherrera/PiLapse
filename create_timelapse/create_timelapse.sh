#!/bin/bash
# Purpose: Can't remember this command
# Created by: Anthony Herrera
# Notes: $1 is the output file name
# Revisions
#           2018.07.18 - Initial version
#           2018.07.19 - Added directory option


output_name=$1
target_dir=$2
current_dir=$PWD

# Got to dir and make the video
cd target_dir
ffmpeg -r 30 -start_number 00001 -i %05d.jpg -s 1280x720 -vcodec libx264 $output_name

# Options to use in command
# -r: FPS
# -start_number: file number to start at
# -i: input filename
# 1280x720: output resolution
# $1: Output name

# Copy video back and come back
mv $output_name current_dir
cd current_dir


