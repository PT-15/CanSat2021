import time

import radio
import sensor
import gps

def main():
	radio.init()
	sensor.init()
	gps.init()

	while True:
		sensor.writeLogLine()
		gps.writeLogLine()
		packet = bytes(sensor.line(), "utf-8")
		radio.rfm69.send(packet)
#Dividir en paquetes y enviar sensor y gps juntos. Usar timestamp del gps para sensor
#		packet = bytes(gps.line(), "utf-8")
#		radio.rfm69.send(packet)
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
