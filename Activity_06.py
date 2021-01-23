import RPi.GPIO as GPIO
import time

RED_LED_PIN = 17
BLUE_LED_PIN = 27
YELLOW_LED_PIN = 22
SW_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW_PIN, GPIO.IN)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_LED_PIN, GPIO.OUT)

GPIO.output(RED_LED_PIN, GPIO.LOW)
GPIO.output(BLUE_LED_PIN, GPIO.LOW)
GPIO.output(YELLOW_LED_PIN, GPIO.LOW)

last_colour = "yellow"
previous_button_state = GPIO.input(SW_PIN)

while True:
    #print(GPIO.input(SW_PIN))
    time.sleep(0.1)
    button_state = GPIO.input(SW_PIN)
    if button_state != previous_button_state:
        previous_button_state = button_state
        if button_state == GPIO.HIGH:
            if (last_colour == "yellow"):
                GPIO.output(RED_LED_PIN, GPIO.HIGH)
                GPIO.output(BLUE_LED_PIN, GPIO.LOW)
                GPIO.output(YELLOW_LED_PIN, GPIO.LOW)
                last_colour = "red"
        
            elif (last_colour == "red"):
                GPIO.output(RED_LED_PIN, GPIO.LOW)
                GPIO.output(BLUE_LED_PIN, GPIO.HIGH)
                GPIO.output(YELLOW_LED_PIN, GPIO.LOW)
                last_colour = "blue"
        
            else:
                GPIO.output(RED_LED_PIN, GPIO.LOW)
                GPIO.output(BLUE_LED_PIN, GPIO.LOW)
                GPIO.output(YELLOW_LED_PIN, GPIO.HIGH)
                last_colour = "yellow"
        
    
    
GPIO.cleanup()