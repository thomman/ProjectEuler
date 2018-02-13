numb = 600851475143

fact = []
i = 2

while numb > 1:
	if numb % i == 0:
		while numb % i == 0:
			numb /= i
		fact.append(i) #These will be prime factors.
	else:
		i += 1

print("The highest prime factor of %d is %d" % (600851475143, fact[-1]))
