# A toolbox for functions shared between multiple solutions.

def fibonacci():
    """Calculates the fibonacci numbers, then returns them via generator."""
    a, b = 1, 1
    while 1:  # Always true. Not problematic due to how generators work.
        yield a
        # By simultaneously assigning multiple variables, I can skip the temporary variable "z" from the initial solution:
        a, b = b, a+b

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

# From problem 95a and 95b:
# def calcDivSum(n):
#     """Returns the sum of proper divisors of n, i.e. of divisors < n."""