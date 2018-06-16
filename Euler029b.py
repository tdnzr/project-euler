# Solution to Project Euler problem 29.
# Solution via set plus for-loop.


def run():
    power_set = set()
    for a in range(2, 100+1):
        for b in range(2, 100+1):
            power_set.add(a ** b)
    return len(power_set)


if __name__ == "__main__":
    print(run())
