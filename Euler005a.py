# Solution to Project Euler problem 5 by tdnzr.
# Obvious manual solution without programming.

# I just need to find the smallest list of prime factors from which one can calculate all numbers from 1 to 20,
# e.g. we already have 2, 3, 5, 7, 11, 13, 17, 19.
# So we need another factor 2 to obtain 4, and another factor 2 to obtain 8, and another factor 3 to obtain 9, and another factor 2 to obtain 16.
# Resulting solution: 2^4*3^2*5*7*11*13*17*19, which is correct.


def run():
    return 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19


if __name__ == "__main__":
    print(run())
