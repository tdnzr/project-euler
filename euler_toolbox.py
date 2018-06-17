# A toolbox for functions shared between multiple solutions.


from math import sqrt  # for proper_divisor_sum


def fibonacci():
    """Calculates the fibonacci numbers, then returns them via generator."""
    a, b = 1, 1
    while 1:  # Always true. Not problematic due to how generators work.
        yield a
        # By simultaneously assigning multiple variables, I can skip the temporary variable "z" from the initial solution:
        a, b = b, a+b


def proper_divisor_sum(n):
    """Returns the sum of proper divisors of n, i.e. of divisors < n."""

    # Special case for zero. Perhaps never used.
    if n == 0:
        return 0

    # Special case for the divisor 1:
    div_sum = 1

    # Otherwise, test all numbers between 2 and the square root, rounded down to the nearest integer.
    # If there's a divisor <root, there's also a divisor >root.
    root = int(sqrt(n))
    for i in range(2, root + 1):
        if n % i == 0:
            div_sum += i + n // i  # Add both the divisor i and the divisor n // i.

    # Special case for squares. Otherwise, we get wrong results for e.g. 128*128=16384.
    if n == root ** 2:
        div_sum -= root

    return div_sum


# Stuff I could migrate to this toolbox:
# From Problem 12:
#  def calc_tri(n):
#    """Returns the n-th triangle number."""
# def divCount(n):
#    """Returns the number of divisors of the integer n."""
# From problem 15 & 53:
# def calcBinomial(r, n):
#    """Calculates the binomial coefficient [r in n]."""
# (though it's a one-liner)
# From problem 36:
# def dec_to_bin(x):
#     """Converts a decimal number to binary, then returns it as a string."""
# From problem 42 & problem 45:
# def check_tri(t):

# From problem 45:
# def calc_tri(n):
# def check_pent(p):
# def check_hex(h):
