import gps
from time import sleep

gps.init()

while True:
	print (gps.time())
	print (gps.coordenadas())
	print (gps.altitude())
	print (gps.satellites())
	sleep(1)
