import time
import radio
import sensor

radio.init()
sensor.init()

gpsLines = []
gpsPacket = []
i = 0

def main():
	while True:
		sensor.writeLogLine()

		#Se escribe en la lista gpsPacket las líneas a enviar
		with open ('gpsInfo.txt', 'rt') as gpsFile:
			for line in gpsFile:
				gpsLines.append(line)

		gpsPacket.clear()

		for x in gpsLines[i:]
			gpsPacket.append(x)
			i += 1
		
		lines.clear()

		#Envía los datos por radio
		packet = bytes(sensor.line(), "utf-8")
		gpsSend = bytes(gpsPacket, "utf-8")

			#Paquetiza la información para que no supere el tamaño de 60
		while len(packet) > 60:
			radio.rfm69.send(packet[:60])
			packet = packet[60:]

		if len(packet) > 0:
			radio.rfm69.send(packet)

		while len(gpsSend) > 60:
			radio.rfm69.send(gpsSend[:60])
			gpsSend = gpsSend[60:]

		if len(gpsSend) > 0:
			radio.rfm69.send(gpsSend)

		time.sleep(0.1)

	radio.close()
	sensor.close()


try:
	main()

except KeyboardInterrupt:
	radio.close()
	sensor.close()
	print("Out")