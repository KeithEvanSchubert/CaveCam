#!/usr/bin/env python
# Created by Keith Schubert on 5/19/2016.
# This script takes pictures at interval with the Raspberry Pi
# camera, and stores them with a dynamically generated name.

import os
import sys
import time
import RPi.GPIO as GPIO
from datetime import datetime

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

options = "-n -r -awb auto -mm average -w " + str(imgWidth) + " -h "
options = options + str(imgHeight) + " -sh " + str(sharpness) + " -co "
options = options + str(contrast) + " -br " + str(brightness) + " -sa "
options = options + str(saturation) + " -ISO " + str(ISO) + " -ev "
options = options + str(ev) + " -q " + str(quality) + " -e " + encoding

# GPIO
setupdelay = 10
holddelay = 10
SigPin = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SigPin, GPIO.OUT)
GPIO.output(SigPin,GPIO.LOW)

# Setup
d = datetime.now()
year = "%04d" % (d.year)
month = "%02d" % (d.month)
day = "%02d" % (d.day)
hour = "%02d" % (d.hour)
min = "%02d" % (d.minute)
#SaveDir = sys.argv[1]
f = open('/media/USB20FD/Dir','r+')
SaveDir = f.read()
f.close()

f = open('/media/USB20FD/Num','r+')
FileNum = int(f.read())
f.seek(0)
f.write(str(FileNum+1))
f.close()

d = datetime.now()
year = "%04d" % (d.year)
month = "%02d" % (d.month)
day = "%02d" % (d.day)
hour = "%02d" % (d.hour)
min = "%02d" % (d.minute)

Tag = " -x time.yyyy.mm.dd.hh.mm=" +     str(year) + "." + str(month)
Tag = Tag + "."  + str(day) + "."  + str(hour) + "."  + str(min)
FileName = SaveDir + "/Pic_" + str(FileNum) + "." + encoding


GPIO.output(SigPin,GPIO.HIGH)
time.sleep(setupdelay)

os.system("raspistill " + options + Tag + " -o " + FileName )

time.sleep(holddelay)
GPIO.output(SigPin,GPIO.LOW)

FileNameFLIR = SaveDir + "/FLIR_" + str(FileNum) + "." + encoding
FLIRcmd ="/home/pi/pylepton/pylepton_capture -d /dev/spidev0.1 "
os.system(FLIRcmd + FileNameFLIR )
