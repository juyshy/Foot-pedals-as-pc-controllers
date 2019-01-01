#-------------------------------------------------------------------------------

# Copyright:   (c) Jukka 2016
# Licence:     do what you wish
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import serial
import time,os
from datetime import datetime,timedelta
import re
import pyautogui
import platform
from utils import paste_from_clipboard

ossystem=platform.system()
# try:

print "Activating foot switches.."
portnum=0

if ossystem != 'Windows':
    for portnum in range(0,7):

        try:
            ser = serial.Serial(portnum)
            ser = serial.Serial(portnum)
            print "Pic in port ", portnum
            break
        except:
            pass
    #     ser.close()
    #     ser = serial.Serial(3)


else:

    serport="COM5"
    serports=["COM1","COM2","COM3","COM4","COM5","COM6","COM7","COM8","COM9","COM10","COM11","COM12"]
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

while True:
#for x in range(500):

    # cntrlcb = paste_from_clipboard()
    # if 'cancel' in cntrlcb:
    #     print "cancelled"
    while ser.inWaiting() > 0:
        instream +=ser.read()
    instream = instream[-100:]

    last_val = re.findall(r'A=(\d)B=(\d)\D*$',instream)
    if last_val != []:

        last_values= last_val[0]

    last_val, last_val2 = last_values

    if prevvalue != last_val:
        # print  "A",  last_val,
        prevvalue = last_val
        if last_val == '1':
            print "windows switcher"
            switchtime=datetime.now()
            timedelta1=switchtime- last_switch_time
            timedelta1.microseconds
            if timedelta1.seconds < 1 and timedelta1.microseconds < 300000:
                break
            # print  timedelta1.microseconds
            last_switch_time=switchtime
            os.system(r'"C:\Users\Default\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\Window Switcher.lnk"')

    if prevvalue2 != last_val2:
        # print  "B" , last_val2,
        prevvalue2 = last_val2

        if last_val2 == '1':
            print "click"
            # clicktime = datetime.now()
            # timedelta2 = clicktime - last_click_time
            # timedelta2.microseconds
            # if timedelta2.seconds < 1 and timedelta2.microseconds < 300000:
            #     break
            # print  timedelta1.microseconds
            # last_click_time = clicktime
            pyautogui.click()
            # os.system(r'"E:\autohotkeys\leftmouseclick.ahk"')


    time.sleep(0.03)

print "closing"
ser.close()

