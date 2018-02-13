#Problem 11; Find largest product in a grid.

with open("problem11.txt", "r") as inFile:
	lines = inFile.read().split("\n")
	del lines[-1]

grid = [[int(s) for s in line.split()] for line in lines]

maximum = i = j = x = y = 0
#hor = vert = rdiag = ldiag = 0
prod = 1
hor = vert = rdiag = ldiag = False

#Horizontal products
for i in range(len(grid)):
	for j in range(len(grid) - 3):
		for k in range(4):
			prod *= grid[i][j+k]
			if maximum < prod:
				maximum = prod
				x = j - k
				y = i
				hor = True
		prod = 1

#Vertical products
for i in range(len(grid) - 3):
	for j in range(len(grid)):
		for k in range(4):
			prod *= grid[i+k][j]
			if maximum < prod:
				maximum = prod
				x = i
				y = j
				vert = True
				hor = False
		prod = 1

#Diagonal crossing rightwards
for i in range(len(grid) - 3):
	for j in range(len(grid) - 3):
		for k in range(4):
			prod *= grid[i+k][j+k]
			if maximum < prod:
				maximum = prod
				x = i
				y = j
				rdiag = True
				vert = hor = False
		prod = 1

#Diagonal crossing leftwards
for i in range(len(grid) - 3):
	for j in range(3, len(grid)):
		for k in range(4):
			prod *= grid[i+k][j-k]
			if maximum < prod:
				maximum = prod
				x = i
				y = j
				ldiag = True
				rdiag = vert = hor = False
		prod = 1

direction = ["horizontally", "vertically", "diagonally rightwards", "diagonally leftwards"]

if hor:
	count = 0
elif vert:
	count = 1
elif rdiag:
	count = 2
elif ldiag:
	count = 3

print("Maximum product of the grid is: %d" % maximum)
print("Direction: %s" % direction[count])
print("Coordinates: (%d,%d)" % (x, y))
