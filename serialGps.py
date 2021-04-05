import busio
import board
import serial
import time

uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=3000)
outputLog = open ('gpsInfo%0f.txt' % time.time(), 'a')
n = 0

while True:

	line = uart.read_until()
	outputLog.write("%s" % line)
	n += 1
	if n >= 10:
		outputLog.flush()
