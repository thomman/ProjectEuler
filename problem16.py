#Problem 16; Power digit sum

#Alternative 1 using string
n = str(2**1000)
digitSum = sum(int(i) for i in n)

print("Alt 1: The digit sum of 2**1000 is %d" % digitSum)

#Alternative 2 working with int
n = 2**1000
digitSum = 0
while 1 < n:
	if n == 10:
		digitSum += 1
	digitSum += n % 10
	n //= 10

print("Alt 2: The digit sum of 2**1000 is %d" % digitSum)
