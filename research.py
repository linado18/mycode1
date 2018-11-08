!#/usr/bin/env python3

import re # bring in the regex library

contact = "Contact: <sip:+5552224978@[2600:2304:9210:ec::2):5060;eri-generated-at=10.172.0.132>;+sip.instace+g.3gpp.isci"

contactobj = re.search(r'<sip:\+(\d+)@[(.*)\]:?(\d+)?", contact)

print("The phone number is: ")
print(contactobj.group(1))

print("The IPv6 address is:")
print(contactobj.group(2))

print("The port is:")
print(contactobj.group(3))

print("The entire matching string is:")
print(contactobj.group(0))

print("The begin character is:")
print(contactobj.start())

print("The end character is:")
print(contactobj.end(1))

print("The start and end character are...:")
print(contactobj.span())


