import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.HIGH)
sleep(0.5)	# Waits for half a second
GPIO.output(22, GPIO.LOW)

GPIO.cleanup()
