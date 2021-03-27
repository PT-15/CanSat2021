import sensor
from picamera import PiCamera
import time

sensor.init()
camera = PiCamera()


camera.resolution = (1920, 1272)


lastAlt = 2000
alt = sensor.altitud()
difference = lastAlt - alt
variation = 0.5

while difference >= variation:
	alt = sensor.altitud()
	camera.capture('/home/pi/Desktop/photo_%0.2f.jpg' % time.time())
	difference = lastAlt - alt
	lastAlt = alt
	print ("*click*")
	time.sleep(5)

