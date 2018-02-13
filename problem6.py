def sumSquares(n): #1*1 + 2*2 + ... + n*n
	return (n*(n + 1)*(2*n + 1))/6

def squareSum(n): #(1 + 2 + ... + n)**2
	return ((n*(n+1)/2))**2

diff = squareSum(100) - sumSquares(100)

print(diff)
