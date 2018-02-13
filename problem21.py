#Problem 21; Amicable numbers

amicable = []

a = 2
i = 1

def d(n): #Returns the sum of divisors of a number
	i = 1
	divisors = []
	while i <= n //2:
		if n % i == 0:
			divisors.append(i)
		i += 1
	return sum(divisors)

while a < 10000:
	b = d(a)
	if a != b and a == d(b):
		if not a in amicable and not b in amicable:
			amicable.append(a)
			amicable.append(b)
	a += 1

print(amicable)
