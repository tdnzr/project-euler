# Solution to Project Euler problem 30.

# What's the largest number I need to check? 9**5 = 59049, and 6 * (9**5) = 354294. I'll take that as my upper bound.


def run():
    power_sum = 0
    for testNum in range(2, 354294+1):  # 1 = 1**5 is specifically excluded by the problem description.
        current_sum = sum([int(n)**5 for n in str(testNum)])
        if current_sum == testNum:
            power_sum += testNum
            # print(f"{testNum} is equal to the sum of the fifth powers of its digits.")
    return power_sum


if __name__ == "__main__":
    print(f"The sum of all the numbers that can be written as the sum of fifth powers of their digits is: {run()}")
