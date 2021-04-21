import gps #importo libreria gps q se encuentra en el directorio CanSat21 y contiene la inicialización del gps, librerías etc...
import serial #importo el serial para comunicarme con el pc y funcionen así los print.
from time import sleep # de la libreria tiempo importo la función dormmir (esperar)
gps.init() #inicializo el gps con la declaración hecha en la libreria gps.py
while True: #mientras verdad q se cumple siempre.
        print (gps.time()) #imprimimos la info de tiempo del gps.
        print (gps.speed_knots())  #imprimimos la info de velocidad q  nos da el gps
        print (gps.coordenadas()) #imprimimos las cooordenadas q nos da el gps
        print (gps.altitude()) #imprimimos la altitud
        print (gps.satellites()) # imprimimos el numero de satelites  q nos da el gps
        sleep(2) #esperar 2 segundos
        line = gps.readline() # decalramos line como leer la line del gps q esta declarado en la libreria gps.py
        data = line.split(" , ") #declaro data como coger line y  hacer una lista con los elementos que van entre comas de line
        if data[0] == "$GPGGA": # declaro una función de que solo si el primer hueco de la lista es $GPGGA ya que es el valor del q gps q nos interesa.
                if data[6] == "1": #otra condición, en el hueco 6 puede haber un 1 o un 0, si es 0 es q los datos son erroneos y 1 son los buenos, solo nos intersa los correctos
                         print  "Latitude: %s " % ( data[2] ) # imprimir "" como hueco 2 de la lista. En este y los siguientes comentarios con "" me refiero a lo q va entre "" despues de print, en este caso sería longitud.
                        print "Longitud: %s" % ( data[3] ) # imprimir "" como hueco 3 de la lista. 
                        print "Hora: %s" % ( data[1] ) # imprimir "" como hueco 1 de la lista.
                        print  "Datos válidos(1): %s" % ( yes ) # imprimir "" como hueco 6 de la lista.
                        print  "Número de satétiles: %s" % ( data[7] ) # imprimir "" como hueco 7 de la lista.
                        print "Dilución horizontal de precisión: %s" % ( data[8] ) # imprimir "" como hueco 8 de la lista.
                        print "altitud: %s" % ( data[9] ) # imprimir "" como hueco 9 de la lista.
                        print "Número de errores de transmisión: %s" % ( data[14] ) # imprimir "" como hueco 14 de la lista.
# cada hueco se puede ver q es buscando lo que significa el sistema de localización $GPGGa y cada hueco corresponde al valor entre comas.
                        with open ("datosgps.txt", "w") as dato: # crar un fichero datosgps.txt con  "w" que es written option

                        dato.write(  "Latitude: %s " % ( data[2] ))  # escribir en el archivo la latitud
                        dato.write("Longitud: %s" % ( data[3] )) # escribir en el archivo la longitud 
                        dato.write("Hora: %s" % ( data[1] )) # escribir en el archivo la hora
                        dato.write("Datos válidos(1): %s" % ( yes )) # escribir en el archivo  si los datos son válidos 
                        dato.write("Número de satétiles: %s" % ( data[7] )) # escribir en el archivo el numero de satelites al que el gps esta conectado
                         dato.write("Dilución horizontal de precisión: %s" % ( data[8] )) # escribir en el archivo  la HDOP (incertidumbre en la posición horizontal del gps) 
                        dato.write("altitud: %s" % ( data[9] )) # escribir en el archivo la altitud
                        dato.write("Número de errores de transmisión: %s" % ( data[14] )) # escribir en el archivo  el numero de errores de transmision
			#dato.close() #cerramos el archivo y que guarde la ifno, en este caso no hace falta porque con la opción "w" lo llama automáticamente.

