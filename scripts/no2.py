#!/usr/bin/env python3

import requests
import csv

estaciones_dict ={}
with open("../data/estaciones-medioambientales-madrid-utm.csv", "r") as estaciones:
    estacion_reader= csv.reader(estaciones,delimiter=";",quotechar='"')
    next(estacion_reader)
    for estacion in estacion_reader:
        estaciones_dict[estacion[0]]={ "nombre": estacion[1],
                                       "long" : estacion[3],
                                       "lat" : estacion[4] }
        
medidas = requests.get('http://www.mambiente.munimadrid.es/opendata/horario.txt').text.split("\n")

datos_no2 = []

for medida in medidas:
    if medida: 
        datos = medida.split(",")
        if datos[3] == "08": # Entonces es NO2
            lecturas = datos[9:]
            for index, val in enumerate(lecturas):
                if index % 2 == 0 and float(val) > 0:
                    esta = estaciones_dict[str(int(datos[2]))]
                    datos_no2.append( [esta['nombre'],esta['long'],esta['lat'],int(index/2),float(val)])


with open("no2-madrid-ahora.csv", "w") as csvfile:
    parkingwriter=csv.writer(csvfile,delimiter=";",quotechar='"')
    parkingwriter.writerow(["nombre","long","lat","hora","NO2"])
    parkingwriter.writerows( datos_no2 )
            



