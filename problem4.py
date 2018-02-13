#Finds the largest palindrome number made up by 3-digit numbers

s = ""
palindromes = []

x = y = 0

for i in range(900, 999): #No need to start at 100.
	for j in range(900, 999):
		s = str(i*j)
		for k in range(int(len(s)/2)):
			if not s[k] == s[-k-1]: #Compare index 0,1,2.. against -1,-2,-3...
				break
			elif k == int(len(s)/2) - 1: #Palindrome found
				x = i
				y = j
				palindromes.append(s)

print("The largest palindrom product is %s = %d * %d." % (palindromes[-1], x, y))
