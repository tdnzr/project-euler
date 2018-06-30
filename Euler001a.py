# Solution to Project Euler problem 1 by tdnzr.
# Initial solution.


def run():
    numbers = range(1000)
    total_sum = 0
    for i in numbers:
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum


if __name__ == "__main__":
    print(run())
