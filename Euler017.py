# Solution to Project Euler problem 17.

# I don't see how to calculate this trivially, so I'll do it via logical thinking,
# tons of ugly special cases, and the automated construction of the 1000 strings for the 1000 numbers.
# The result is a mess. There are just too many special cases in languages. At least the code works!


def run():
    oneDigit = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    specialTen = ["ten"]
    specialNumbers = ["eleven", "twelve", "thirteen", "fourteen", "fifteen",
                        "sixteen", "seventeen", "eighteen", "nineteen"]
    twoDigitsOld = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    specialThousand = ["onethousand"] # Spaces don't count.
    twoDigits = []
    threeDigits = []
    allDigits = []

    for i in twoDigitsOld:
        twoDigits.append(i)
        for j in oneDigit:
            twoDigits.append(i + j)  # i + "-" + j or "%s-%s" would be correct, but there's no need to count hyphens.

    for i in oneDigit:
        threeDigits.append(i + "hundred")
        for j in oneDigit:
            threeDigits.append(i + "hundredand" + j)  # Spaces omitted.
        threeDigits.append(i + "hundredandten")  # Spaces omitted.
        for j in specialNumbers:
            threeDigits.append(i + "hundredand" + j)  # Spaces omitted.
        for j in twoDigits:
            threeDigits.append(i + "hundredand" + j)  # Spaces omitted.

    allDigits.extend(oneDigit)
    allDigits.extend(specialTen)
    allDigits.extend(specialNumbers)
    allDigits.extend(twoDigits)
    allDigits.extend(threeDigits)
    allDigits.extend(specialThousand)

    return sum([len(s) for s in allDigits])


if __name__ == "__main__":
    print(run())
