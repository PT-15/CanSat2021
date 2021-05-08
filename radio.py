'''
Funciones librería
	.init (inicializar modulo radio)
	.close (vaciar pantalla antes de cerrar programa)
'''


import time
# Libreria protocolos serie
import busio
# GPIO
from digitalio import DigitalInOut, Direction, Pull
import board
# Pantalla OLED
import adafruit_ssd1306
# Modulo radio
import adafruit_rfm69

display = None
rfm69 = None
btnA = None
btnB = None

#Inicializa el módulo de radio (incluyendo la pantalla y los botones)
def init():
	global display
	global rfm69
	global btnA
	global btnB

	# I2C
	i2c = busio.I2C(board.SCL, board.SDA)

	# OLED Display
	reset_pin = DigitalInOut(board.D4)
	display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, reset=reset_pin)

	#Vaciar display
	display.fill(0)
	display.show()
	width = display.width
	height = display.height

	#Modulo radio
	CS = DigitalInOut(board.CE1)
	RESET = DigitalInOut(board.D25)
	spi =busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
	rfm69 = adafruit_rfm69.RFM69(spi, CS, RESET, 433.0)
	rfm69.encryption_key = b'\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08'

	# Button A
	btnA = DigitalInOut(board.D5)
	btnA.direction = Direction.INPUT
	btnA.pull = Pull.UP

	# Button B
	btnB = DigitalInOut(board.D6)
	btnB.direction = Direction.INPUT
	btnB.pull = Pull.UP

	# Button C
	btnC  = DigitalInOut(board.D12)
	btnC.direction = Direction.INPUT
	btnC.pull = Pull.UP


def close():
	display.fill(0)
	display.show()
