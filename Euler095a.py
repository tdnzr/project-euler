# Solution to Project Euler problem 95.

# Related to problem 21 and problem 23, both of which deal with amicable numbers.
# And to 14, 74 and 92, all of which were about chains or sequences.

from math import trunc, sqrt


def calcDivSum(n):
    """Returns the sum of proper divisors of n, i.e. of divisors < n."""
    # Special case for zero. Perhaps unnecessary - do we ever run this function for n = 0?
    if n == 0:
        return 0

    # Special case for the divisor 1:
    div_sum = 1

    # Otherwise, test all numbers between 2 and the square root.
    # If there's a divisor <root, there's also a divisor >root.
    root = trunc(sqrt(n))
    for i in range(2, root + 1):
        if n % i == 0:
            div_sum += i + n // i  # Add both the divisor i and the divisor n // i.

    # Special case for squares. Otherwise, we get wrong results for e.g. 128*128=16384.
    if n == root ** 2:
        div_sum -= root

    return div_sum


def run():
    amicableChains = []
    upperLimit = 1_000_000  # No element must exceed 1000000
    for i in range(1, upperLimit + 1):
        chain = []
        number = i
        # Construct the chains. Stop the chain once a member exceeds the limit,
        # or once the chain begins repeating itself.
        while True:
            chain.append(number)
            number = calcDivSum(number)
            if number > upperLimit or number in chain:
                break
		# If the last computed element is identical to the first one in the chain, we've found an amicable chain.
        if number == chain[0]:
            amicableChains.append(chain)

    amicableChainLengths = [len(chain) for chain in amicableChains]
    IndexOfLongestChain = amicableChainLengths.index(max(amicableChainLengths))

    return min(amicableChains[IndexOfLongestChain])


if __name__ == "__main__":
    print(f"The smallest number of the longest amicable chain with no element exceeding one million is: {run()}")
