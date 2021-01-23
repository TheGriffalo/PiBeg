import RPi.GPIO as GPIO
import time

SW_PIN = 26

GPIO.setmode(GPIO.BCM)

#GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SW_PIN, GPIO.IN)

while True:
    print(GPIO.input(SW_PIN))
    time.sleep(1)


    

GPIO.cleanup()
