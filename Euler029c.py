# Solution to Project Euler problem 29.
# Solution via set comprehension.


def run():
    power_set = set(a ** b for b in range(2, 100+1) for a in range(2, 100+1))
    return len(power_set)


if __name__ == "__main__":
    print(run())
