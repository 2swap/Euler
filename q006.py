sq = 0
s = 0
for i in range(101):
	s += i
	sq += i * i
s *= s
print(s - sq)