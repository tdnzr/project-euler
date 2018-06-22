# Solution to Project Euler problem 95 by tdnzr.

# Related to problem 21 and problem 23, both of which deal with amicable numbers.
# And to 14, 74 and 92, all of which were about chains or sequences.


# The following method was supposed to be faster, but didn't actually turn out to be that much faster.
# The idea: Once proper_divisor_sum(number) < number, we've already computed that chain.
# I used the same logic in problems 14, 74 and 92.


from euler_toolbox import proper_divisor_sum


def run():
    ChainsList = []
    upperLimit = 1_000_000  # No element must exceed 1000000
    for i in range(upperLimit):
        chain = []
        number = i
        # Construct the chains. Stop once number < i,
        # in which case we've already computed the chain.
        # Or once a member exceeds the limit,
        # or once the chain begins repeating itself.
        # In any case, this time we append the repeating element to the chains.
        while True:
            chain.append(number)
            number = proper_divisor_sum(number)
            if number < i:
                chain += ChainsList[number]  # 1-based index. The chain beginning with the number 1 has the index 1.
                break
            elif number > upperLimit or number in chain:
                chain.append(number)  # We have to append this element so we can later check if it's identical to the first one.
                break
        ChainsList.append(chain)

    amicableChains = [chain for chain in ChainsList if chain[0] == chain[-1]]
    amicableChainLengths = [len(chain) for chain in amicableChains]
    IndexOfLongestChain = amicableChainLengths.index(max(amicableChainLengths))

    return min(amicableChains[IndexOfLongestChain])


if __name__ == "__main__":
    print(f"The smallest number of the longest amicable chain with no element exceeding one million is: {run()}")
