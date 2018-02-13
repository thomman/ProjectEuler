fib = [1,2]

while fib[-1] + fib[-2] < 4000000: #Generate all Fibonacci numb < 4 mill
	fib.append(fib[-1] + fib[-2])

fib = list(filter(lambda x: x % 2 == 0, fib)) #Filter out all odd numb


print("The sum of the even Fibonacci #'s < 4 million is: %d" % sum(fib))
