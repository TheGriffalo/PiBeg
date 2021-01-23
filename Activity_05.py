import RPi.GPIO as GPIO
import time

LED_PIN = 17
SW_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    print(GPIO.input(SW_PIN))
    if ((GPIO.input(SW_PIN)) == 1):
        GPIO.output(LED_PIN, GPIO.HIGH)
        
    else:
        GPIO.output(LED_PIN, GPIO.LOW)
        
    time.sleep(0.1)
    
GPIO.cleanup()