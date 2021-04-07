import gps
import serial
from time import sleep
gps.init()
while True:
        print (gps.time())
        print (gps.speed_knots())
        print (gps.coordenadas())
        print (gps.altitude())
        print (gps.satellites())
        sleep(2)
        line = gps.readline()
        data = line.split(" , ")
        if data[0] == "$GPGGA":
                if data[6] == "1":
                         print  "Latitude: %s " % ( data[2] )
                        print "Longitud: %s" % ( data[3] )
                        print "Hora: %s" % ( data[1] )
                        print  "Datos válidos(1): %s" % ( data [6] )
                        print  "Número de satétiles: %s" % ( data[7] )
                        print "Dilución horizontal de precisión: %s" % ( data[8] )
                        print "altitud: %s" % ( data[9] )
                        print "Número de errores de transmisión: %s" % ( data[14] )

                        with open ("datosgps.txt", "w") as dato:

                        dato.write(  "Latitude: %s " % ( data[2] ))
                        dato.write("Longitud: %s" % ( data[3] ))
                        dato.write("Hora: %s" % ( data[1] ))
                        dato.write("Datos válidos(1): %s" % ( data [6] ))
                        dato.write("Número de satétiles: %s" % ( data[7] ))
                         dato.write("Dilución horizontal de precisión: %s" % ( data[8] ))
                        dato.write("altitud: %s" % ( data[9] ))
                        dato.write("Número de errores de transmisión: %s" % ( data[14] ))
