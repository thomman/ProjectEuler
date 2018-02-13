with open("problem8.txt", "r") as inFile:
	lines = "".join(inFile.read().split("\n")) #Make one cohesive string

prod = 1
maximum = 0

for i in range(len(lines) - 13): #Stop 13 units from the end.
	for j in range(i, i + 14):	#Multiply 13 numbers in sequence.
		prod *= int(lines[j])
	if prod > maximum:
		maximum = prod
	prod = 1

print(maximum)
