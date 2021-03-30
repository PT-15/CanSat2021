/* Tabla de datos de tiempo, temperatura, humedad, presión y altitud.*/
CREATE TABLE datos_satelite id INTEGER PRIMARY KEY AUTOINCREMENT, Tiempo INTEGER, Temperatura INTEGER, Humedad INTEGER, Presión INTEGER, Altitud INTEGER);
COPY datos_satelite FROM '/home/pi/CanSat2021/data.txt' DELIMETER ' ';
