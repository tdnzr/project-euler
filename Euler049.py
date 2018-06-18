# Solution to Project Euler problem 49.

# I suspect that this algorithm could possibly be improved
# by cycling through permutations first, and then testing whether
# they're an equal distance apart.
# But I'm not actually sure whether it would be faster, and in any case,
# the program is already essentially instantaneous in its current implementation.


from euler_toolbox import prime_sieve


def run():
    limit = 10_000  # We're interested in 4-digit primes, i.e. primes < 10000.
    sieve = prime_sieve(limit)

    # Loop through all 4-digit primes:
    for primeCandidate in range(1000, limit - 1):
        if sieve[primeCandidate]:
            continue

        # We're looking for three evenly spaced prime numbers below 10000.
        # So we can at most add ((limit - 1) - primeCandidate) / 2, twice.
        upperLimit = int(((limit - 1) - primeCandidate) / 2)
        for j in range(1, upperLimit):
            # Calculate the two candidates, then check whether they're prime:
            primeCandidate2 = primeCandidate + j
            primeCandidate3 = primeCandidate + (2*j)
            if sieve[primeCandidate2] or sieve[primeCandidate3]:
                continue

            # Now we know all three numbers are prime, we still have to test
            # whether they're also permutations of one another:
            else:
                sortedPrime = sorted(str(primeCandidate))
                if sortedPrime == sorted(str(primeCandidate2)) and sortedPrime == sorted(str(primeCandidate3)):
                    # Now we concatenate the three primes into the answer string,
                    # and make sure that it's not the answer already provided in the problem description.
                    answer_string = str(primeCandidate) + str(primeCandidate2) + str(primeCandidate3)
                    if answer_string != "148748178147":
                        return answer_string


if __name__ == "__main__":
    print(f"The three prime numbers with the desired property are concatenated into the following 12-digit number: {run()}")
