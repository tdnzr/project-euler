# Solution to Project Euler problem 80.

# Note: I only discovered this via trial and error,
# but by "first one hundred decimal digits",
# the problem means digits *including the ones to the left of the comma*.


# This problem requires high precision, so import the Decimal module
from decimal import Decimal, getcontext


def hundred_digit_sum(x):
    """Removes the period from the number, then computes the digital sum of the first 100 digits."""
    testString = str(x).replace(".", "")[:100]  # Remove the period, then all digits after the hundredth.
    return sum([int(i) for i in testString])


def run():
    # Adjust the precision of the Decimal class:
    # For a precision of 5, Decimal rounds to numbers like 12.345 or 1.2345.
    # I need to take the irrational roots of 1...99, resulting in numbers beginning with 1...9,
    # i.e. one digit left of the comma, plus (given the required precision) 100 digits to the right.
    # Plus one more digit, because Decimal rounds to this precision.
    # (For example, with a precision of 1, Decimal(4) / Decimal(3) = 1.)
    # So we need a precision of at least 102.
    getcontext().prec = 102

    total_sum = 0
    squares = set(number**2 for number in range(1, 10 + 1))
    for number in range(1, 100 + 1):  # "For the first one hundred natural numbers"
        # Skip numbers which have rational square roots, e.g. 25 = 5*5:
        if number not in squares:
            # Calculate the root via the Decimal class. Note that e.g. Decimal(math.sqrt(3)) would not work,
            # because math.sqrt(3) is not as accurate. Similarly, Decimal(1 / 3.0) = 0.333333333333333314829...,
            # even if a sufficiently large precision has been set, because 3.0 only has the low precision of a float.
            root = Decimal(number) ** Decimal(0.5)
            total_sum += hundred_digit_sum(root)
    return total_sum


if __name__ == "__main__":
    print(run())
