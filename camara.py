import sensor
from picamera import PiCamera
import time

sensor.init()
camera = PiCamera()


camera.resolution = (1920, 1272)


while True:
	camera.capture('/home/pi/Desktop/photoTime_%0.2f.jpg' % time.time())
	time.sleep(2)
