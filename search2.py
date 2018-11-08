#!/usr/bin/env python3

import re # bring in the regex library

contact = open('vzwpcap.txt', 'r')

contactobj = re.findall(r'<sip:\+(\d+)@[(.*)\]:?(\d+)?", contact.read())

for x in contactobj:
print(x)
print(x[0])
print(x[1])
print([2])

contact.close()


