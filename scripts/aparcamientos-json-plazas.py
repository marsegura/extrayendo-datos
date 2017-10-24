#!/usr/bin/env python3

import json
import requests
import csv
import re

def mis_columnas( fila ):
    cifras = re.match( r"(\d+)", fila['organization']['organization-desc'])
    return [fila['title'],fila['address']['postal-code'],
            fila['organization']['accesibility'],
            fila['location']['latitude'],fila['location']['longitude'],
            cifras[0], cifras[1]]

aparcamientos_json = requests.get('http://sl.ugr.es/parking_json').text

aparcamientos = json.loads(aparcamientos_json)['@graph']

aparcamientos_columnas = list(map( mis_columnas, aparcamientos ))

with open("aparcamientos-limpio-plazas.csv", "w") as csvfile:
    parkingwriter=csv.writer(csvfile,delimiter=";",quotechar='"')
    parkingwriter.writerow(["nombre","latitude","longitude"])
    parkingwriter.writerows( aparcamientos_columnas )

