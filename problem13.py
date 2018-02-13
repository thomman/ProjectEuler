#Problem 13; Large Sum

with open("problem13.txt", "r") as inFile:
	lines = inFile.read().split("\n")
	del lines[-1] #Empty string

theSum = str(sum([int(s) for s in lines])) #Sum of one-hundred 50-digit numbers as str
print(theSum[:10]) #First ten digits
