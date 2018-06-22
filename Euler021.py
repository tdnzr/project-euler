# Solution to Project Euler problem 21 by tdnzr.

from euler_toolbox import proper_divisor_sum


def run():
    amicable_sum = 0
    for numOne in range(10000):  # Amicable numbers under 10000.
        numTwo = proper_divisor_sum(numOne)
        # To avoid double-counting, we require numOne <= numTwo.
        # And numOne == numTwo is explicitly ruled out in the exercise.
        if numOne < numTwo and numOne == proper_divisor_sum(numTwo):
            amicable_sum += numOne + numTwo
    return amicable_sum


if __name__ == "__main__":
    print(run())
