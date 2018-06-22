# Solution to Project Euler problem 37 by tdnzr.

# For this solution, I borrowed liberally from problem 27.


from euler_toolbox import prime_sieve


def run():
    limit = 800_000  # arbitrary, but it yields the correct result
    sieve = prime_sieve(limit)

    count_trunc = 0
    truncSum = 0
    
    for primeCandidate in range(11, limit - 1):  # The single-digit primes aren't considered truncatable.
        if not sieve[primeCandidate]:  # sieve[4] is True if 4 is *not* prime.
            truncLeft = str(primeCandidate)
            truncRight = str(primeCandidate)
            while True:
                # Truncate the primes. Then if the truncated numbers
                # aren't prime anymore, exit the loop.
                truncLeft = truncLeft[1:]  
                truncRight = truncRight[:-1]
                if sieve[int(truncLeft)] or sieve[int(truncRight)]:
                    break
                
                # Otherwise, check whether the numbers have been truncated to 1 digit,
                # in which case we've found a new truncatable prime.
                if len(truncLeft) == 1:
                    count_trunc += 1
                    truncSum += primeCandidate
                    break
        # According to the description, there are only 11 truncatable primes.
        # So we're done once we've found them all.
        if count_trunc >= 11:
            return truncSum


if __name__ == "__main__":
    print(f"The sum of the eleven truncatable primes is: {run()}")
