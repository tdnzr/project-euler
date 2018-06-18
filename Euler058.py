# Solution to Project Euler problem 58.

# This problem is related to problem 28.
# Instead of going through the pain of generating the spiral again,
# here I use the insight that beginning with the center (spiral side length 1),
# the corner numbers in the next spiral (side length 3) can be reached by adding +2 each time:
# 1 + 2 = 3 + 2 = 5 + 2 = 7 + 2 = 9,
# then by adding +4 each time, then +6 each time, etc.

from euler_toolbox import is_prime


def run():
    # Initialize values: We begin at the center,
    # so corner_num = 1; 1 is not a prime, so primes = 0;
    # we've seen one corner so far, so corners = 1;
    # and the current spiral has a side_length of 1.
    corner_num = 1
    primes = 0
    corners = 1
    side_length = 1

    # Calculate the numbers on the diagonals, check if they're prime,
    # and compute the ratio of primes:
    for offset in range(2, 1_000_000 + 1, 2):  # Offset starts at 2, then goes to 4, 6, 8, ...
        for _ in range(4):
            corner_num += offset
            corners += 1
            if is_prime(corner_num):
                primes += 1

        # After a full loop, our spiral has grown by 1 in all directions,
        # so it has grown by 2 in height and width.
        side_length += 2

        # Finally, we test if the ratio of primes on the diagonals has dropped below 0.1.
        primeRatio = primes / corners
        if primeRatio < 0.1:
            return side_length


if __name__ == "__main__":
    print(f"For the spiral with side length {run()}, the prime ratio first falls below 0.1.")
