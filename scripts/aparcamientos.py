#!/usr/bin/env python

import urllib2
import csv

aparcamientos = urllib2.urlopen('http://datos.madrid.es/egob/catalogo/202625-0-aparcamientos-publicos.csv').read()

parkingreader= csv.reader(aparcamientos,delimiter=';')
