# Import required libraries
from lcd1602 import LCD1602
from time import sleep
import RPi.GPIO as GPIO
import flickering, lightsense, tempsense
from multiprocessing import Process
import os

# Set variable for LCD library
lcd = LCD1602()

# Print a test pattern to the LCD
lcd.lcd_string("Home Automation",lcd.LCD_LINE_1)
lcd.lcd_string("     System    ",lcd.LCD_LINE_2)

# Wait for 3 secs
print('DEBUG: Wait for 3 secs before continuting')
sleep(3)

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.OUT)

# Set up menu variables
selected = "none"
menu = 1
oneOn = False

#Set up thread variables
fireplaceProcess = Process(target = flickering.run)
lightProcess = Process(target = lightsense.run)
tempProcess = Process(target = tempsense.run)

def menuOne():
    sleep(1)
    oneOn = False
    # While the menu is equal to one
    while True:
        # Print the option title to the LCD
        lcd.lcd_string("LED",lcd.LCD_LINE_1)
        lcd.lcd_string("OFF",lcd.LCD_LINE_2)
        while True:
            # While option is off
            while oneOn == False:
                # If the first button is pressed
                while GPIO.input(26) == True:
                    # Change the setting on the LCD to "ON"
                    print('DEBUG: LED turned on')
                    lcd.lcd_string("ON",lcd.LCD_LINE_2)
                    # Wait for one second
                    sleep(1)
                    # Set the ON/OFF variable to True
                    oneOn = True
                    # Turn on the device
                    lightProcess.start()
                # If the second button is pressed
                print('DEBUG: Scroll through options')
                if GPIO.input(19) == True:
                    # Change the menu item variable to 2
                   # menu = 2
                    print ("Switching to menu 2")
                    menuTwo()
                    #print menu
                    # Wait for one second
                    print('DEBUG: Wait for one second...')
                    sleep(1)

             # While the option is turned on
            while oneOn == True:
                # When the first button is pressed
                print('DEBUG: First button pressed')
                while GPIO.input(26) == True:
                    # Change the option to "OFF" on the LCD
                    lcd.lcd_string("OFF",lcd.LCD_LINE_2)
                    # Wait for one second
                    sleep(1)
                    # Set the option variable to False
                    oneOn = False
                    # Turn off the device
                    print('DEBUG: LED turned off')

                # If the second button is pressed
                if GPIO.input(19) == True:
                    # Set the menu variable to 2
                    #menu = 2
                    print ("Switching to menu 2")
                    menuTwo()
                    #print menu
                    # Wait for one second
                    sleep(1)
                    print('DEBUG: switching menu')
def menuTwo():
    sleep(1)
    twoOn = False
    # While the menu is equal to one
    while True:
        # Print the option title to the LCD
        lcd.lcd_string("Fireplace",lcd.LCD_LINE_1)
        lcd.lcd_string("OFF",lcd.LCD_LINE_2)
        while True:
            # While option is off
            while twoOn == False:
                # If the first button is pressed
                print('DEBUG: first button pressed')
                while GPIO.input(26) == True:
                    # Change the setting on the fireplace to "ON"
                    lcd.lcd_string("ON",lcd.LCD_LINE_2)
                    # Wait for one second
                    sleep(1)
                    # Set the ON/OFF variable to True
                    oneOn = True
                    # Turn on the device
                    print('DEBUG: fireplace on')
                    fireplaceProcess.start()
                # If the second button is pressed
                if GPIO.input(19) == True:
                    # Change the menu item variable to 2
                   # menu = 2
                   print('DEBUG: Menu change')
                   print ("Switching to menu 3")
                   menuThree()
                   #print menu
                   # Wait for one second
                   sleep(1)

             # While the option is turned on
            while twoOn == True:
                # When the first button is pressed
                while GPIO.input(26) == True:
                    # Change the option to "OFF" on the LCD
                    lcd.lcd_string("OFF",lcd.LCD_LINE_2)
                    # Wait for one second
                    sleep(1)
                    # Set the option variable to False
                    oneOn = False
                    # Turn off the device
                    print('DEBUG: Fireplace off')

                # If the second button is pressed
                if GPIO.input(19) == True:
                    # Set the menu variable to 2
                    #menu = 2
                    print ("Switching to menu 3")
                    menuThree()
                    #print menu
                    # Wait for one second
                    sleep(1)
                    print('DEBUG: Menu change')

def menuThree():
    sleep(1)
    threeOn = False
    # While the menu is equal to one
    while True:
        # Print the option title to the LCD
        lcd.lcd_string("Fan/Temperature",lcd.LCD_LINE_1)
        lcd.lcd_string("OFF",lcd.LCD_LINE_2)
        while True:
            # While option is off
            while threeOn == False:
                # If the first button is pressed
                while GPIO.input(26) == True:
                    # Change the setting on the LCD to "ON"
                    lcd.lcd_string("ON",lcd.LCD_LINE_2)
                    # Wait for one second
                    sleep(1)
                    # Set the ON/OFF variable to True
                    oneOn = True
                    # Turn on the device
                    tempProcess.start()
                    print('DEBUG: temperature sensing/fan on')
                # If the second button is pressed
                if GPIO.input(19) == True:
                    # Change the menu item variable to 2
                   # menu = 2
                    print ("Switching to menu 1")
                    menuOne()
                    #print menu
                    # Wait for one second
                    sleep(1)
                    print('DEBUG: Switch menu')

             # While the option is turned on
            while threeOn == True:
                # When the first button is pressed
                while GPIO.input(26) == True:
                    # Change the option to "OFF" on the LCD
                    lcd.lcd_string("OFF",lcd.LCD_LINE_2)
                    # Wait for one second
                    sleep(1)
                    # Set the option variable to False
                    oneOn = False
                    # Turn off the device
                    print('DEBUG: Fan turned off')

                # If the second button is pressed
                if GPIO.input(19) == True:
                    # Set the menu variable to 2
                    #menu = 2
                    print ("Switching to menu 1")
                    menuTwo()
                    #print menu
                    # Wait for one second
                    sleep(1)
                  

lcd.lcd_string(" ",lcd.LCD_LINE_1)
lcd.lcd_string(" ",lcd.LCD_LINE_2)
try:
    menuOne()
    print('DEBUG: KeyboardInterrupt')
except KeyboardInterrupt:
    GPIO.cleanup()
    lcd.lcd_string(" ",lcd.LCD_LINE_1)
    lcd.lcd_string(" ",lcd.LCD_LINE_2)
