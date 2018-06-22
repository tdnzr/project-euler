# Solution to Project Euler problem 97 by tdnzr.

# Naturally, we can't efficiently calculate a number with >2 million digits directly.
# i.e. return str(28433 * 2**7830457 + 1)[-10:]

# But given that we're only interested in the last ten digits,
# and that we're just multiplying numbers, I can just truncate everything in front of the last ten digits,
# without it affecting the result.

# Also, I can significantly simplify the base-exponent pair as follows:
# 2**X = 2**(A*B) = (2**A)**B. For instance, 2**9 = (2**3)**3 = 8**3.
# The exponent 7830457 is prime by construction, but we can still simplify the calculation:
# 7830457 = 783*10000 + 457
# -> 2**7830457 = (2**10000)**783 * (2**457)


def run():
    truncNum = int(str(2**10000)[-10:])
    product = (truncNum**783) * (2**457)
    result_string = str(28433 * product + 1)
    return result_string[-10:]


if __name__ == "__main__":
    print(run())
