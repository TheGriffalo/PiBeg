import RPi.GPIO as GPIO
import time

PIR_PIN = 4
BLUE_LED_PIN = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)
GPIO.output(BLUE_LED_PIN, GPIO.LOW)

while True:
    time.sleep(0.1)
    if (GPIO.input(PIR_PIN)) == GPIO.HIGH:
        GPIO.output(BLUE_LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(BLUE_LED_PIN, GPIO.LOW)
        


GPIO.cleanup()