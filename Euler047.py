# Solution to Project Euler problem 47.

from math import sqrt
from euler_toolbox import prime_sieve, count_unique_prime_factors


def run():
    limit = 1_000_000  # Check primes below 1000000
    sieve = prime_sieve(limit)

    # Loop through the composite numbers:
    for compositeCandidate in range(4, limit - 1):
        # Check whether the current number and the next three consecutive numbers in the sieve
        # are all composite. If they aren't, skip to the next compositeCandidate.
        for i in range(3 + 1):
            if not sieve[compositeCandidate + i]:
                break
        # Now that we've found four consecutive composite numbers,
        # we count their distinct prime factors.
        else:
            for j in range(3 + 1):
                if count_unique_prime_factors(compositeCandidate + j, sieve) < 4:
                    break
            # Once we've found four consecutive composites with
            # at least 4 distinct prime factors each, we're done.
            else:
                return compositeCandidate


if __name__ == "__main__":
    print(f"The first of the four consecutive integers to have four distinct prime factors is: {run()}")
