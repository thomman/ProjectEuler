#Problem 25; 1000-digit Fibonacci number

count = 3
x1 = x2 = 1
x3 = x1 + x2
while len(str(x3)) < 1000:
	x1 = x2
	x2 = x3
	x3 = x1 + x2
	count += 1

print(count, x3)
