# Solution to Project Euler problem 119.

# My original algorithm looped through the natural numbers,
# computed their digit sum, and then looped through exponents
# until digit sum ** exponent >= number.
# This was impossibly inefficient, even after using the logarithm
# to speed up some calculations.

# The following, more efficient solution takes an entirely opposite approach:
# Loop through base-exponent pairs, then test if the digit sum of the
# result is equal to the base.

# Note that while this solution is fast, the ranges for base and exponent
# were set arbitrarily. If either range is too small, the algorithm would miss some
# valid results.


def calcDigitSum(x):
    return sum([int(digit) for digit in str(x)])


def run():
    listOfPowers = []
    for base in range(1, 500 + 1):
        for exponent in range(1, 50):
            result = base ** exponent
            if result >= 10 and calcDigitSum(result) == base:
                listOfPowers.append(result)
    listOfPowers.sort()
    return listOfPowers[30 - 1]


if __name__ == "__main__":
    print(run())
