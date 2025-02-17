import I2C_LCD_driver
from time import *
import RPi.GPIO as GPIO 
#import Server.PythonFiles.addVote
#import Server.PythonFiles.findLocation
import addVote
import findLocation

#Setup for ultrasonic
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 16
GPIO_ECHO = 20
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

mylcd = I2C_LCD_driver.lcd()

#Global Variables
readyForVote = False
fullDistance = 0.0
smallDistance = 0.0
location = "Edmonton" #Set Location

#Green for true
def gbutton_callback(channel):
    if smallDistance == 0.0: #Setting up values
        smallDistance = distance() + (0.2 * fullDistance) #Gives Error, Needs better way
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Ready to Vote", 1)

    elif readyForVote == True:
        curDistance = distance()
        if curDistance >= smallDistance: #If there is no hole: True Vote
            lat_PI, long_PI = getLocation(location) #Get lat and long of location
            addVote(1, lat_PI, long_PI) #Adds Vote

            #Display
            mylcd.lcd_clear()
            mylcd.lcd_display_string("Voted: True", 1)

            time.sleep(2)

            mylcd.lcd_clear()
            mylcd.lcd_display_string("Ready to Vote", 1)


        else:
            mylcd.lcd_clear()
            mylcd.lcd_display_string("Voted Inconsistency", 1)

    else:
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Please Wait", 1)



#Red for false
def rbutton_callback(channel):
    if readyForVote == True:
        curDistance = distance()
        if curDistance <= smallDistance: #If there is no hole: True Vote
            lat_PI, long_PI = getLocation(location) #Get lat and long of location
            addVote(0, lat_PI, long_PI) #Adds the vote to database

            mylcd.lcd_clear()
            mylcd.lcd_display_string("Voted: False", 1)

            time.sleep(2)

            mylcd.lcd_clear()
            mylcd.lcd_display_string("Ready to Vote", 1)


        else:
            mylcd.lcd_clear()
            mylcd.lcd_display_string("Voted Inconsistency", 1)

    else:
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Please Wait", 1)



def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def main():
    #Init distance values
    fullDistance = distance()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Initilizing", 1)


    readyForVote = True

    #Button Logic
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BCM) # Use physical pin numbering
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)# Set pin 10 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.add_event_detect(17,GPIO.FALLING,callback=gbutton_callback)# Setup event on pin 10 rising edge
    GPIO.add_event_detect(27,GPIO.FALLING,callback=rbutton_callback)

    message = input("Press enter to quit\n\n") # Run until someone presses enter
    GPIO.cleanup() # Clean up

if __name__ == '__main__':
    main()




