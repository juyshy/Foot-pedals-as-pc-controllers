Foot pedals as pc controllers
=======

Two switches via arduino controlling windows switcher (to replace ALT+TAB) and left mouse click.
 


Prerequisites, Requirements: 
	- Arduino Uno
	- (foot) Switches
	- Python, python modules: serial, pyautogui

Exit from serial polling loop: double swich with pedal A (windows switcher)

Arduino code and wiring: 
    - piezotest2.ino  provides polling for 5 analog inputs
    - connect 5 piezos with protective 1 M ohm resistors (like instructed here https://microcontrollerslab.com/piezoelectric-sensor-interfacing-arduino-uno-r3/)

installation: 
    - upload piezotest2/piezotest2.ino to arduino 
    - connect arduino to pc
    - replace your file paths and python executable paths at pedals_launcher.bat
    - launch pedals_launcher.bat