# Solution to Project Euler problem 46 by tdnzr.

# Note: A composite number is just a natural number that's neither 1 nor prime.
# In other words, numbers > 1 which are marked as True in the prime sieve.

from math import sqrt
from euler_toolbox import prime_sieve


def run():
    limit = 1_000_000  # arbitrary, but it yields the correct result
    sieve = prime_sieve(limit)

    # Loop through all odd composites, so begin with 9 (all smaller odd numbers are prime),
    # and use a step size of 2.
    for compositeCandidate in range(9, limit - 1, 2):
        if sieve[compositeCandidate]:  # sieve[4] is True if 4 is composite, i.e. not prime.
            # Once we've found an odd composite, we try to test the conjecure,
            # i.e. we try to write the composite as the sum of a prime and twice a square.

            # First, we loop through all valid squares for the "twice a square" part of the conjecture.
            # The upper limit comes from setting the prime to 0, so composite = 0 + 2*a**2
            # -> a = sqrt(composite/2) is the upper limit for a.
            for i in range(1, int(sqrt(compositeCandidate / 2)) + 1):
                doubleSquare = 2*(i**2)
                # Finally, we test if the composite minus the doubled square is still prime:
                # composite = potentialPrime + doubleSquare -> potentialPrime = composite - doubleSquare.
                if not sieve[compositeCandidate - doubleSquare]:
                    break
            # We're done once we've found an odd composite which doesn't fulfill the condition:
            else:
                return compositeCandidate


if __name__ == "__main__":
    print(f"The smallest odd composite that cannot be written as the sum of a prime and twice a square is {run()}.")
