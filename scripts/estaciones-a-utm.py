#!/usr/bin/env python3

import csv
import re

def decimal( cifras ):
    if ( len(cifras) < 4 ):
        cifras.append( 0 )
    return float(cifras[0])+float(cifras[1])/60+float("{cifras[2]}.{cifras[3]}".format(**locals()))/3600

rows = []
with open("../data/estaciones-medioambientales-madrid.csv") as origen:
    estacion_reader = csv.reader(origen,delimiter=";",quotechar='"')
    rows.append( next(estacion_reader) )
    for row in estacion_reader:
        cifras_long = re.findall(r"(\d+)",row[3])
        cifras_lat = re.findall(r"(\d+)",row[4])
        rows.append([row[0],row[1], row[2],decimal(cifras_long),decimal(cifras_lat),row[5]])

with open("estaciones-medioambientales-madrid-utm.csv", "w") as csvfile:
    estacion_writer=csv.writer(csvfile,delimiter=";",quotechar='"')
    estacion_writer.writerows( rows )
    
