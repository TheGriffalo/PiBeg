import RPi.GPIO as GPIO
import time
from picamera import PiCamera

def take_photo(camera):
    file_name = "/home/pi/Camera/img_" + str(time.time()) + ".jpg"
    camera.capture(file_name)
    return file_name

PIR_PIN = 4
BLUE_LED_PIN = 27

#Setup camera
camera = PiCamera()
camera.resolution = (720, 480)
camera.rotation = 90
print("Waiting two seconds to initialise the camera...")
time.sleep(2)
print("Camera setup OK")

#Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)
GPIO.output(BLUE_LED_PIN, GPIO.LOW)

MOV_DETECT_THRESHOLD = 3.0
MIN_DURATION_BETWEEN_PHOTOS = 30.0
last_pir_state = GPIO.input(PIR_PIN)
movement_timer = time.time()
last_time_photo_taken = 0

try:
    while True:
        time.sleep(0.01)
        pir_state = GPIO.input(PIR_PIN)
        if pir_state == GPIO.HIGH:
            GPIO.output(BLUE_LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(BLUE_LED_PIN, GPIO.LOW)
        if last_pir_state == GPIO.LOW and pir_state == GPIO.HIGH:
            movement_timer = time.time()
        if last_pir_state == GPIO.HIGH and pir_state == GPIO.HIGH:
            if time.time() - movement_timer > MOV_DETECT_THRESHOLD:
                if time.time() - last_time_photo_taken > MIN_DURATION_BETWEEN_PHOTOS:
                    print("Take photo and send by email")
                    take_photo(camera)
                    last_time_photo_taken = time.time()
        last_pir_state = pir_state
            
except KeyboardInterrupt:
    GPIO.cleanup()