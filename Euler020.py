# Solution to Project Euler problem 20 by tdnzr.


def run():
    product = 1
    for i in range(1, 101):
        product *= i

    return sum([int(s) for s in str(product)])


if __name__ == "__main__":
    print(run())
