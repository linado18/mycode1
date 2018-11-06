#!usr/bin/env python3

zfileobj=open('auth.log', 'r')

zfilelist=zfileobj.readlines()

zfileobj.close()


print("In auth.log there are ", len(zfilelist), "lines")

for x in zfilelist:
    if "terminating" in x.lower():
        print(x,rstrip("\n"))


