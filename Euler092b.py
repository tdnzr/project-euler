# Solution to Project Euler problem 92 by tdnzr.

# Adapted version of the original solution.
# 1) Now when a computed element of a chain is > i, we store that number,
# then once we know how this chain terminates, we store this information for all these chains, as well.
# 2) Pre-computed the results for 1 and 89, so I wouldn't have to 
# constantly check for these numbers in the for-loop.

# I expected this solution to be faster as a result, but it's just... not;
# it's pretty much as fast as the original.
# I haven't had time to investigate why. Maybe the overhead due to additional
# lists and comparisons etc. cancels out all potential time savings?


def squared_digit_sum(n):
    """Returns the sum of the squared digits of n."""
    return sum(int(digit)**2 for digit in str(n))


def run():
    # For each number, we store whether the resulting chain loops endlessly via 1 or via 89.
    # By seeding this list with one element, I can make it 1-based, i.e. the index of number 1 is suddenly 1,
    # and index and number are no longer off by one. I like that.
    chainList = [0] * 10_000_000
    # Slight improvement: We know the results for 1 and 89,
    # so we can pre-compute them here, and therefore remove them from the while-loop:
    chainList[1] = 1
    chainList[89] = 89

    for i in range(1, 10_000_000):  # Starting numbers *below* ten million.
        # Advance the loop if we've already computed the chain for this number:
        if chainList[i] != 0:
            continue
        next_in_sequence = squared_digit_sum(i)
        larger_elements = []
        while next_in_sequence > i and next_in_sequence != 89:  # Without that "!= 89" check, this is an infinite loop.
            larger_elements.append(next_in_sequence)
            next_in_sequence = squared_digit_sum(next_in_sequence)

        # Now next_in_sequence < i, by construction (we've already dealt with the remaining
        # case of i = 1 and 89 at the top). So I can just look up how the chain of i ended:
        known_value = chainList[next_in_sequence]
        chainList[i] = known_value
        for n in larger_elements:
            chainList[n] = known_value
    return chainList.count(89)


if __name__ == "__main__":
    from time import time
    start = time()
    print(f"Among starting numbers below ten million, {run()} eventually arrive at 89.")
    print(time()-start)
