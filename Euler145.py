# Solution to Project Euler problem 145.

# The following solution works, but it's glacially slow.
# It got the correct result after ~1250s on my machine.


def all_digits_odd(n):
    """Returns True if n contains only odd digits, False otherwise."""
    # Because we have to turn n into a string to loop over it,
    # this test for oddness is much faster than converting each
    # digit-string back into an integer and taking it modulo 2.
    for digit in str(n):
        if digit in {"0", "2", "4", "6", "8"}:
            return False
    else:
        return True


def run():
    count_reversible = 0
    for i in range(1_000_000_000):  # numbers below one billion
        # Skip numbers which end in a zero - their reverse
        # would have a leading zero, which isn't allowed.
        if i % 10 == 0:
            continue
        # Otherwise, reverse i, add i and reverse_i together,
        # and test whether all digits in this sum are odd.
        reverse_i = int(str(i)[::-1])
        if all_digits_odd(i + reverse_i):
            count_reversible += 1
    
    return count_reversible


if __name__ == "__main__":
    print(run())
