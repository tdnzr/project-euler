# Solution to Project Euler problem 7.


from euler_toolbox import prime_sieve


def run():
    limit = 150_000  # According to https://primes.utm.edu/howmany.html, there are ~10000 primes below ~100000.
    sieve = prime_sieve(limit)

    counter = 0
    for n in range(limit):
        if not sieve[n]:  # False = prime
            counter += 1
            if counter == 10001:
                return n


if __name__ == "__main__":
    print(f"The 10001st prime is: {run()}")
