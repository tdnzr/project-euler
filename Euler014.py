# Solution to Project Euler problem 14 by tdnzr.

# My initial solution didn't make use of Collatz sequences we'd already calculated.
# As a result, it was extraordinarily inefficient.

# The following solution makes use of two tricks:
# 1) I can stop calculating further elements in a Collatz sequence once I reach
# an element which has appeared in a previous sequence already.
# 2) Rather than saving all the Collatz sequences,
# it's enough if I save just the length of the sequence.

# Further efficiency gains would be possible: Currently, I don't save sequences > i,
# even though by e.g. computing the sequence for 3, I already have to compute the
# sequences for 4, 5, 8, 10, and 16.


def next_collatz(n):
	"""Returns the next element in the Collatz sequence following after n."""
	if n % 2 == 0:
		return n // 2
	else:
		return n * 3 + 1


def run():
    # List of 1 million elements. We gradually replace the contents of this list
    # with the length of the corresponding Collatz sequences.
    # By beginning the list at zero, we can make it 1-based,
    # which slightly helps with some later calculations.
    collatz_lengths = [0 for _ in range(1_000_000)]

    # Hack: The algorithm below only works for i >= 5, so I hard-code the results for i = 1...4 here.
    collatz_lengths[1] = 3
    collatz_lengths[2] = 3
    collatz_lengths[3] = 8
    collatz_lengths[4] = 3

    # Loop through the natural numbers and compute the corresponding Collatz sequence.
    # Stop once an element in the sequence dips below i itself - because I already
    # know the Collatz lengths below i.
    for i in range(5, 1_000_000):
        sequence_length = 0
        num = i
        while num >= i:
            sequence_length += 1
            num = next_collatz(num)
        sequence_length += collatz_lengths[num]  # 1-based: the length of the sequence beginning with 1 is at index 1 of the list, etc.
        collatz_lengths[i] = sequence_length

    return collatz_lengths.index(max(collatz_lengths))

if __name__ == "__main__":
    print(f"Among starting numbers under one million, {run()} produces the longest Collatz chain.")
