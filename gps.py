#Librería para el GPS

#fecha, sello de tiempo, coordenadas, fix quality, satelites, altitud, velocidad

import time
import board
import busio
import serial

import adafruit_gps

gps = None
outputLog = None

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

def fecha():
	return "%d/%d/%d" % (gps.timestamp_utc.tm_mday, gps.timestamp_utc.tm_mon, gps.timestamp_utc.tm_year)

def timeStamp():
	return "%s:%s:%s" % (gps.timestamp_utc.tm_hour, gps.timestamp_utc.tm_min, gps.timestamp_utc.tm_sec)

def coordenadas():
	return "%s %s" % (gps.latitude, gps.longitude)

def fixQuality():
	return "%s" % (gps.fix_quality)

def satelites():
	if gps.satellites:
		return "%s" % (gps.satellites)

def altitud():
	if gps.altitude_m:
		return "%s" % (gps.altitude_m)

def velocidad():
	if gps.speed_knots:
		return "%s" % (gps.speed_knots)

def writeLogLine():
	outputLog.write("Datos:")
	outputLog.write("".join([chr(gps.coordenadas)]
	outputLog.write(fixQuality())
	outputLog.write(str(satelites()))
	outputLog.write(str(altitud()))
	outputLog.write(str(velocidad()))
#Fecha y hora borradas
	outputLog.flush()

def close():
	outputLog.close()
