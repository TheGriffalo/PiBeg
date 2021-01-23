import RPi.GPIO as GPIO
import time

#RED_LED_PIN = 17
#BLUE_LED_PIN = 27
#YELLOW_LED_PIN = 22
LED_PIN_LIST = [17, 27, 22]
SW_PIN = 26

def power_on_selected_led(selected_led_pin):
    if selected_led_pin not in LED_PIN_LIST:
        return
    for pin in LED_PIN_LIST:
        if pin == selected_led_pin:
            GPIO.output(pin, GPIO.HIGH)
        else:
            GPIO.output(pin, GPIO.LOW)
            

GPIO.setmode(GPIO.BCM)

for pin in LED_PIN_LIST:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(SW_PIN, GPIO.IN)

for pin in LED_PIN_LIST:
    GPIO.output(pin, GPIO.LOW)


led_index = 0
previous_button_state = GPIO.input(SW_PIN)

while True:
    
    time.sleep(0.1)
    button_state = GPIO.input(SW_PIN)
    if button_state != previous_button_state:
        previous_button_state = button_state
        if button_state == GPIO.HIGH:
            power_on_selected_led(LED_PIN_LIST[led_index])
            led_index += 1
            if led_index >= len(LED_PIN_LIST):
                led_index = 0
            
        
    
    
GPIO.cleanup()