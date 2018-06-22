# Solution to Project Euler problem 51 by tdnzr.

# To generate primes, I borrowed the prime sieve from some earlier problems.
# To replace part of the number, I borrowed the function itertools.combinations from problem 98.

from itertools import combinations
from euler_toolbox import prime_sieve


def run():
    # Generate the prime sieve, and create a generator for all primes below the limit.
    limit = 1_000_000  # arbitrary, but it yields the correct result
    sieve = prime_sieve(limit)
    primes = (i for i in range(1, limit) if not sieve[i])

    for prime in primes:
        prime_length = len(str(prime))
        # Loop through all possibilities of how many digits to replace - at most all but one.
        # Then use itertools.combinations to yield all combinations of which *digit positions* to replace.
        # The construction below yields all the combinations of the integers 0 ... len(prime)
        # of length amount_to_replace, in sorted order, i.e. there could be a "0129",
        # but then there'd be no "9012". Which is exactly what I want.
        for amount_to_replace in range(1, prime_length):
            for digitsToReplace in combinations(range(prime_length), amount_to_replace):
                primeFamily = []
                newNumberList = [digit for digit in str(prime)]
                for newDigit in range(10): # Replace the chosen digits with the numbers 0...9.
                    for index in digitsToReplace:
                        newNumberList[index] = str(newDigit)
                    newNumber = int("".join(newNumberList))
                    # If newNumber begins with a zero, disregard it:
                    if len(str(newNumber)) < prime_length:
                        continue
                    # If newNumber is prime, add it to the primeFamily.
                    if not sieve[newNumber]:
                        primeFamily.append(newNumber)
                # If we've found a primeFamily of length 8, we're done:
                if len(primeFamily) == 8:
                    return min(primeFamily)


if __name__ == "__main__":
    print(f"{run()} is the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.")
