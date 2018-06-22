# Solution to Project Euler problem 95 by tdnzr.

# Related to problem 21 and problem 23, both of which deal with amicable numbers.
# And to 14, 74 and 92, all of which were about chains or sequences.

from euler_toolbox import proper_divisor_sum


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
            number = proper_divisor_sum(number)
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
