# Solution to Project Euler problem 206.

# We're trying to find an integer whose square has the form 1_2_3_4_5_6_7_8_9_0.
# Preliminary thoughts: We're talking about a square of length 19, between 1*10^18 and 2*10^18.
# So we need only consider integers in the range 1*10^9 and 1.42*10^9.

# Also, for the square of a number to end in a zero, its final digit has to be a zero, as well.
# In which case the square will end on 00 by necessity. So we could take steps of size 10,
# i.e.: for i in range(1*10**9, 2*10**9, 10)

# But we can save even more computations by entirely ignoring this factor 100 in the square.
# So we'll instead consider integers in the range 1*10^8 to 1.42*10^8,
# and check that their square has the form 1_2_3_4_5_6_7_8_9.

# In fact, given that the last unknown digit, when squared, has to result in a 9,
# this means that it's either a 3 or a 7.
# So we can save even more time by only considering these cases.

# The original solution at the top took ~110.2s. After all these optimizations, I've ended up with ~6.8s.

import re


def run():
    regex = re.compile(r"1\d2\d3\d4\d5\d6\d7\d8\d9", re.VERBOSE)

    # The simple range function mentioned at the top has turned into this awkward construction:
    # The outer for-loop yields tuples of two numbers ending in 3 and 7 respectively.
    # The inner for-loop loops through these two numbers.
    for valid_values in zip(range(1*10**8 + 3, int(1.42*10**8), 10), range(1*10**8 + 7, int(1.42*10**8), 10)):
        for i in valid_values:
            # If the square of i matches the regular expression, we're done:
            if (regex.match(str(i**2))):
                return i * 10


if __name__ == "__main__":
    print(f"The correct number is: {run()}")
