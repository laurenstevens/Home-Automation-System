# Import both required libraries
print('DEBUG:Importing required libraries')
import RPi.GPIO as GPIO, time
import sys, signal

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)
#print(DEBUG: 'GPIO mode to BCM')

# Discharge the cap and measure the time it takes to recharge
def RCtime (PiPin):
    measurement = 0
    print('DEBUG: Measuring how long it takes for the capacitor to charge')
  # Discharge capacitor
    GPIO.setup(PiPin, GPIO.OUT)
    GPIO.output(PiPin, GPIO.LOW)
    print('DEBUG: Discharge the capacitor')
  # Wait to ensure complete discharge
    time.sleep(1)
    print('DEBUG: Ensuring the capacitor has discharged')

  # Measure time it takes to recharge capacitor
    print('DEBUG: Measure time takes to recharge the capacitor')
    GPIO.setup(PiPin, GPIO.IN)

    while (GPIO.input(PiPin) == GPIO.LOW):
    # Increase the measurement whilst capacitor is not charged
        print('DEBUG: Increase the measurement whilst the capacitor is not charged')
        measurement += 1
  
  # Return the time taken
  #print('DEBUG: Return time taken...')
    return measurement
def run():
    try:
        #Always...
        while True:
            #Setup GPIO6 as output
            print('DEBUG: Set GPIO pin 6 as output')
            GPIO.setup(6, GPIO.OUT)
            #Print the value
            print('DEBUG: Print value')
            print(RCtime(14))
            #If the value is under 250000 (too warm)
            if RCtime(14) < 250000:
                #Turn on the fan
                print('DEBUG: If under 250000, turn fan on')
                GPIO.output(6, True)
            #Otherwise...
            else:
                #Turn off the fan
                print ('DEBUG: Otherwise turn fan off')
                GPIO.output(6, False)
    
    #If Ctrl+C is pressed
#    print('DEBUG: KeyboardInterrupt')
    except KeyboardInterrupt:
        #Turn off all GPIO
        GPIO.cleanup()
