#!/bin/bash
#Setup GPIO21 as input. GPIO21 will be used to detect if the GPS has a fix.
echo "21" > /sys/class/gpio/export
echo "in" > /sys/class/gpio/gpio21/direction

IntervalTime=5

while true; do

    echo "Starting"
    START_TIME=$SECONDS

    #Check to see if GPS has a FIX.  GPS fix pin will go high every 1 sec if there is a fix. 
    FIX="NO"  # Reset fix condition
    #Stay in this 'while' loop if there is no fix and less than two secands have passed.
    while [ $FIX == "NO" ] && [ $(($SECONDS  - $START_TIME)) -lt 2 ]; do
        fixcheck=$(cat /sys/class/gpio/gpio21/value)      #GPIO21 is connected to the fix indication pin on BerryGPS-IMU
        if [ "$fixcheck" == "0" ]; then
            FIX="NO"
        else
            FIX="YES"
        fi
    done

    #If there is a fix, grab all the relevant GPS data
    if [ $FIX == "YES" ]; then
        tpv=$(gpspipe -w -n 10 | grep -m 1 TPV)
        latitude=$(echo $tpv | python -c 'import sys, json; print json.load(sys.stdin)["lat"]')
        longitude=$(echo $tpv | python -c 'import sys, json; print json.load(sys.stdin)["lon"]')
        altitude=$(echo $tpv | python -c 'import sys, json; print json.load(sys.stdin)["alt"]')
        speed=$(echo $tpv | python -c 'import sys, json; print json.load(sys.stdin)["speed"]')
        time=$(echo $tpv | python -c 'import sys, json; print json.load(sys.stdin)["time"]')

        #Convert latitude to 5 decimal places
        latitude=$(printf "%0.5f\n" $latitude)
        longitude=$(printf "%0.5f\n" $longitude)
    fi

    #Get angles and heading from the IMU
    attitude=$(sudo python /home/pi/pilapse/berryIMU_files/berryIMU.py | tail -n2 | head -n1)
    echo "debug: $attitude"
    roll=$(echo $attitude | python -c 'import sys, json; print json.load(sys.stdin)["Roll"]')
    pitch=$(echo $attitude | python -c 'import sys, json; print json.load(sys.stdin)["Pitch"]')
    heading=$(echo $attitude | python -c 'import sys, json; print json.load(sys.stdin)["tiltCompensatedHeading"]')


    #Create file name with current time
    FILE="/home/pi/image_$(date +%Y%m%d_%H%M%S).jpg"

    #Remove old file
    sudo rm -f /home/pi/image.jpg


    fswebcam -r 1280x720 --no-banner /home/pi/image.jpg

    #Take photo
    # sudo raspistill -o /home/pi/image.jpg  -ex auto -w 1280 -h 720 --nopreview  --rotation 180


    #Add GeoTags and attitude to bottom of image and save with new file name
    if [ $FIX == "YES" ];then
        # cmd="convert /home/pi/image.jpg -gravity SouthEast -stroke '#000C' -pointsize 24 -strokewidth 2 -annotate 0 'Lat: $latitude Lon: $longitude Alt: $altitude Speed: $speed Pitch: $pitch Roll: $roll Direction: $heading' -stroke none -fill white -annotate 0 'Lat: $latitude Lon: $longitude Alt: $altitude Speed: $speed Pitch: $pitch Roll: $roll Direction: $heading' $FILE"
        #If you dont want to annotate the photos with the metadata, comment out the above line and use the line below.
        cmd="convert /home/pi/image.jpg   $FILE"

        eval $cmd

        #Update the photo with all the relevant exif metadata
        exiftool -fast -fast2 -overwrite_original_in_place '-gpstimestamp<${DateTimeOriginal}+1:00' '-gpsdatestamp<${DateTimeOriginal}+1:00' -GPSLongitudeRef="E" -GPSLongitude="$longitude" -GPSLatitudeRef="S" -GPSLatitude="$latitude" -GPSAltitude="$altitude" -GPSroll="$roll" -GPSpitch="$pitch" -GPSImgDirectionRef="m" -GPSImgDirection="$heading" "$FILE"

        else
        #As there isnt a GPS fix, only add roll,pitch and direction.
        cmd="convert /home/pi/image.jpg -gravity SouthEast -stroke '#000C' -pointsize 24 -strokewidth 2 -annotate 0 'Pitch: $pitch Roll: $roll Direction: $heading' -stroke none -fill white -annotate 0 'Pitch: $pitch Roll: $roll Direction: $heading' $FILE"

        eval $cmd

        #Update EXIF information
        exiftool -fast -fast2 -overwrite_original_in_place -GPSroll="$roll" -GPSpitch="$pitch" -GPSImgDirectionRef="m" -GPSImgDirection="$heading" "$FILE"
    fi

    #Delay loop, set to how often you want a photo to be taken
    while [ $(($SECONDS  - $START_TIME)) -lt $IntervalTime ]; do
        sleep 1
    done
done
