import radio


sensorLog = None
gpsLog = None

def main():
	radio.init()

	sensorLog = open('dataTARS.txt', 'a')
	gpsLog = open('gpsTARS.txt', 'a')

	while True:
		packet = radio.rfm69.receive(timeout = 2)

		if packet is None:
			radio.display.fill(0)
			radio.display.text('No packet', 25, 15, 1)
			radio.display.show()
		else:
			dataLine = packet.decode()

			fields = dataLine.split (' ')

			for i in range (5):
				print (i + "\n")
				sensorLog.write(str(i))
			sensorLog.write("\n")

			for i in dataLine:
				if i >= 5:
					print (fields[i] + "\n")

			timeStamp = float(fields[0])
			temperature = float(fields[1])
			humedad = float(fields[2])
			presion = float(fields[3])
			altitud = float(fields[4])
			fixQuality = float(fields[5])

			if fixQuality is not 0:
				

			if i is 0:
				startTime = timeStamp

			outputLog.write("xxx %f %f %f %f %f\n" % (timeStamp, temperature, humedad, presion, altitud))
			print("\nTime: %0.2f s" % (timeStamp - startTime))
			print("Temperature: %0.1f C" % temperature)
			print("Humedad: %0.1f %%" % humedad)
			print("Presión: %0.1f hPa" % presion)
			print("Altitud: %0.2f meters" % altitud)

			radio.display.fill(0)
			radio.display.text('%0.2f  P:%0.1f hPa' % (timeStamp - startTime, presion), 2, 2, 1)
			radio.display.text('T:%0.1f C  Hum:%0.2f%%' % (temperature, humedad), 2, 13, 1)
			radio.display.text('Alt:%0.2fm' % (altitud), 2, 25, 1)
			radio.display.show()


	radio.close()
	sensorLog.close()
	gpsLog.close()




try:
	main()

except KeyboardInterrupt:
	radio.close()
	sensorLog.close()
	gpsLog.close()
	print("Out")

