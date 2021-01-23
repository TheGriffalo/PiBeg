import os
from picamera import PiCamera
import time

    

if not os.path.exists("/home/pi/Documents/Python_programs/Snaps"):
    os.mkdir ("/home/pi/Documents/Python_programs/Snaps")
else:
    print("Directory already exists.")


camera = PiCamera()
camera.resolution = (1280, 720)
camera.rotation = 90
time.sleep(2)

counter = 1

while True:
    file_name = "/home/pi/Documents/Python_programs/Snaps/img" + str(counter) + ".jpg"
    counter += 1
    camera.capture(file_name)
    print("New photo has been taken")
    time.sleep(5)

print("Done!")