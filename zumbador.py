import zumbadorlibreria.py
import sensor.py
import RPi.GPIO as GPIO
import time
altura_dif = 10
last_altura = sensor.altitud()
while True:
    time.sleep(40)
    altura = sensor.altitud()
    diferencia = altura - last_altura
    if diferencia > 0 :
        if diferencia < altura_dif:
            GPIO.setmode(GPIO.BOARD)
            zumbadorlibreria.midi()
            GPIO.cleanup()
