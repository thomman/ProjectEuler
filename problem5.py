#numb = 2520

#for i in range(1,11):
#	print("%d: %r" % (i,numb % i == 0))

numb = 3000
count = 0

while True:
	for i in range(20, 0, -1):
		if numb % i != 0:
			break
		else:
			count += 1
	if count == 20:
		break
	count = 0
	numb += 20

print("The number is divisible by:")
for i in range(1, 21):
	print("%d: %r" % (i, numb % i == 0))
print("And the number is: %d" % numb)
