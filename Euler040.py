# Solution to Project Euler problem 40 by tdnzr.

# Straightforward solution: Just concatenate the integers
# until I reach a string with a million digits, then
# compute the product in question.


def run():
    # Concatenate the integers into a string:
    testString = ""
    i = 0
    while len(testString) < 1_000_000:
        i += 1
        testString += str(i)

    # Then calculate the product of the digits at position
    # 1, 10, 100, ..., 1,000,000:
    product = 1
    for i in range(7):
        product *= int(testString[(10**i) - 1])

    return product


if __name__ == "__main__":
    print(run())
