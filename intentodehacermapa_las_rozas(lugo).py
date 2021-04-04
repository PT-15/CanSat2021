import folium # libreria de mapas
mapa=folium.Map(location=[43.11436191191138, -7.460387189703997]), zoom_start=12, control_scale=True, tiles='Stamen Toner' #Tiles stamen toner es para que el relieve sea en blaco y negro # de la libreria poner la latitud y longitud (coordenadas) del mapa que vamos a hacer. Establece el zoom del mapa y el control_scale sirve para decir que muestre la escala.
mapa.save('C:\Users\Samu\Documents\CanSat2021\Progama_hacerunmapa//mapa_las_rozas.html') #donde guarda el mapa, establecer unas ruta de ordenador.Se guarda como html
