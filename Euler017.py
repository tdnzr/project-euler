# Solution to Project Euler problem 17 by tdnzr.

# I don't see how to calculate this trivially, so I'll do it via logical thinking,
# several ugly special cases, and the automated construction of the 1000 strings for the first 1000 numbers.
# The result is pretty messy - there are just too many special cases in languages - but it used to be much worse...


def run():
    oneDigit = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    twoDigitsRegular = ["twenty", "thirty", "forty",
                        "fifty", "sixty", "seventy", "eighty", "ninety"]

    # Only the first 99 numbers are full of special cases. Once we've constructed these, the rest is straightforward.
    one_to_ninetynine = []
    one_to_ninetynine.extend(oneDigit)
    one_to_ninetynine.extend(["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                              "sixteen", "seventeen", "eighteen", "nineteen"])

    for i in twoDigitsRegular:
        one_to_ninetynine.append(i)
        for j in oneDigit:
            one_to_ninetynine.append(i + j)  # Hyphens omitted.

    # Put 1...99 into the final list:
    allDigits = []
    allDigits.extend(one_to_ninetynine)

    # Now that we've constructed the first 99 numbers, constructing numbers 100...999, and 1000, is easy:
    for i in oneDigit:
        allDigits.append(i + "hundred")
        for j in one_to_ninetynine:
            allDigits.append(i + "hundredand" + j)  # Spaces omitted.

    allDigits.append("onethousand")  # Spaces omitted.

    return sum([len(s) for s in allDigits])


if __name__ == "__main__":
    print(run())
