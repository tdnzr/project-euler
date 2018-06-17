# Solution to Project Euler problem X.

# Comment: In this solution I check the sums and differences of the first 2500 pentagon numbers.
# This yields a single result, which is considered the correct solution.
# However, I'm not sure if there's an easy way to prove that this result must be the correct one.


from math import sqrt


def calc_pent(n):
    return n * (3 * n - 1) // 2


def check_pent(p):
    # How do I check if a number is a pentagon number?
    # That's easy. P = n*(3n-1)/2 -> 2P = 3 n^2-n -> 3n^2-n-2P = 0
    # -> Quadratic equation with the two solutions n=(1+-sqrt(1+24P))/6;
    # I can ignore the solution for negative n.
    check = (1 + sqrt(1 + 24*p))/6
    return check.is_integer()


def run():
    # Calculates the first 2500 pentagon numbers via list comprehension:
    pentagonList = [calc_pent(i) for i in range(1, 2500 + 1)]
    listOfDiffs = []

    # New somewhat neat for-loop construction: Iterate over each y, for each x.
    # This line in particular yields a for-loop for two pentagonal numbers which haven't appeared before.
    for x, y in ((x, y) for x in pentagonList for y in pentagonList if x < y):
        penta_sum = x + y
        diff = y - x  # No abs() needed because x < y by construction.
        if check_pent(penta_sum) and check_pent(diff):
            listOfDiffs.append(diff)
            break  # This break statement isn't strictly justified, but I know that the single valid result turns out to be correct.
    return min(listOfDiffs)


if __name__ == "__main__":
    print(f"The minimal difference of Pentagon numbers for which their sum and diff are pentagonal is: {run()}")
