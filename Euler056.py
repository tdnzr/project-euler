# Solution to Project Euler problem 56 by tdnzr.


def calcDigitSum(x):
    return sum([int(digit) for digit in str(x)])


def run():
    max_sum = 0
    for a in range(100):  # a < 100
        for b in range(100):  # b < 100
            digitSum = calcDigitSum(a**b)
            if digitSum > max_sum:
                max_sum = digitSum
    return max_sum


if __name__ == "__main__":
    print(run())
