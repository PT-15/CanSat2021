import time

#Programas que se encargan de manejar los módulos
import radio
import sensor
import gps

def main():

	#Inicialización de los módulos
	radio.init()
	sensor.init()
	gps.init()

	while True:
		#Graba los datos a la microSD
		sensor.writeLogLine()
		gps.writeLogLine()

		#Envía los datos por radio
		packet = bytes(sensor.line(), "utf-8")

			#Paquetiza la información para que no supere el tamaño de 60
		while len(packet) > 60:
			radio.rfm69.send(packet[:60])
			packet = packet[60:]

		if len(packet) > 0:
			radio.rfm69.send(packet)

		if gps.fix():
			infoGps = bytes(gps.line(), "utf-8")

			while len(infoGps) > 60:
				radio.rfm69.send(infoGps[:60])
				infoGps = infoGps[60:]

			if len(infoGps) > 0:
				radio.rfm69.send(infoGps)
		else:
			infoGps = bytes(gps.fixQuality(), "utf-8")
			radio.rfm69.send(infoGps)

		time.sleep(0.5)

	radio.close()
	sensor.close()
	gps.close()


try:
	main()

except KeyboardInterrupt:
	radio.close()
	sensor.close()
	gps.close()
	print("Out")
