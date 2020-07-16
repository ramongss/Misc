def fibonacci(sequence_length):
    ''' Fibonacci function to calculate the fibonacci sequence of a given number.'''

    # sequence initials
    fib_init = [0, 1]

    for i in range(sequence_length):
        # summing the last 2 numbers
        fib_init.append(fib_init[-1] + fib_init[-2])
    return fib_init


if __name__ == "__main__":

    # length of the sequence
    sequence_len = 10
    fib_sequence = fibonacci(sequence_len)

    print(f"The Fibonacci Sequence of {sequence_len} numbers is: {fib_sequence}")
