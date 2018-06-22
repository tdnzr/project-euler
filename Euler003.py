# Solution to Project Euler problem 3 by tdnzr.

from math import trunc, sqrt


def findFactor(x):
    """Finds a factor of an integer."""
    root = trunc(sqrt(x))  # Integer square root of the number.
    for i in range(2, root+1):  # [2, ..., root]
        if x % i == 0:
            return i
    else:
        return x


def run():
    remainder = 600851475143
    listOfFactors = []

    while True:
        factor = findFactor(remainder)
        listOfFactors.append(factor)
        if factor == remainder:
            break
        remainder = remainder // factor

    return max(listOfFactors)


if __name__ == "__main__":
    print(f"Largest prime factor: {run()}")
