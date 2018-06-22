# Solution to Project Euler problem 27 by tdnzr.


from euler_toolbox import prime_sieve


def run():
    sieve = prime_sieve(150_000)

    maxPrimeCounter = 0
    max_product = 0
    # Loop through the coefficients a and b,
    # with |a| < 1000, |b| <= 1000.
    for a in range(-1000 + 1, 1000):
        for b in range(-1000, 1000 + 1):
            primeCounter = 0
            # Count how many consecutive primes we can construct:
            for n in range(10_000):  # arbitrary limit, but irrelevant as we always break the loop early
                primeCandidate = n**2 + a * n + b
                if not sieve[primeCandidate]:  # sieve[4] is True if 4 is *not* prime.
                    primeCounter += 1
                else:
                    break
            if primeCounter > maxPrimeCounter:
                maxPrimeCounter = primeCounter
                max_product = a*b
    return max_product


if __name__ == "__main__":
    print(f"The product of the coefficients a and b which produces the maximum number of primes for consecutive values of n is: {run()}")
