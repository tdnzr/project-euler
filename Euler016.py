# Solution to Project Euler problem 16.


def run():
    numberString = str(2**1000)
    return sum(int(s) for s in numberString)


if __name__ == "__main__":
    print(run())
