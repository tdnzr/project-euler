# Solution to Project Euler problem 29 by tdnzr.
# Solution via list plus for-loop.


def run():
    power_list = []
    for a in range(2, 100+1):
        for b in range(2, 100+1):
            n = a ** b
            if n not in power_list:
                power_list.append(n)
    return len(power_list)


if __name__ == "__main__":
    print(run())
