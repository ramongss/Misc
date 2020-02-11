def fibonacci(x):
	
	'''
	Fibonacci function to calculate the fibonacci sequence 
	of a given number. 
	'''

	fib_init = [0,1]    # sequence initials

	for i in range(x):
		fib_init.append(fib_init[-1] + fib_init[-2])	# summing the last 2 numbers
	
	return fib_init


if __name__ == "__main__":

	x = 10    # length of the sequence

	fib_sequence = fibonacci(x)

	print(f"The Fibonacci Sequence of {x} numbers is:")
	print(fib_sequence)