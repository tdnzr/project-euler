# Solution to Project Euler problem 24 by tdnzr.

# This is a problem based on lexicographical permutations. In Python, there's a built-in library for this.
# itertools.permutations(iterable) doesn't just return the permutations, it even returns them in lexicographic order.

from itertools import permutations, islice


def run():
    # Permutations returns a generator, so we'd normally have to loop through it.
    # But to obtain the nth permutation, there's a more concise way via itertools.islice:
    # (The iterator is zero-based, hence the -1.)
    digitTuple = next(islice(permutations("0123456789"), 1_000_000 - 1, None))
    return "".join(digitTuple)


if __name__ == "__main__":
    print(f"The millionth lexicographic permutation of the digits 0...9 is: {run()}")
