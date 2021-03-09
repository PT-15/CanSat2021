#Librería para el GPS

#fecha, sello de tiempo, coordinadas, fix quality, satelites, altitud, velocidad

import time
import board
import busio

import adafruit_gps

gps = None
outputLog = None

def init():
	global gps
	global outputLog

	RX = board.RX
	TX = board.TX

	uart = busio.UART(TX, RX, baudrate = 9600, timeout = 3000)

	gps = adafruit_gps.GPS (uart)

	#Configurar datos GPS
	gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")

	#Update every second
	gps.send_command (b"PMTK220,1000")

	last_print = time.monotonic()

	outputLog = open ('gps.txt0', 'a')

def fecha():
	return "%/%/%" % (ps.timestamp_utc.tm_mday, gps.timestamp_utc.tm_mon, gps.timestamp_utc.tm_year)

def timeStamp():
	return "%:%:%" % (gps.timestamp_utc.tm_hour, gps.timestamp_utc.tm_min, gps.timestamp_utc.tm_sec)

def coordenadas():
	return "%0.6f %0.6f" % (gps.latitude, gps.longitude)

def fixQuality():
	return "%" % (gps.fix_quality)

def satelites():
	if gps.satellites is not None:
		return "%" % (gps.satellites)

def altitud():
	if gps.altitude_m is not None:
		return "%" % (gps.altitude_m)

def velocidad():
	if gps.speed_knots is not None:
		return "%" % (gps.speed_knots)

def writeLogLine():
	outputLog.write(coordenadas())
	outputLog.flush()

def close():
	outputLog.close()
