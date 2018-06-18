# Solution to Project Euler problem 50.

# This problem took me several tries before I found an algorithm fast enough to solve it.

# Algorithm for constructing numbers from the sums of consecutive primes:
# Store the consecutive summed-up primes in memory,
# sum them up until sum >= prime, then remove old primes until sum <= prime,
# then add new primes until sum >= prime again, etc.

# But with just the algorithm above, the solution still took >10 min on repl.it.

# But another dramatic speedrup resulted from replacing the for-loop with a while-loop,
# beginning with the largest prime in the sieve, rather than the smallest,
# and ending the while-loop once the current prime is smaller than the sum of the first X consecutive primes,
# where X is the highest number we've found so far of consecutive primes which sum up to a prime.

# For instance, the actual solution (997651) had 543 prime summands. By using the algorithm above and starting at 999999,
# there's no need to consider any primes smaller than the sum of the first 543 primes, i.e. 985878.

from euler_toolbox import prime_sieve
from collections import deque  # Using a deque instead of a list yields time-savings of a few seconds.


def run():
    # Generate the prime sieve, and create a list of all primes below the limit.
    limit = 1_000_000  # Primes below one million.
    sieve = prime_sieve(limit)
    primeList = [i for i in range(1, limit) if not sieve[i]]

    # Initialize some variables:
    lowerLimit = 0
    max_summands = 0
    prime_with_most_summands = 0

    # Loop through all primes in descending order.
    primeIndex = len(primeList) - 1  # Begin with the largest prime in the list. If a list has 5 elements, it has length 5, but its largest index is 4.
    prime = primeList[primeIndex]
    while prime > lowerLimit:
        prime_sum = 0
        summandList = deque()
        # Loop through all primes <= prime, then sum up consecutive primes
        # and check whether the sum equals prime.
        # Because we begin the sum with the smallest prime, once prime_sum == prime,
        # we've automatically found the sum with the most summands for this prime.
        for summandIndex in range(primeIndex):
            if prime_sum < prime:
                summand = primeList[summandIndex]
                prime_sum += summand
                summandList.append(summand)
            elif prime_sum == prime:
                # We've constructed the given prime as a sum of consecutive primes.
                # Now we count the number of summands sumCounter and test if it's a new maximum.
                # If it is, we increase the lower limit accordingly, so that it always corresponds to
                # the sum of the sumCounter lowest primes.
                sumCounter = len(summandList)
                if sumCounter > max_summands:
                    # Increase the lower limit by however many summands have been added due to the increase in max:
                    for i in range(max_summands, sumCounter):
                        lowerLimit += primeList[i]
                    max_summands = sumCounter
                    prime_with_most_summands = prime
            # Otherwise, prime_sum > prime, and we have to subtract summands from the left 
            # until prime_sum <= prime again.
            else:
                while prime_sum > prime:
                    prime_sum -= summandList.popleft()
        # Finally, we go to the next-largest prime.
        primeIndex -= 1
        prime = primeList[primeIndex]

    return prime_with_most_summands

if __name__ == "__main__":
    print(f"The current prime which can be written as the sum consisting of the most primes is {run()}.")
