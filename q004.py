def isPalindromic(a):
	return str(a) == str(a)[::-1]

largest=-1

for i in range(999,99,-1):
	for j in range(999,99,-1):
		if(isPalindromic(i*j)):
			print(i*j)
			largest = max(largest, i*j)

print("Largest is: {}".format(largest))