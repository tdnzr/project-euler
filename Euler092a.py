# Solution to Project Euler problem 92 by tdnzr.

# This problem is related to problem 14, Longest Collatz sequence.
# I used a similar algorithm here:
# Compute the square digit chains beginning with 1, 2, 3, ...
# For each starting integer, store whether it loops at 1 or at 89.
# As before, once any element of the chain dips below the original integer,
# I'm done, since I can look up how that chain has ended.


def squared_digit_sum(n):
    """Returns the sum of the squared digits of n."""
    return sum(int(digit)**2 for digit in str(n))


def run():
    # For each number, we store whether the resulting chain loops endlessly via 1 or via 89.
    # By seeding this list with one element, I can make it 1-based, i.e. the index of number 1 is suddenly 1,
    # and index and number are no longer off by one. I like that.
    chainList = [0]
    for i in range(1, 10_000_000):  # Starting numbers below ten million.
        next_in_sequence = squared_digit_sum(i)
        while next_in_sequence > i and next_in_sequence != 89:  # Without that "!= 89" check, this is an infinite loop.
            next_in_sequence = squared_digit_sum(next_in_sequence)

        # The sequence terminates (or rather, loops) at either 1 or 89.
        # Incidentally, because sequences only loop at 1 or 89,
        # if i == next_in_sequence, this can only be true for i = 1 or 89.
        if next_in_sequence == 1 or next_in_sequence == 89:
            chainList.append(next_in_sequence)
        else:
            # Now next_in_sequence < i, by construction. So I can just look up how the chain of i ended:
            chainList.append(chainList[next_in_sequence])
    
    return chainList.count(89)


if __name__ == "__main__":
    print(f"Among starting numbers below ten million, {run()} eventually arrive at 89.")
