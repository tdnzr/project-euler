# Solution to Project Euler problem 1.
# Solution with list comprehension.


def run():
    sum = 0
    for i in [j for j in range(1000) if (j % 3 == 0) or (j % 5 == 0)]:
        sum += i
    return sum


if __name__ == "__main__":
    print(run())
