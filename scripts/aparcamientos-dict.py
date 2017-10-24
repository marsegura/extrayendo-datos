#!/usr/bin/env python3

import csv
import requests
import re

aparcamientos = requests.get('http://datos.madrid.es/egob/catalogo/202625-0-aparcamientos-publicos.csv').text.split("\n")
no_vacios = list( filter( lambda p: len(p)>2, aparcamientos))
columnas = no_vacios[0].split(";")
parkingreader= csv.DictReader(no_vacios,fieldnames=columnas,delimiter=';',quotechar='"')
aparcamientos_accesibles = list( filter(lambda p: p['ACCESIBILIDAD'] == '1', parkingreader))

print(aparcamientos_diccionario)    
