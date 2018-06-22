# Solution to Project Euler problem 23 by tdnzr.

# This problem is related to problem 21.

# I originally tried to find the non-abundant numbers by looping through all numbers up to 28123,
# then testing if I could construct them from two numbers in abundantList.
# This was glacially slow - the program wasn't done even after 3 minutes.

# So instead, I now take the opposite approach: Find all numbers <= 28123 which can be written as
# the sum of two abundant numbers, then seeing what's missing. This solution is almost instantaneous.

from euler_toolbox import proper_divisor_sum


def run():
    # Construct a list of abundant numbers, i.e. numbers n with proper_divisor_sum(n) > n.
    # Range: We later on need to build sums of two abundant numbers <= 28123.
    # The smallest abundant number is 12, so the largest relevant number is 28123 - 12 = 28111.
    abundantList = [i for i in range(12, 28111 + 1) if i < proper_divisor_sum(i)]

    # Find all numbers <= 28123 which can be written as the sum of two abundant numbers.
    abundant_sums = set()
    for i in abundantList:
        for j in abundantList:
            abundant_sum = i + j
            if abundant_sum <= 28123:
                abundant_sums.add(abundant_sum)

    # Then subtract their sum from the total sum of 1...28123, which is n*(n+1)/2:
    total_sum = 28123 * 28124 // 2
    return total_sum - sum(abundant_sums)


if __name__ == "__main__":
    print(run())
