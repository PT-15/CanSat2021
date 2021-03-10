import sensor
import time
import picamera

#camera.start_preview()

picamera.camera.resolution = (1920,1272)
picamera.camera.annotate_text_size = 18
#picamera.camera.annotate_background = color('blue')
#picamera.camera.annotate_foreground = Color('yellow')
picamera.camera.annotate_text = "Las Rozas"

lastAlt = 0
alt = sensor.altitud
variacionMin = 1 #Poner variación mínima del sensor

while variacionMin < lastAlt - alt: # and lastAlt - alt != 0:
	camera.capture('/home/pi/Desktop/altitud%0.2.jpg' %sensor.altitud) 
	lastAlt = sensor.altitud
	time.sleep (5)
	alt = sensor.altitud
