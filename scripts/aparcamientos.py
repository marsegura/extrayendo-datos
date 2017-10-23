#!/usr/bin/env python3

import csv
import requests
import re

aparcamientos = requests.get('http://datos.madrid.es/egob/catalogo/202625-0-aparcamientos-publicos.csv').text

parkingreader= csv.reader(aparcamientos.split("\n"),delimiter=';',quotechar='"')
no_vacios = list( filter( lambda p: p, parkingreader))
columnas = no_vacios[0]
publicos = list( filter( lambda p: re.search(r"público",p[1]), no_vacios))
with open("exclusivo-publicos.csv", "w") as csvfile:
    parkingwriter=csv.writer(csvfile,delimiter=";",quotechar='"')
    parkingwriter.writerow(columnas)
    parkingwriter.writerows( publicos )
    
