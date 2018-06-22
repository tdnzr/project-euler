# Solution to Project Euler problem 10 by tdnzr.


from euler_toolbox import prime_sieve


def run():
    limit = 2_000_000  # Numbers *below* 2,000,000.
    sieve = prime_sieve(limit)
    prime_sum = sum(n for n in range(limit) if not sieve[n])
    return prime_sum


if __name__ == "__main__":
    print(f"The sum of all the primes below 2000000 is {run()}")
