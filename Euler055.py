# Solution to Project Euler problem 55.

# This problem is related to problem 36, so I was able to borrow code from there.


def revertNum(n):
    """Returns the number n in reverse."""
    return int(str(n)[::-1])


def run():
    lychrel_count = 0
    for i in range(10000):  # Lychrel numbers below 10000.
        startNum = i
        # Test whether the number becomes a palindrome within
        # <50 iterations of the reverse-and-add process.
        # If that doesn't happen, it's a Lychrel number.
        for j in range(49):
            startNum += revertNum(startNum)
            if startNum == revertNum(startNum):
                break
        else:
            lychrel_count += 1
    return lychrel_count


if __name__ == "__main__":
    print(f"Below 10000, there are {run()} Lychrel numbers.")
