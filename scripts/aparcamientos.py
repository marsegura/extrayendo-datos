#!/usr/bin/env python3

import csv
import requests

aparcamientos = requests.get('http://datos.madrid.es/egob/catalogo/202625-0-aparcamientos-publicos.csv').text
#with open("../data/202625-0-aparcamientos-publicos.csv","r") as aparcamientos:
parkingreader= csv.reader(aparcamientos,delimiter=';',quotechar='"',skipinitialspace=True)
for row in parkingreader:
    print(row)

