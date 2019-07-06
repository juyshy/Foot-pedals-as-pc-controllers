#-------------------------------------------------------------------------------
# using piezotest2/piezotest2.ino
# Copyright:   (c) Jukka 2016
# Licence:     do what you wish
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import serial
import time,os
from datetime import datetime,timedelta
import pyautogui
import platform

ossystem=platform.system()

print "Activating piezo switches.."
portnum=0

if ossystem != 'Windows':
    for portnum in range(0,7):
        try:
            ser = serial.Serial(portnum)
            print "Pic in port ", portnum
            break
        except:
            pass
    #     ser.close()
    #     ser = serial.Serial(3)

else:
    serport="COM5"
    serports=["COM6","COM4","COM8","COM9","COM10","COM11","COM12","COM13","COM14","COM5","COM7","COM2","COM3","COM1"]#
    for serport in serports:
        try:
            print("tryin port ", serport)
            ser = serial.Serial(serport)
            break
        except:
            pass

print "connect serialport",serport
ser
time.sleep(1)
instream=""


last_click_time=last_switch_time =datetime.now() -timedelta(seconds=3)

prevvalue='0'
prevvalue2='0'
last_values = ('0','0')
previnstream=""
while True:
#for x in range(500):

    # cntrlcb = paste_from_clipboard()
    # if 'cancel' in cntrlcb:
    #     print "cancelled"
    while ser.inWaiting() > 0:

        instream +=ser.read()


    if instream != previnstream:
        print instream[-3],
        if instream[-3] == '1':
            pyautogui.click()
        elif instream[-3] == '2':
            print "windows switcher"
            switchtime=datetime.now()
            timedelta1=switchtime- last_switch_time
            timedelta1.microseconds
            if timedelta1.seconds < 1 and timedelta1.microseconds < 300000:
                break
            # print  timedelta1.microseconds
            last_switch_time=switchtime
            os.system(r'"C:\Users\Default\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\Window Switcher.lnk"')
        elif instream[-3] == '3':
            pyautogui.mouseDown()
            time.sleep(3)
            pyautogui.mouseUp()
        elif instream[-3] == '4':
            pyautogui.doubleClick()
            time.sleep(1)

        elif instream[-3] == '5':
            pyautogui.rightClick()
            time.sleep(1)



    instream = instream[-4:]
    previnstream =instream
    time.sleep(0.05)

print "closing"
ser.close()

