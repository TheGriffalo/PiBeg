import RPi.GPIO as GPIO
import time

LED_PIN = 17
SW_PIN = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SW_PIN, GPIO.IN)


#State 0 = power off
#State 1 = power on

state = int(input("Enter 0 to power off the LED, 1 to power on the LED: "))

if (state == 0):
    GPIO.output(LED_PIN, GPIO.LOW)
elif (state == 1):
    GPIO.output(LED_PIN, GPIO.HIGH)
else:
    print("Wrong state value : ", state)
    GPIO.cleanup()
    exit

time.sleep(5)

    

GPIO.cleanup()