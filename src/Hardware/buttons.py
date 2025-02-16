import I2C_LCD_driver
from time import *
import RPi.GPIO as GPIO 

mylcd = I2C_LCD_driver.lcd()


def gbutton_callback(channel):
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Green Button!", 1)
    
def rbutton_callback(channel):
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Red Button!", 1)
    
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)# Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(17,GPIO.FALLING,callback=gbutton_callback)# Setup event on pin 10 rising edge
GPIO.add_event_detect(27,GPIO.FALLING,callback=rbutton_callback)
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up

