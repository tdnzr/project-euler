# Solution to Project Euler problem 48.

# Initial intuition: We have to calculate terms like 1000**1000 = 10**3000, which has 3000 digits. That seems impossible to calculate naively.
# Result: The solution came *instantaneously*. My intuition for how quick modern computers are is apparently *terrible*.
# However, the issue of a number having 3000 digits is a legitimate one, surely? If so, I'm honestly confused how the calculation even works under the hood.


def run():
    total_sum = sum([i**i for i in range(1, 1000+1)])  # Probably faster: pow(i, i, 10**10)
    return str(total_sum)[-10:]  # This yields the last 10 digits.


if __name__ == "__main__":
    print(run())
