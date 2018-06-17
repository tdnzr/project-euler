# Solution to Project Euler problem 57.


# I was initially confused regarding how to actually calculate the n-th term of the expansion, regardless of code.
# Iteration 1: 1 + 1/2
# Iteration 2: 1 + 1/(2 + 1/2)
# ...
# I finally came up with this description:
# Start with 0. Add 2, reverse everything, add 2, reverse everything, ..., add 1.
# -> Now the step "add 2" appears n times in the n-th iteration.


from fractions import Fraction


def fraction_expansion(n):
    """Generator which yields the first n fraction expansions."""
    start = 0
    for _ in range(n):  # first n expansions
        start += 2                  # Step 1: Add 2.
        start = Fraction(1, start)  # Step 2: Revert. x -> 1/x.
        yield start + 1             # Step 3: Add 1 to the final result, but don't carry this this over to the next iteration.


def run():
    counter = 0
    for i in fraction_expansion(1000):
        if len(str(i.numerator)) > len(str(i.denominator)):  # fraction = numerator / denominator
            counter += 1
    return counter


if __name__ == "__main__":
    print (f"In the first one-thousand expansions [of this fraction], {run()} fractions have a numerator with more digits than their denominator.")
