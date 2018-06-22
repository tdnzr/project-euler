# Solution to Project Euler problem 5 by tdnzr.
# Initial, highly inefficient solution. Works, but takes a few minutes.

# Algorithm: Find the smallest number that can be divided by 1 ... 20 without leaving any remainder.


def run():
    i = 0
    while True:
        i += 1
        for j in range(2, 21):  # No need to divide by 1.
            if i % j != 0:
                break  # Escape the for-loop (not the while loop).
        else:
            smallestDivisible = i
            break
    return smallestDivisible


if __name__ == "__main__":
    print(run())
