def fact(n):
	if n == 0:
		return 1
	return n*fact(n-1)

#Alternative 1 using string
n = str(fact(100))
digitSum = sum(int(i) for i in n)

print("Alt 1: The digit sum of 100! is %d" % digitSum)

#Alternative 2 working with int

n = fact(100)
digitSum = 0
while 1 < n:
	if n == 10:
		digitSum += 10
	digitSum += n % 10
	n //= 10

print("Alt 2: The digit sum of 100! is %d" % digitSum)
