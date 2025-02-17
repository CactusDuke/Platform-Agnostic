import I2C_LCD_driver
import time
import RPi.GPIO as GPIO
from addVote import addVote
from findLocation import getLocation

# Setup for ultrasonic
GPIO.setmode(GPIO.BCM)

# Set GPIO Pins
GPIO_TRIGGER = 16
GPIO_ECHO = 20

# Set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# Set up LCD display
mylcd = I2C_LCD_driver.lcd()

# Global Variables
readyForVote = False
fullDistance = 0.0
smallDistance = 30.0  # Set a fixed distance threshold for voting (e.g., 30 cm)
location = "Edmonton"  # Set Location

# Green button callback for True vote
def gbutton_callback(channel):
    global smallDistance
    if smallDistance == 0.0:  # Initial setup
        fullDistance = distance()  # Get the first reading
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Ready to Vote", 1)
    elif readyForVote:
        curDistance = distance()
        if curDistance >= smallDistance:  # If distance exceeds threshold, vote True
            lat_PI, long_PI = getLocation(location)  # Get location
            addVote(1, lat_PI, long_PI)  # Add vote as True
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

# Red button callback for False vote
def rbutton_callback(channel):
    if readyForVote:
        curDistance = distance()
        if curDistance <= smallDistance:  # If distance is below threshold, vote False
            lat_PI, long_PI = getLocation(location)  # Get location
            addVote(0, lat_PI, long_PI)  # Add vote as False
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

# Calculate distance from the ultrasonic sensor
def distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    dist = (TimeElapsed * 34300) / 2
    return dist

# Main function to initialize and start the voting process
def main():
    global readyForVote

    mylcd.lcd_clear()
    mylcd.lcd_display_string("Initializing", 1)
    time.sleep(2)

    readyForVote = True

    # Setup GPIO for button presses
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Green button (True vote)
    GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Red button (False vote)

    # Add event detection for button presses with debouncing
    GPIO.add_event_detect(17, GPIO.FALLING, callback=gbutton_callback, bouncetime=300)  # 300ms debounce
    GPIO.add_event_detect(27, GPIO.FALLING, callback=rbutton_callback, bouncetime=300)  # 300ms debounce

    mylcd.lcd_clear()
    mylcd.lcd_display_string("Press button to vote", 1)

    message = input("Press Enter to quit\n\n")  # Run until someone presses enter
    GPIO.cleanup()  # Clean up GPIO

if __name__ == '__main__':
    main()
