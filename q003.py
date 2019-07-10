num = 600851475143
a = 2
while True:
	if num % a == 0:
		print(a)
		num /= a
		a -= 1
	a += 1
	if num == 1:
		print("done")
		break