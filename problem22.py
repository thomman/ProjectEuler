#Problem 22; Names scores

fileName = "names.txt"

with open(fileName, "r") as inFile:
	lines = inFile.read() #One line

import re
p = re.compile(r'\w+') #Match any character
names = sorted(p.findall(lines))

def alphVal(char): #Returns alphanumeric value of a character
	return ord(char) - 64

nameScore = []
nameVal = 0

for i in range(len(names)):
	name = names[i]
	for j in name:
		nameVal += alphVal(j)
	nameScore.append((i+1)*nameVal)

total = sum(nameScore)

print("The total name score in %s is: %d" % (fileName, total))
