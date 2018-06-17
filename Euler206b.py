# Solution to Project Euler problem 206.

# Based on Euler206a.py, I've replaced the regular expression via a string test.
# It's slightly faster (by roughly a second), but I find it ugly and less readable.


def run():
    # The simple range function mentioned at the top has turned into this awkward construction:
    # The outer for-loop yields tuples of two numbers ending in 3 and 7 respectively.
    # The inner for-loop loops through these two numbers.
    for valid_values in zip(range(1*10**8 + 3, int(1.42*10**8), 10), range(1*10**8 + 7, int(1.42*10**8), 10)):
        for i in valid_values:
            # If the square of i matches the condition, we're done:
            sq = str(i**2)
            if (sq[0] == "1" and sq[2] == "2" and sq[4] == "3"
               and sq[6] == "4" and sq[8] == "5" and sq[10] == "6"
               and sq[12] == "7" and sq[14] == "8" and sq[16] == "9"):
                return i * 10


if __name__ == "__main__":
    print(f"The correct number is: {run()}")
