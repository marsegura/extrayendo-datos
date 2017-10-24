#!/usr/bin/env python3

import csv
import requests
import re

aparcamientos = requests.get('http://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=json&file=0&filename=202625-0-aparcamientos-publicos&mgmtid=26e6cc885fcd3410VgnVCM1000000b205a0aRCRD&preview=full').text
no_vacios = list( filter( lambda p: len(p)>2, aparcamientos))
columnas = no_vacios[0].split(";")
parkingreader= csv.DictReader(no_vacios,fieldnames=columnas,delimiter=';',quotechar='"')
aparcamientos_accesibles = list( filter(lambda p: p['ACCESIBILIDAD'] == '1', parkingreader))

print(aparcamientos_diccionario)    
