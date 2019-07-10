from math import sqrt

def isPrime(x):
	for i in range(2, int(sqrt(x)) + 1):
		if(x % i == 0):
			return False
	return True

ct = 0
i = 2
while True:
	if isPrime(i):
		ct+=1
		if ct == 10001:
			print("10001th found! " + str(i))
			break
		print(i)
	i+=1