# Solution to Project Euler problem 12.

# 500 divisors -> What's the minimal number I even need to consider?
# It's certainly far, far smaller than the product of 1...500.

from math import trunc, sqrt


def calc_tri(n):
    """Returns the n-th triangle number."""
    return n * (n + 1) // 2


def divCount(n):
    """Returns the number of divisors of the integer n."""
    # Implementation: This function was *waaaaaay* too slow in its naive implementation.
    # Taking the square root made the difference between an impossibly slow function and a lightning-fast one.

    counter = 0
    root = trunc(sqrt(n))
    for i in range(1, root + 1):  # Tip from the web: Only check factors up to sqrt. If one factor is smaller than sqrt, then the other is larger.
        if n % i == 0:
            # Since I only check factors up to sqrt, I have to double-count each divisor.
            counter += 2

    # The following fixes an off-by-one error in case n is a square number.
    # E.g. 25 has the divisors 1, 5, 25, but the function would count 4 divisors (because it double-counts the 5).
    if root**2 == n:
        counter -= 1

    return counter


def run():
    for i in range(1_000_000):
        triangle_number = calc_tri(i)
        count = divCount(triangle_number)
        if count >= 500:
            return (i, triangle_number, count)


if __name__ == "__main__":
    index, triangle_number, count = run()
    print(f"Triangle number {index} has the value {triangle_number} and {count} divisors.")
