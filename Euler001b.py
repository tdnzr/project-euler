# Solution to Project Euler problem 1 by tdnzr.
# Solution with list comprehension.


def run():
    total_sum = 0
    for i in [j for j in range(1000) if (j % 3 == 0) or (j % 5 == 0)]:
        total_sum += i
    return total_sum


if __name__ == "__main__":
    print(run())
