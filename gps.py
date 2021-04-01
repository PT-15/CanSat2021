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

	outputLog = open ('gps.txt', 'a')


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
	return fixQuality(), timeStamp(), satelites(), coordenadas(), altitud(), velocidad()

def writeLogLine():
	if fix():
		outputLog.write(line())
		outputLog.flush()
	else:
		outputLog.write("No fix")


def close():
	outputLog.close()