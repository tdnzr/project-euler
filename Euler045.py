# Solution to Project Euler problem 45 by tdnzr.

# This problem is similar to problem 44, which also deals with pentagonal numbers.

# Note that there are less hexagonal numbers than pentagonal or triangle numbers,
# so if we computed hexagonal numbers and checked if they were triangular (rather than the other way around),
# the algorithm would be slightly faster still.

from math import sqrt


def calc_tri(n):
    return n * (n + 1) // 2


def check_tri(t):
    # Unused.
    # Inverse function of Tn = n(n + 1)/2
    check = (-1 + sqrt(1 + 8*t))/2
    return check.is_integer()


def check_pent(p):
    # Borrowed from problem 44. It's just the inverse function of the generating function Pn.
    check = (1 + sqrt(1 + 24*p))/6
    return check.is_integer()


def check_hex(h):
    # Inverse function of Hn = n * (2n - 1)
    check = (1 + sqrt(1 + 8*h))/4
    return check.is_integer()


def run():
    # No need to consider triangle numbers <= T285, given the problem.
    triangles = (calc_tri(i) for i in range(286, 100000))  # generator expression

    for triangle_number in triangles:
        if check_pent(triangle_number) and check_hex(triangle_number):
            return triangle_number


if __name__ == "__main__":
    print(f"{run()} is simultaneously a triangle, penagonal and hexagonal number.")
