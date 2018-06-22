# Solution to Project Euler problem 99 by tdnzr.

# We're trying to compare which of the pairs of bases and exponents yields the largest result.
# However, calculating the results directly would require comparing numbers with >3 million digits.

# Instead, I prefer using the logarithm to make the comparisons almost trivial:
# A ** B = e ** (ln (A ** B)) = e ** (B * ln(A))
# -> Suddenly, I only need to evaluate B ** ln(A) for each line and compare the results
# to know which line yields the biggest result. That's an enormously efficient algorithm.

# Though do note that the naive comparison, with result = pair[0] ** pair[1], also worked.
# It just had a completion time on the order of 20 minutes (when I ran the program online on repl.it).


from math import log


def run():
    with open("Euler099_base_exp.txt", 'r') as inputFile:
        BasesAndExponents = []
        # Turn the raw text input into a well-formatted list of of pairs of integers (a list of lists):
        for line in inputFile.read().splitlines():
            string_numbers = line.split(',')
            BasesAndExponents.append([int(s) for s in string_numbers])

    # Efficient comparison:
    maximum = 0
    for index, pair in enumerate(BasesAndExponents):
        result = log(pair[0]) * pair[1]  # ln(base) * exponent
        if result > maximum:
            maximum = result
            maxLine = index + 1  # Line number is 1-based, index is 0-based.
    return maxLine


if __name__ == "__main__":
    print(f"Line {run()} yields the largest result.")
