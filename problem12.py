#Problem 12; Higly divisible triangular number.

divisors = i = 0
count = 7 #Number 28

while divisors < 501:
	count += 1
	divisors = 0
	triangular = sum(i for i in range(1, count + 1))
	divisors += 2 #Since all numbers are divisible by 1 and themselves.
	for j in range(2, triangular//2 + 1):
		if triangular % j == 0:
			divisors += 1

print("The first triangular number that have over 500 divisors is: %d\n\
It has: %d divisors." % (triangular, divisors))
