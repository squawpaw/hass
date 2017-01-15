#!/usr/bin/env python2.7  
# script by Alex Eames http://RasPi.tv
# PIR functions added by Corey Vaughan
  
import RPi.GPIO as GPIO  
from datetime import datetime
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  
  
# GPIO 23 & 24 set up as inputs. One pulled up, the other down.  
# 23 will go to GND when button pressed and 24 will go to 3V3 (3.3V)  
# this enables us to demonstrate both rising and falling edge detection  
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.IN)

# now we'll define the threaded callback function  
# this will run in another thread when our event is detected  
def my_callback(channel):  
   print "BUTTON INTRUDER!"
   print datetime.now()

def PIR_active(channel):  
   print "PIR INTRUDER!"
   print datetime.now()

  
print "Make sure you have a button connected so that when pressed"  
print "it will connect GPIO port 23 (pin 16) to GND (pin 6)\n"  
print "You will also need a second button connected so that when pressed"  
print "it will connect GPIO port 24 (pin 18) to 3V3 (pin 1)"  
raw_input("Press Enter when ready\n>")  
  
# The GPIO.add_event_detect() line below set things up so that  
# when a rising edge is detected on port 24, regardless of whatever   
# else is happening in the program, the function "my_callback" will be run  
# It will happen even while the program is waiting for  
# a falling edge on the other button.  
GPIO.add_event_detect(24, GPIO.RISING, callback=my_callback)
GPIO.add_event_detect(21, GPIO.RISING, callback=PIR_active) 
  
try:  
	## Old code...
    '''print "Waiting for falling edge on port 23"  
                GPIO.wait_for_edge(23, GPIO.FALLING)  
                print "Falling edge detected. Here endeth the second lesson."  '''
    xTime = 0

    while xTime < 60:

    	print "All is quiet..."
    	print xTime
    	xTime += 1
      time.sleep(10)


except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit