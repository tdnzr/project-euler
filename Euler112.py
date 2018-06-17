# Solution to Project Euler problem 112.


from fractions import Fraction


def is_bouncy(num):
    """Returns True if the given number is neither ascending nor descending, False otherwise."""
    numberString = str(num)
    asc, desc = True, True
    for a, b in zip(numberString[:-1], numberString[1:]):
        if a == b:
            continue
        if desc and a < b:  # The "desc and" part of the if-clause ensures that, if the number isn't descending, the second part is not evaluated. Saves a bit of time.
            desc = False
        if asc and a > b:
            asc = False
        if not (asc or desc):
            break
    else:
        return False

    return True


def run():
    # There are no bouncy numbers below 100.
    n_total = 100
    n_bouncy = 0

    while Fraction(n_bouncy, n_total) - 0.99 != 0:
        if is_bouncy(n_total):
            n_bouncy += 1
        n_total += 1

    return n_total


if __name__ == "__main__":
    print(f"Among the first {run()} numbers, exactly 99% are bouncy.")
