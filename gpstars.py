import radio

sensorLog = None
gpsLog = None

def main():
	radio.init()
	i = 0

	sensorLog = open('dataTARS.txt', 'at')
	gpsLog = open('gpsData.txt', 'a')

	while True:
		packet = radio.rfm69.receive(timeout = 2)

		if packet is None:
			print ("No packet")
			radio.display.fill(0)
			radio.display.text('No packet', 25, 15, 1)
			radio.display.show()
		else:
			dataLine = packet.decode()

			fields = dataLine.split (' ')

			for x in fields:
				if x[:5] == '16204':
					gpsLog.flush()
					sensorLog.write(x + " ")
					i += 1

				elif i > 0:
					if i == 4:
						sensorLog.write(x + "\n")
						sensorLog.flush()
						i = 0
					else:
						sensorLog.write(x + " ")
						i += 1
				else:
					gpsLog.write(x + "\n")



			'''


			radio.display.fill(0)
			radio.display.text('%0.2f  P:%0.1f hPa' % (float(fields[0]), float(fields[3])), 2, 2, 1)
			radio.display.text('T:%0.1f C  Hum:%0.2f%%' % (float(fields[1]), float(fields[2])), 2, 13, 1)
			radio.display.text('Alt:%0.2fm' % (float(fields[4])), 2, 25, 1)
			radio.display.show()
			'''

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

