# Solution to Project Euler problem 35 by tdnzr.

# This problem is related to e.g. problems 7, 37, and 41.

from euler_toolbox import prime_sieve


def rotateNumber(n):
    """Given an integer n, this function returns a list of integers
    corresponding to all possible string rotations of n."""
    numString = str(n)
    rotatedList = []
    for _ in range(len(numString)):
        rotatedList.append(n)
        numString = numString[1:] + numString[:1]
        n = int(numString)
    return rotatedList


def run():
    limit = 1_000_000  # primes below 1000000
    sieve = prime_sieve(limit)

    # Loop through all primes. Rotate the primes,
    # then check if their rotations are also prime.
    count_circular = 0
    for primeCandidate in range(1, limit - 1):
        if not sieve[primeCandidate]:  # sieve[4] is True if 4 is *not* prime.
            candidateList = rotateNumber(primeCandidate)
            # If all the rotated candidates are prime, we've found a circular prime.
            for rotated_number in candidateList:
                if sieve[rotated_number]:
                    break
            else:  # Triggers if the for-loop wasn't stopped early.
                count_circular += 1
    return count_circular


if __name__ == "__main__":
    print(f"The number of circular primes below one million is: {run()}")
