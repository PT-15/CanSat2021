import radio
import socket
from time import sleep

radio.init()

while True:

	if not radio.btnA.value: 
		hostName = socket.gethostname()
		ip_adress = socket.gethostbyname(hostName + ".local") 

		radio.display.fill(0)
		radio.display.text('IP: %s' %ip_adress, 5, 15, 1)
		radio.display.show()

		sleep(1)

		while True:
			if not radio.btnA.value:
				radio.display.fill(0)
				radio.display.show()
				quit()
