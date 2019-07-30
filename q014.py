i = 2
maxi=maxl=0
while i<1000000:
    n = i
    l = 1
    while n != 1:
        if n%2==0:
            n/=2
        else:
            n=3*n+1
        l+=1
    if l>maxl:
        maxi=i
        maxl=l
    print(str(i)+": "+str(l))
    i+=1
print("Maximum chain starts with " + str(maxi) + " and has length " + str(maxl))
