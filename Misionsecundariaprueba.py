#másinfo en https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2
import sensor
import time
import picamera
import adafruit_gps
import board
import busio
import serial

camera.start_preview()

camera.resolution = (1920,1272)
camera.annotate_text_size = 18
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text = "Las Rozas a 1km de altitud"

lastAlt = None
alt = sensor.altitud
variacionMin = None #Poner variación mínima del sensor

while variacionMin <= lastAlt - alt and lastAlt - alt != 0:
	camera.capture('/home/pi/Desktop/altitud%0.2.jpg' %sensor.altitud) 
	lastAlt = sensor.altitud
	time.sleep (5)
	alt = sensor.altitud
	
#código gps
uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=3) #el timeout3 es el tiempo de espera para la información, en este caso 3 segundos. NOTA: debe ser mayor que la tasa de refresco de la línea 35
#cambiando /dev/ttyUSB0al puerto serie apropiado para la rasberry pi3; mas info en: https://learn.adafruit.com/adafruit-ultimate-gps/circuitpython-python-uart-usage
i2c = board.I2C() #si usas la interfaz I2C; creo q es la de la placa adafruit
gps = adafruit_gps.GPS_GtopI2C (i2c, debug = False) #i2c es porque usamos la interfaz I2C; ssi fuese raspberry gps = adafruit_gps . GPS ( uart , debug = False )
gps.send_command (b'PMTK314,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ') #envía solo la ubicaión.
# gps.send_command (b'PMTK314,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ')  se usa para apagar todo.
gps . send_command ( b "PMTK220,1000" ) # establece la tasa de refresco a 1hz , es decir, se actualiza cada segundo. NOTA La tasa de actualización de la línea 29 tiene que ser mayor.
# También puede acelerar la tasa, pero no vaya demasiado rápido o puede perder datos durante el análisis. EJ:dos veces por segundo (2 Hz, 500 ms de retraso)
last_print = time.monotonic() #Asegúrese de llamar a gps.update () cada iteración del ciclo y al menos dos veces tan rápido como los datos provienen de la unidad GPS (generalmente cada segundo).Esto devuelve un bool que es verdadero si analizó nuevos datos (puede ignorarlo aunque si no le importa y en su lugar mira la propiedad has_fix).
while True:
	gps.update()
	current = time.monotonic() 
    if current - last_print >= 1.0:  # cada segundo imprimir la ubicación
        last_print = current
        if not gps.has_fix:  #si no hay gps, intentarlo de nuevo
		 print("Waiting for fix...")
          	  continue
	print("=" * 40)  #imprime línea de separación
        print(
            "Fix timestamp: {}/{}/{} {:02}:{:02}:{:02}".format(   # corregir maraca de tiempo
                gps.timestamp_utc.tm_mon,  #?
                gps.timestamp_utc.tm_mday,  #?
                gps.timestamp_utc.tm_year,  #?
                gps.timestamp_utc.tm_hour,  #?
                gps.timestamp_utc.tm_min,  #?
                gps.timestamp_utc.tm_sec, #?
            )
        )
        print("Latitude: {0:.6f} degrees".format(gps.latitude))
        print("Longitude: {0:.6f} degrees".format(gps.longitude)) #algunos datos excepto la latitud, longitud y la marca del tiempo son opcionales.
        print("Fix quality: {}".format(gps.fix_quality))
# comprobar antes de usar que todos los datos estan pressentes.
	if gps.satellites is not None:
            print("# satellites: {}".format(gps.satellites))
        if gps.altitude_m is not None:
            print("Altitude: {} meters".format(gps.altitude_m))
        if gps.speed_knots is not None:
            print("Speed: {} knots".format(gps.speed_knots))
        if gps.track_angle_deg is not None:
            print("Track angle: {} degrees".format(gps.track_angle_deg))
        if gps.horizontal_dilution is not None:
            print("Horizontal dilution: {}".format(gps.horizontal_dilution))
        if gps.height_geoid is not None:
            print("Height geo ID: {} meters".format(gps.height_geoid))



 
 
