# Solution to Project Euler problem 1.
# Unreadable solution with list comprehension.


def run():
    return sum([j for j in range(1000) if (j % 3 == 0) or (j % 5 == 0)])


if __name__ == "__main__":
    print(run())
