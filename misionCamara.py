import sensor
from picamera import PiCamera
import time

sensor.init()
camera = PiCamera()


camera.resolution = (1920, 1272)


lastShotAlt = sensor.altitud()
maxAltDiff = 3 #Set real max time diff

lastShotTimestamp = time.time()
maxTimeDiff = 2

altVariationMin = 0.5

while True:
	timestamp = time.time()
	alt = sensor.altitud()

	altDiff = alt - lastShotAlt
	timeDiff = timestamp - lastShotTimestamp

	if timeDiff >= maxTimeDiff:
		if altDiff <= altVariationMin and altDiff >= -0.5:
			exit()
		else: 
			camera.capture('/home/pi/Desktop/photoTime_%0.2f.jpg' % time.time())
			lastShotAlt = sensor.altitud()
			lastShotTimestamp = time.time()
			continue
	else: 
		if altDiff >= maxAltDiff:
			camera.capture('/home/pi/Desktop/photoFall_%0.2f.jpg' % time.time())
			lastShotAlt = sensor.altitud()
			lastShotTimestamp = time.time()
		else: 
			continue