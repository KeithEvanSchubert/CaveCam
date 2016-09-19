#!/usr/bin/env python
# Created by Keith Schubert on 5/19/2016.

import os
import time
import RPi.GPIO as GPIO
from datetime import datetime

# stuff to edit
FileNum = 0
delay = 10

# Setup
d = datetime.now()
year = "%04d" % (d.year)
month = "%02d" % (d.month)
day = "%02d" % (d.day)
hour = "%02d" % (d.hour)
min = "%02d" % (d.minute)
SaveDir = "/media/USB20FD/Pics_" + str(year) + "_" + str(month) + "_"  + str(day)
SaveDir = SaveDir + "_"  + str(hour) + "_"  + str(min)

os.mkdir(SaveDir)

f = open('/media/USB20FD/Dir','w')
f.write(str(SaveDir))
f.close()

f = open('/media/USB20FD/Num','w')
f.write(str(FileNum))
f.close()

time.sleep(delay)
os.system("sudo python /media/USB20FD/Single_Pic.py")
