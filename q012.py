#FYI, this is an approximation, doesn't work for squares

import sys, math

i = 2
while i<50000:
    fac = 0
    a = 1
    tri = sum(range(i))
    while True:
        if tri % a == 0:
            fac += 2
        a += 1
        if fac>500:
            print(str(tri) + ": " + str(fac))
            sys.exit()
        if(a>math.sqrt(tri)):
            print(str(tri) + ": " + str(fac))
            break
    i+=1
