c = 2 * 3 * 5 * 7 * 11 * 13 * 17
b = c
while True:
	right = True
	for a in range(1,21):
		if b % a != 0:
			right = False
			break
	if right:
		print(b)
		break
	b += c