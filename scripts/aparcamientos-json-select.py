#!/usr/bin/env python3

import json
import requests
import csv
aparcamientos_json = requests.get('http://sl.ugr.es/parking_json').text

aparcamientos = json.loads(aparcamientos_json)['@graph']

aparcamientos_accesibles = list( filter(lambda p: p['organization']['accesibility'] == '1', aparcamientos))

aparcamientos_columnas = list(map( lambda p: [p['title'],p['location']['latitude'],p['location']['longitude']], aparcamientos_accesibles ))

with open("aparcamientos-limpio.csv", "w") as csvfile:
    parkingwriter=csv.writer(csvfile,delimiter=";",quotechar='"')
    parkingwriter.writerow(["nombre","latitude","longitude"])
    parkingwriter.writerows( aparcamientos_columnas )

