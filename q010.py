from math import sqrt

def isPrime(x):
    for i in range(2, int(sqrt(x)) + 1):
        if(x % i == 0):
            return False
    return True

ct = 0
i = 2
while i < 2000000:
    if isPrime(i):
        ct+=i
    i+=1
print(ct);
