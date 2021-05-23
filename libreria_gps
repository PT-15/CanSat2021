import RPi.GPIO as GPIO
import time

tonePin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(tonePin,GPIO.OUT)

def delay (times):
	time.sleep(times/1000.0)

def tone(pin, pitch, duration):
	GPIO.setup(tonePin, GPIO.OUT)
	if pitch == 0:
		delay(duration)
		return
	p = GPIO.PWM(tonePin, pitch)
	p.start(30)
	delay(duration)
	p.stop()
	delay(2)

def midi():
	tone(tonePin, 391.995, 500)
	tone(tonePin, 440.00, 500)
	tone(tonePin, 349.23, 500)
	tone(tonePin, 698.46, 500)
	tone(tonePin, 261.63, 1500)

while 1:
	GPIO.setmode(GPIO.BOARD)
	midi()
	GPIO.cleanup()
