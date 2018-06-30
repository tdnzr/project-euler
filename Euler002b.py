# Solution to Project Euler problem 2 by tdnzr.
# Alternative solution, with generator.

# Simplification: We only need to sum even terms in the Fibonacci sequence.
# Every third Fibonacci number is even, so I only need to consider those.

from euler_toolbox import fibonacci


def run():
    total_sum = 0

    for n in fibonacci():
        if n > 4000000:
            break
        if n % 2 == 0:  # Only add even Fibonacci numbers.
            total_sum += n

    return total_sum


if __name__ == "__main__":
    print(f"The total sum of the even-valued Fibonacci numbers below four million is: {run()}")
