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


# try:
print "Activating foot switches.."

for portnum in range(0,7):

    try:
        ser = serial.Serial(portnum)
        print "Pic in port ", portnum
        break
    except:
        pass
#     ser.close()
#     ser = serial.Serial(3)

time.sleep(1)
instream=""


last_click_time=last_switch_time =datetime.now() -timedelta(seconds=3)

prevvalue='0'
prevvalue2='0'
last_values = ('0','0')

while True:
#for x in range(500):

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

