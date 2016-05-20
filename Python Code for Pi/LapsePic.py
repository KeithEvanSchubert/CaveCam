#!/usr/bin/env python
# Created by Keith Schubert on 5/19/2016.
# This script takes pictures at interval with the Raspberry Pi
# camera, and stores them with a dynamically generated name.

import os
import time
import RPi.GPIO as GPIO
from datetime import datetime

# settings
interval=30 # in seconds 24*60*60

imgWidth = 2592  #max 2592
imgHeight = 1944 #max 1944
sharpness = 0 #-100 to 100
contrast = 0 #-100 to 100
brightness = 50 #0 to 100
saturation = 0 #-100 to 100
ISO = 200 #100 to 800
ev = 0 #-10 to 10
quality = 100 # 1 to 100
encoding = "jpg" # jpg, bmp, gif, png

options = "-n -r -awb auto -mm average -w " + str(imgWidth) +
" -h " + str(imgHeight) + " -sh " + str(sharpness) + " -co " +
str(contrast) + " -br " + str(brightness) + " -sa " + str(saturation) +
" -ISO " + str(ISO) + " -ev " + str(ev) + " -q " + str(quality) +
" -e " + encoding


# Setup
d = datetime.now()
year = "%04d" % (d.year)
month = "%02d" % (d.month)
day = "%02d" % (d.day)
hour = "%02d" % (d.hour)
min = "%02d" % (d.minute)
SaveDir = "Pics_" + str(year) + "_" + str(month) + "_"  + str(day) +
"_"  + str(hour) + "_"  + str(min)

os.mkdir(SaveDir)
FileNum = 0

# main loop
try:
  while True:
    d = datetime.now()
    year = "%04d" % (d.year)
    month = "%02d" % (d.month)
    day = "%02d" % (d.day)
    hour = "%02d" % (d.hour)
    min = "%02d" % (d.minute)

    os.system("raspistill " + options + " -x time.yyyy.mm.dd.hh.mm=" +
    str(year) + "." + str(month) + "."  + str(day) + "."  + str(hour) +
    "."  + str(min) + " -o " + SaveDir + "/Pic_" + str(FileNum) +
    "." + encoding )

    FileNum += 1
    time.sleep(interval)
except KeyboardInterrupt:	
