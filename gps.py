#Librería para el GPS

#fecha, sello de tiempo, coordenadas, fix quality, satelites, altitud, velocidad

import time
import board
import busio
import serial

import adafruit_gps

gps = None
outputLog = None

#Inicializa el gps
def init():
	global gps
	global outputLog

	uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=3000)

	gps = adafruit_gps.GPS (uart)

	#Configurar datos GPS
	gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")

	#Update every second
	gps.send_command (b"PMTK220,1000")

	outputLog = open ('dataGPS.txt', 'a')

def fixQuality():
	return gps.fix_quality

def fix():
	gps.update()
	if not gps.has_fix:
		return False

def line():
	return "%d %f %d %0.6f %0.6f %f %f\n" % (gps.fix_quality, gps.timestamp_utc, gps.satellites, gps.latitude[0:], gps.longitude[0:], gps.altitude_m, gps.speed_knots)

def writeLogLine():
	if fix():
		outputLog.write(line())
	else:
		outputLog.write("%d" % gps.fix_quality)
		outputLog.write("\n")

	outputLog.flush()


def close():
	outputLog.close()
'''
def fixQuality():
	return ("%d") % gps.fix_quality

def fix():
	gps.update()
	print(fixQuality())
	if not gps.has_fix:
		return False
	else:
		return True



def timeStamp():
	return "%02d : %02d : %02d" % (gps.timestamp_utc.tm_hour, gps.timestamp_utc.tm_min, gps.timestamp_utc.tm_sec)

def fecha():
	return "%d/%d/%d" % (gps.timestamp_utc)

def coordenadas():
	return "%0.6f %0.6f" % (gps.latitude[0:], gps.longitude[0:])

def satelites():
	if gps.satellites:
		return "%d" % gps.satellites
	else:
		return -1

def altitud():
	if gps.altitude_m:
		return "%f" % gps.altitude_m
	else:
		return -1

def velocidad():
	if gps.speed_knots:
		return "%f" % gps.speed_knots
	else:
		return -1.0

def line():
<<<<<<< HEAD
	return "%d %f %f %f %f %f\n" % (fixQuality(), timeStamp(), satelites(), coordenadas(), altitud(), velocidad())
=======
	return fixQuality(), timeStamp(), satelites(), coordenadas(), altitud(), velocidad()
>>>>>>> b12f5433323416f8efd5b1f8a24d2ffabead6973

def writeLogLine():
	if fix():
		outputLog.write(line())
	else:
		outputLog.write(fixQuality())
		outputLog.write("\n")

	outputLog.flush()

def close():
	outputLog.close()
'''
