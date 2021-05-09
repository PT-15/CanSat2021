import busio
import board
import serial

uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=3000)
outputLog = open ('gpsInfo.txt', 'at')
outputLog.write("START\n")

while True:
	line = uart.readline()
	outputLog.write(str(line) + "\n")
	outputLog.flush()
