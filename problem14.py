#Problem 14; Longest Collatz sequence

def f(n):
	return n//2 if n % 2 == 0 else 3*n + 1

i = 2
chain = numb = 0

while i < 1000000:
	steps = 1
	n = i
	while 1 < n:
		n = f(n)
		steps += 1
	if chain < steps:
		chain = steps
		numb = i
	i += 1

print("%d is the number that produces the largest chain of %d \
iterations while being under a million." % (numb, chain))
