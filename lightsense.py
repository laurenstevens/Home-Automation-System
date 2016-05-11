# code to sense light

import RPi.GPIO as GPIO, time

# Tell the GPIO library to use
# Broadcom GPIO references
print('DEBUG: Set to BCM')
GPIO.setmode(GPIO.BCM)

# Define function to measure charge time
print('DEBUG: Measure charge time of capacitor')
def RCtime (PiPin):
  measurement = 0
  # Discharge capacitor
  print('Discharge the capacitor')
  GPIO.setup(PiPin, GPIO.OUT)
  GPIO.output(PiPin, GPIO.LOW)
  time.sleep(0.1)

  GPIO.setup(PiPin, GPIO.IN)
  # Count loops until voltage across
  # capacitor reads high on GPIO
  while (GPIO.input(PiPin) == GPIO.LOW):
    measurement += 1
  # return the time
  print('DEBUG: Return time taken')
  return measurement

def run():
    try:
        while True:
            # Print the current light level
            print('DEBUG: Printing current light level')
            print RCtime(21)
            
            # Setup GPIO 24 as an output
            print('DEBUG: GPIO output set as 24')
            GPIO.setup(20, GPIO.OUT)
            
            # If light level is above setpoint, turn off lights
            print('DEBUG: If light level is above setpoint, turn off LED')
            if RCtime(21) > 500:
                GPIO.output(20, True)
            # Otherwise turn them on
           # print('DEBUG: Otherwise turn the LED on')
            else:
                GPIO.output(20, False)
    
    # Stop the program on ctrl+c
    #print('DEBUG: KeyboardInterrupt, code stopped')
    except KeyboardInterrupt:
        GPIO.cleanup()

