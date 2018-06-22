# Solution to Project Euler problem 41 by tdnzr.

# Approach: Generate pandigital numbers in reverse order,
# similar to what we did in problem 24 (lexicographic permutations),
# then stop once we've found one which is prime.

# Note: itertools returns items in lexicographic order. That's not alphabetical order!
# permutations of [1,0] yield the order (1, 0), (0, 1); [0,1] yields (0, 1), (1, 0).
# As I want to start with the numbers corresponding to the largest permutations,
# I've entered the numbers from largest to smallest in digitList.

from euler_toolbox import is_prime
from itertools import permutations


def run():
    # By using a list of strings here, later on we don't have to convert from int to str as often:
    digitList = ["9", "8", "7", "6", "5", "4", "3", "2", "1"]

    for _ in range(9):
        for pandigitalTuple in permutations(digitList):
            numberString = ''.join(pandigitalTuple)
            number = int(numberString)
            if is_prime(number):
                return number
        # If no 9-digit pandigital prime has been found,
        # remove the leftmost (largest) number from the list, then try again.
        digitList.pop(0)


if __name__ == "__main__":
    print(f"The largest n-digit pandigital prime that exists is: {run()}")
