import RPi.GPIO as GPIO
from random import randint

def run():
    GPIO.setmode(GPIO.BCM)
    # set up the fireplace LED
    print('DEBUG: Fireplace LED set uo')
    PIN_FIREPLACE = 16
    GPIO.setup(PIN_FIREPLACE, GPIO.OUT)
    fire = GPIO.PWM(PIN_FIREPLACE, 30)
    fire.start(0)
    
    # flickering effect
    print('DEBUG: Flickering code')
    try:
        while 1:
            r=randint(0,100)
            fire.ChangeDutyCycle(r)
               
    except KeyboardInterrupt:
        GPIO.cleanup()
