You can use LapsePic.py if you want to keep your Pi Running (short lapse interval).  For long
intervals you will want to shut the Pi off and restart and have it run Single_Pic.py.  With
Single_Pic.py you need to: (1) make the directory in advance and pass its path as a command
line option (2) create a file called "Num" with the starting number of the file in the
directory you will be in when you invoke Single_Pic.py.

New simple system - run setup.py then put Single_Pic.py in chrontab.  eg: crontab -e and add:

@reboot sudo python setup.py &
@daily sudo python Single_Pic.py &

make sure to autologin by editing /etc/inittab: 

#1:2345:respawn:/sbin/getty 115200 tty1
1:2345:respawn:/bin/login -f pi tty1 </dev/tty1 >/dev/tty1 2>&1
