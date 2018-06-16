# Solution to Project Euler problem 2.
# Initial solution.

# Simplification: We only need to sum even terms in the Fibonacci sequence.
# Every third Fibonacci number is even, so I only need to consider those.


def run():
    x = 1
    y = 1
    z = 0  # Temporary variable
    counter = 2  # Starts at 2, because we already have 2 Fibonacci numbers
    sum = 0

    while x <= 4000000:  # Fibonacci numbers that do not *exceed* 4000000
        z = x
        x = x + y
        y = z
        counter += 1
        if counter % 3 == 0:  # Every third Fibonacci number is even
            sum += x

    return sum


if __name__ == "__main__":
    print(run())
