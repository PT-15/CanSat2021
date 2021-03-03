from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()

i = 0

while i<3:
	sleep(5)
	camera.capture('/home/pi/Desktop/image.jpg')
	camera.stop_preview()

camera.stop_preview()
