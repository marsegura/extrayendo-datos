#!/usr/bin/env python3

import csv
import requests
import re

aparcamientos = requests.get('http://datos.madrid.es/egob/catalogo/202625-0-aparcamientos-publicos.csv').text

#with open("../data/202625-0-aparcamientos-publicos.csv","r") as aparcamientos:
parkingreader= csv.reader(aparcamientos.split("\n"),delimiter=';',quotechar='"')
#for row in parkingreader:
#    print(row)
no_vacios = list( filter( lambda p: p, parkingreader))
publicos = list( filter( lambda p: re.search(r"público",p[1]), no_vacios))
print(publicos)
