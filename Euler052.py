# Solution to Project Euler problem 52 by tdnzr.

# Optimization potential: We only care about numbers where 6x has the same number of digits as x,
# so e.g. the first two digits of x can only go from 1 to 16 because 17 * 6 = 102.
# If the algorithm wasn't already instantaneous, implementing this condition might help improve its speed.

# Or if that produces too much overhead in the calculation,
# I can at least check first that 6x has the same number of digits as x.


def sort_string(s):
    """Returns the string s, sorted alphabetically."""
    return ''.join(sorted(s))


def run():
    for i in range(1, 1_000_000):
        numStr = str(i)
        # Check that x and 6x have the same length:
        if len(numStr) == len(str(i * 6)):
            sortedStr = sort_string(numStr)
            # Go through the multiples in reverse order,
            # then check whether they contain the same digits
            # by testing whether their sorted strings are equal.
            for j in range(6, 1, -1):  # 6x ... 2x
                if sortedStr != sort_string(str(i * j)):
                    break
            # If we don't escape the for-loop early, that means we've found the solution.
            else:
                return i


if __name__ == "__main__":
    print(run())
