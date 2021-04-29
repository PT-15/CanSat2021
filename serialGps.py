import busio
import board
import serial

uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=3000)
outputLog = open ('gpsInfo.txt', 'at')
outputLog.write("START\n")
n = 0

while True:

	line = uart.read_until()
	outputLog.write(str(line))
	n += 1
	if n >= 10:
		outputLog.flush()
		n = 0
