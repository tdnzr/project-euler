# Solution to Project Euler problem 15.
# Manual solution.

# Realisation: I can represent this 2d grid as a binary number.
# Paths in the 2x2 grid can be represented as a number with 2+2=4 digits,
# where 0 means "move vertically", 1 means "move horizontally",
# and any binary number which contains an equal number of 0s and 1s is a valid solution or path.

# -> In a 20x20 grid, I have a 20 + 20 = 40 digit long binary number.
# The answer I'm looking for is: How many 40-digit binary numbers are there that contain 20 ones and 20 zeroes?
# And the answer to that is simply the binomial coefficient (20 in 40).


from math import factorial


def calcBinomial(r, n):
    """Calculates the binomial coefficient [r in n]."""
    # We can use integer division here because binomial coefficients are natural numbers by construction.
    return (factorial(n) // (factorial(r) * factorial(n - r)))


def run():
    return calcBinomial(20, 40)


if __name__ == "__main__":
    print(run())
