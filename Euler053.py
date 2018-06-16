# Solution to Project Euler problem 53.

# Definition of the binomial coefficient: [a in b] = (a in b) = b! / (a! * (b - a)!), 0 <= a <= b

from math import factorial


def calcBinomial(r, n):
    """Calculates the binomial coefficient [r in n]."""
    # We can use integer division here because binomial coefficients are natural numbers by construction.
    return (factorial(n) // (factorial(r) * factorial(n - r)))


def run():
    counter = 0
    for n in range(1, 100+1):
        for r in range(n+1):  # 0 <= r <= n
            if calcBinomial(r, n) > 1_000_000:
                counter += 1
    return counter


if __name__ == "__main__":
    print(run())
