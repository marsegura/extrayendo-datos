#!/usr/bin/env python3

import json
import requests

aparcamientos_json = requests.get('http://sl.ugr.es/parking_json').text

aparcamientos = json.loads(aparcamientos_json)['@graph']

aparcamientos_accesibles = list( filter(lambda p: p['organization']['accesibility'] == '1', aparcamientos))

print(json.dumps(aparcamientos_accesibles))
