#!/usr/bin/env python3

import urllib.request
import json

##trace the ISS
majortom='http://api.open-notify.org/astros.json'

groundctrl=urllib.request.urlopen(majortom) #this line should call the webservice

print(groundctrl.read())

