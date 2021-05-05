import radio

sensorLog = None
gpsLog = None

def main():
	radio.init()

	sensorLog = open('dataTARS.txt', 'a')
	gpsLog = open('gpsData.txt', 'a')

	while True:
		packet = radio.rfm69.receive(timeout = 2)

		if packet is None:
			radio.display.fill(0)
			radio.display.text('No packet', 25, 15, 1)
			radio.display.show()
		else:
			dataLine = packet.decode()

			fields = dataLine.split (' ')

			i = 0

			for x in fields:
				if i <= 5:
					print(x + "\n")
					sensorLog.write(x)
					if i == 5:
						sensorLog.write("\n")
				else:
					gpsLog.write(x + "\n")
					print(x)

			radio.display.fill(0)
			radio.display.text('%0.2f  P:%0.1f hPa' % (fields[0], fields[3]), 2, 2, 1)
			radio.display.text('T:%0.1f C  Hum:%0.2f%%' % (fields[1], fields[2]), 2, 13, 1)
			radio.display.text('Alt:%0.2fm' % (fields[4]), 2, 25, 1)
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

